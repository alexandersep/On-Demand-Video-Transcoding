import sqlite3
import re

acceptedResolutions = ["640:480", "1280:720","1920:1080","2560:1440","3840:2160"]
acceptedCodecs = ["I'll do this later"]

addingFiles = True
while(addingFiles):
    currentlyAdding = False
    addFilePrompt = str(input("Do you wish to add a file?(y/n)"))
    if addFilePrompt == "y":
        currentlyAdding = True
    else:
        addingFiles = False

    while(currentlyAdding):
        fileName = str(input("What is the name of your file?"))
        forbidden = True if (re.search("[/><|:&]", fileName)) or (fileName == "/") else False
        if forbidden:
            print("Error: Forbidden characters in file name.")
            currentlyAdding = False
            break
    
        print("What resolution is this media? Accepted resolutions:")
        print(acceptedResolutions)
        fileScale = str(input())
        if(fileScale not in acceptedResolutions):
            print("Error: Forbidden resolution.")
            currentlyAdding = False
            break
        
        print("What encoding is this media in? Accepted codeccs:")
        print(acceptedCodecs)
        fileCodec = str(input())
        if(fileCodec not in acceptedCodecs):
            print("Error: Forbidden codec.")
            currentlyAdding = False
            break

        fileOutputName = str(input("What is the output name of your file?"))
        forbidden = True if (re.search("[/><|:&]", fileName)) or (fileName == "/") else False
        if forbidden:
            print("Error: Forbidden characters in file name.")
            currentlyAdding = False
            break

        print(fileName, fileScale, fileCodec, fileOutputName)
        currentlyAdding = False

    else:
        addingFiles = False
