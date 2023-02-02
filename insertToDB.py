import sqlite3, re, os

acceptedResolutions = ["640:480", "1280:720","1920:1080","2560:1440","3840:2160"]
acceptedCodecs = ["H264"]

# Ask to add file, and do so if needed 
# Ensure file conforms to linux naming convention
def maybe_add_gather_file_and_info():
    currently_adding = True
    while(currently_adding):
        add_file_prompt = str(input("Do you wish to add a file?(y/n) "))
        if add_file_prompt != "y":
            break;
        currently_getting_info = True
        while (currently_getting_info):
            maybe_name_file("What is the name of your file?")
            bool_and_file_scale = is_get_info_on_arr("What resolution is this media? Accepted resolutions:", 
                                acceptedResolutions, "Error: Forbidden resolution.")
            if not bool_and_file_scale[0]: 
                break;
            bool_and_file_codec = is_get_info_on_arr("What encoding is this media in? Accepted codecs:", 
                                acceptedCodecs, "Error: Forbidden codec.")
            if not bool_and_file_codec[0]:
                break;
            bool_and_file_output_name = maybe_name_file("What is the output name of your file?", file_name)
            if not bool_and_file_output_name[0]:
                break;
            print(bool_and_file_scale[1], bool_and_file_codec[1], bool_and_file_output_name[1])
            currently_getting_info = False # end while loop

# Generic: Ask to gather information array and
# if information is not in array error out and erturn False
# If not erroring, return True
def is_get_info_on_arr(question, arr, error_str):
    print(question)
    print(arr)
    info = str(intput())
    if info not in arr:
        print(error_str)
        return (False,info)
    return (True,info)

# Name a file if conforms to linux naming convention
# Return False if it does not, and True if it does
def maybe_name_file(question, file_name):
    file_name = str(input(question))
    currently_add_file = is_search_file_forbidden(file_name)
    if not currently_add_file:
        return False
    return True
    # Naming file logic goes here #

# Given a Boolean if False print error 
# return the same Boolean
def is_search_file_forbidden(file_name):
    search = re.search("/><|:&", file_name) 
    if search:
        print("Error: Inputted a character 
            that does not conform to linux
            filenaming convention")
    return search

# Runs ffmpeg command on filen_name specified
# With accepted_resolution, codecs
# Will always run with -crf 17, and -preset veryslow
def run_ffmpeg(file_name, resolution, codec):
    # Logic to conver file_name to dash separated file_name
    # and additional meta data e.g. to "file-name-4k.mkv"
    # os.execute(fmmpeg_command) # Shell command, not Yet implemented
    return False

maybe_add_gather_file_and_info()
