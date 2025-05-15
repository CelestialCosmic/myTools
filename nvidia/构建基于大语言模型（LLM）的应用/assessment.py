import requests
import base64
import os 
import re
from chatbot.conv_tool_caller import ConversationalToolCaller
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.pydantic_v1 import Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from chatbot.jupyter_tools import FileLister
from diffusers import DiffusionPipeline
import torch
import requests
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.runnables import Runnable, RunnableAssign, RunnablePassthrough, RunnableLambda
from langgraph.prebuilt import ToolNode

## USE THIS ONE TO START OUT WITH. NOTE IT'S INTENTED USE AS A VISUAL LANGUAGE MODEL FIRST
# model_path="http://localhost:9000/v1"
## USE THIS ONE FOR GENERAL USE AS A SMALL-BUT-PURPOSE CHAT MODEL BEING RAN LOCALLY VIA NIM
model_path="http://nim:8000/v1"
# ## USE THIS ONE FOR ACCESS TO CATALOG OF RUNNING NIM MODELS IN `build.nvidia.com`
# model_path="http://llm_client:9000/v1"

model_name = requests.get(f"{model_path}/models").json().get("data", [{}])[0].get("id")
%env NVIDIA_BASE_URL=$model_path
%env NVIDIA_DEFAULT_MODE=open

if "llm_client" in model_path:
    model_name = "meta/llama-3.1-70b-instruct"

llm = ChatNVIDIA(model=model_name, base_url=model_path, max_tokens=5000, temperature=0)
def ask_about_image(image_path, question="Describe the image"):
    invoke_url = "http://localhost:9000/v1/chat/completions"
    stream = False
    with open("./img-files/paint-cat.jpg", "rb") as f:
      image_b64 = base64.b64encode(f.read()).decode()
    
    headers = {
        "Authorization": "Bearer $API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC",
        "Accept": "text/event-stream" if stream else "application/json"
    }
    
    payload = {
        "model": 'microsoft/phi-3.5-vision-instruct',
        "messages": [
            {'role': 'system', 'content': '{question}'},
            {'role': 'user', 'content': [
                {'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{image_b64}', 'detail': 'low'}}
            ]},
        ],
        "max_tokens": 512,
        "temperature": 0.20,
        "top_p": 0.70,
        "stream": stream
    }
    response = requests.post(invoke_url, headers=headers, json=payload)
    desc = response.json()["choices"][0]["message"]["content"]
    return desc

def generate_images(prompt):
    pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16",
    ).to("cuda")
    images = pipe(prompt=prompt).images
    return images

def diffusion_prompts_func(original_description):
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Focus on the main subject and its environment.Specify the style or type (e.g., photography, illustration, concept art, etc.)Include at least one technical or artistic detail (e.g., lighting, camera type, resolution, etc.)Use clear, descriptive, comma-separated keywords or phrasesAvoid abstract or subjective terms (e.g., beautiful or amazing)Keep prompts under 75 tokensEach prompt should vary in style, perspective, or composition"),
    ])
    agent_prompt = ChatPromptTemplate.from_messages([
    (("system", "Focus on the main subject and its environment.Specify the style or type (e.g., photography, illustration, concept art, etc.)Include at least one technical or artistic detail (e.g., lighting, camera type, resolution, etc.)Use clear, descriptive, comma-separated keywords or phrasesAvoid abstract or subjective terms (e.g., beautiful or amazing)Keep prompts under 75 tokensEach prompt should vary in style, perspective, or composition"),
    ),
    ("user", original_description)])
    return response

def generate_images_from_image(image_url: str, num_images = 4):
    original_description = ask_about_image(image_url)
    new_diff_prompt = diffusion_prompts_func(original_description)
    diffusion_prompts = [line for line in new_diff_prompt.split('\n') if re.match(r'^\d+\.',line.strip())]
    print(diffusion_prompts)
    generated_images = []
    for prompt in diffusion_prompts:
       print(prompt)
       images = generate_images(prompt)
       generated_images += images
       for img in images:
          img.show()
    return generated_images, diffusion_prompts, original_description

results = []
results += [generate_images_from_image("imgs/agent-overview.png")]
results += [generate_images_from_image("imgs/multimodal.png")]
results += [generate_images_from_image("img-files/tree-frog.jpg")]
results += [generate_images_from_image("img-files/paint-cat.jpg")]
