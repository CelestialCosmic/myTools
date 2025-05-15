
import requests
from langchain_nvidia_ai_endpoints import ChatNVIDIA

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

import requests
import base64

def ask_about_image(image_url, question="Describe the image"):
    invoke_url = "http://localhost:9000/v1/chat/completions"
    stream = False
    with open(image_url, "rb") as f:
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
    return response.json()["choices"][0]["message"]["content"]

    ####################################################################
    ## < EXERCISE SCOPE

    ## TODO: Implement the method by connecting to a vision-language model

    ## EXERCISE SCOPE >
    ####################################################################

from diffusers import DiffusionPipeline
import torch

## TODO: Consider initializing your diffusion pipeline outside of generate_images

## TODO: Implement this method
def generate_images(prompt):
    ####################################################################
    # < EXERCISE SCOPE    
    pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16",
    ).to("cuda")
    images = pipe(prompt=prompt).images
    return images
    ## EXERCISE SCOPE >
    ####################################################################

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

####################################################################
## < EXERCISE SCOPE

## TODO: Create a pipeline for synthetic prompts, optputting a string.

## EXERCISE SCOPE >
####################################################################
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch
from random import random
def generate_new_prompt(desc):
    state = {"messages": []}
    agent_msg = ""
    sys_msg = (
        "Focus on the main subject and its environment.but generate in different style or type (e.g., photography, illustration, concept art, etc.)Include at least one technical or artistic detail (e.g., lighting, camera type, resolution, etc.)Use clear, descriptive, comma-separated keywords or phrasesAvoid abstract or subjective terms (e.g., beautiful or amazing)Keep prompts under 75 tokensEach prompt should vary in style, perspective, or composition.generate four kind of prompt,one kind in one line,only prompts,no other word,dont descript what it is"
    )
    # print(sys_msg)
    prompt = ChatPromptTemplate.from_messages([("system", sys_msg),("question","help me generate four prompt which is the same as main subject,but different in theme,background or color"),("user",desc)])
    chain = prompt | llm
    for token in chain.stream(state):
        # print(token.content)
        agent_msg += str(token.content)
        # print(agent_msg)
    new_diff_prompt = agent_msg.split("\n")
    # print(new_diff_prompt[2:6])
    return new_diff_prompt[2:6]

## TODO: Execute on assessment objective
def generate_images_from_image(image_url: str, num_images = 4):

    ####################################################################
    ## < EXERCISE SCOPE

    ## TODO: Generate the description of the image provided in image_url
    original_description = ask_about_image(image_url, question="Describe the image")
    ## TODO: Generate four disjoint prompts, hopefully different, to feed into SDXL
    diffusion_prompts = generate_new_prompt(str(original_description))

    ## TODO: Generate the resulting images
    for prompt in diffusion_prompts:
        print(prompt)
        # generate_images(prompt)
    generated_images = []

    ## EXERCISE SCOPE >
    ####################################################################
        
    return generated_images, diffusion_prompts, original_description

results = []
results += [generate_images_from_image("imgs/agent-overview.png")]
results += [generate_images_from_image("imgs/multimodal.png")]
results += [generate_images_from_image("img-files/tree-frog.jpg")]
results += [generate_images_from_image("img-files/paint-cat.jpg")]