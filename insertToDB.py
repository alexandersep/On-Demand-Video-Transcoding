import sqlite3, re, os

acceptedResolutions = ["640:480", "1280:720","1920:1080","2560:1440","3840:2160"]
acceptedCodecs = ["H264"]

# Ask to add file, and do so if needed 
# Ensure file conforms to linux naming convention
def maybe_add_gather_file_and_info():
    # currently_adding = True
    # while(currently_adding):
    #     add_file_prompt = str(input("Do you wish to add a file?(y/n) "))
    #     if add_file_prompt != "y":
    #         break;
    #     currently_getting_info = True
    #     while (currently_getting_info):
    #         bool_and_file_name = maybe_name_file("What is the name of your file?")
    #         bool_and_file_path = maybe_get_path("Where is the file located?(File Path)")
    #         bool_and_file_scale = is_get_info_on_arr("What resolution is this media? Accepted resolutions:", 
    #                             acceptedResolutions, "Error: Forbidden resolution.")
    #         if not bool_and_file_scale[0]: 
    #             break;
    #         # bool_and_file_codec = is_get_info_on_arr("What encoding is this media in? Accepted codecs:", 
    #         #                     acceptedCodecs, "Error: Forbidden codec.")
    #         # if not bool_and_file_codec[0]:
    #         #     break;

    #         # # output name may only be applicable in api.py, where the file output name is given.
    #         # bool_and_file_output_name = maybe_name_file("What is the output name of your file?")
    #         # if not bool_and_file_output_name[0]:
    #         #     break;
    #         # print(bool_and_file_scale[1], bool_and_file_codec[1], bool_and_file_output_name[1])
    #         currently_getting_info = False # end while loop

        # add_information_to_db('image-database.db', bool_and_file_name[1], bool_and_file_scale[1], convertToBinaryData(bool_and_file_path))
        add_information_to_db('image-database.db', 'house.jpg', '1280:720', convertToBinaryData('./assets/house.jpg'))

# connect to db and add information
def add_information_to_db(db, name, scale, media):
    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    db_query = """INSERT INTO files
            (file_name, file_scale, media) VALUES (?, ?, ?)"""
    db_tuple = (name, scale, media)
    cursor.execute(db_query, db_tuple) # str converts bytes to string

    conn.commit()
    conn.close()

# create BLOB
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

# Generic: Ask to gather information array and
# if information is not in array error out and return tuple (False,info)
# If not erroring, return (True,info)
def is_get_info_on_arr(question, arr, error_str):
    print(question)
    print(arr)
    info = str(input())
    if info not in arr:
        print(error_str)
        return (False,info)
    return (True,info)

# Name a file if conforms to linux naming convention
# Return False if it does not, and True if it does
def maybe_name_file(question):
    file_name = str(input(question))
    currently_add_file = is_search_file_forbidden(file_name)
    if not currently_add_file:
        return False
    return (True, file_name)
    # Naming file logic goes here #

def maybe_get_path(question):
    file_path = str(input(question))
    return (file_path)

# Given a Boolean if False print error 
# return the same Boolean
def is_search_file_forbidden(file_name):
    search = re.search("/><|:&", file_name) 
    if search:
        print(  "Error: Inputted a character" +
                "that does not conform to linux" +
                "filenaming convention"
                )
    return search

# TODO
# Runs ffmpeg command on filen_name specified
# With accepted_resolution, codecs
# Will always run with -crf 17, and -preset veryslow
# def run_ffmpeg(file_name, resolution, codec):
#     # Logic to convert file_name to dash separated file_name
#     # and additional meta data e.g. to "file-name-4k.mkv"
#     if("." not in file_name):           # NEED TO CHECK IF THIS WORKS
#         print("Invalid file name.")
#         raise Exception("Invalid file name.")

#     file_name_and_type = file_name.split(".")
#     words = file_name_and_type[0].split(" ")
#     file_name_DB = ""
#     for i in words:
#         file_name_DB += i + "-"

#     file_name_DB = file_name_DB[0:-2] #This gets rid of last "-" NOTE: MAY NOT WORK
#     file_name_DB += file_name_and_type[1]

#     ffmpeg_command = (  "ffmpeg -i video.mp4 \\" +
#                         "-vf scale=1920:1080 \\" +
#                         "-c:v libx264 -preset veryslow \\" +
#                         "-crf 0 video-output.mp4"
#                     )

#     os.execute(fmmpeg_command) # Shell command, not Yet implemented
#     return False

maybe_add_gather_file_and_info()