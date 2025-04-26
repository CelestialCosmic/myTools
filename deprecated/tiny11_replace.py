# 脚本来源：https://github.com/ntdevlabs/tiny11builder/issues/101

import re

print("Inform the drive letter of the mounted image: ", end="")
drive_letter = input().upper()
if len(drive_letter) == 1:
    drive_letter = drive_letter + ":"
elif len(drive_letter) == 2:
    drive_letter = drive_letter[0] + ":"
elif len(drive_letter) == 3:
    drive_letter = drive_letter[0] + ":"
else:
    print("Invalid drive letter informed. Please inform a valid drive letter.")
    exit()

file_name = (
    drive_letter
    + "\\sources\\replacementmanifests\\microsoft-windows-appx-deployment-server\\appxprovisioning.xml"
)

# Read in the file
with open(file_name, "r", buffering=4096, encoding="UTF-8") as file:
    file_contents = file.read()

system_package_list = [
    "Clipchamp\.Clipchamp_",
    "Microsoft\.BingNews_",
    "Microsoft\.BingWeather_",
    "Microsoft\.GamingApp_",
    "Microsoft\.GetHelp_",
    "Microsoft\.Getstarted_",
    "Microsoft\.MicrosoftOfficeHub_",
    "Microsoft\.MicrosoftSolitaireCollection_",
    "Microsoft\.People_",
    "Microsoft\.PowerAutomateDesktop_",
    "Microsoft\.Todos_",
    "Microsoft\.WindowsAlarms_",
    "microsoft\.windowscommunicationsapps_",
    "Microsoft\.WindowsFeedbackHub_",
    "Microsoft\.WindowsMaps_",
    "Microsoft\.WindowsSoundRecorder_",
    "Microsoft\.Xbox.TCUI_",
    "Microsoft\.XboxGamingOverlay_",
    "Microsoft\.XboxGameOverlay_",
    "Microsoft\.XboxSpeechToTextOverlay_",
    "Microsoft\.YourPhone_",
    "Microsoft\.ZuneMusic_",
    "Microsoft\.ZuneVideo_",
    "MicrosoftCorporationII\.MicrosoftFamily_",
    "MicrosoftCorporationII\.QuickAssist_",
    "MicrosoftTeams_",
    "Microsoft\.549981C3F5F10_",
]
print("\nReplace the lines below in the original creator bat:\n")
error_list = []
for package_name in system_package_list:
    pattern = rf'<Package FullName="({package_name}.*?)" PackageType="bundle"/>'
    # Find the first match using the regex pattern
    match = re.search(pattern, file_contents)
    # Print the first match if found
    if match:
        print(
            "dism /image:c:\\scratchdir /Remove-ProvisionedAppxPackage /PackageName:"
            + match.group(1)
        )
    else:
        error_list.append(
            f"ERROR: No match was found for package: {package_name.split('.', 1)[0]}"
        )
for error in error_list:
    print(error)