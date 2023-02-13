from flask import Flask
from flask_restful import Resource, Api, reqparse
import sqlite3
import base64
import os
import io
import PIL.Image as Image

app = Flask(__name__)
api = Api(app)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# this class will accept the post req. from front end, run the command, and send back the media
class transcoder(Resource):
    def post(self):
        parser = reqparse.RequestParser() # checks for requirements
        parser.add_argument('mediaName', required = True)
        parser.add_argument('mediaScale', required = True)
        parser.add_argument('mediaEncoding', required = True)
        parser.add_argument('mediaNameOutput', required = True)

        args = parser.parse_args()

        

        # to be completed: 
        ## store images on database, 
        ## have image be stored after transcoding, 
        ## send image in return statement as BLOB.
        db_path = os.path.join(__location__, 'video-database.db')
        db_connection = connection(db_path)

        # creates db cursor
        main_cursor = db_connection.cursor()

        # NOTE: below probably doesn't work
        # searches for requested file
        file_name = main_cursor.execute("SELECT file_name FROM files WHERE file_name = '" +  args['mediaName'] + "'")
        # file_name = main_cursor.execute("SELECT file_name FROM files WHERE file_name = 'house.jpg'")
        
        file_name = main_cursor.fetchone()

        # if the file is found
        if(file_name[0] == args['mediaName']):
            # save as image temporarily under the same name
            # with open(__location__ + "/" + args['mediaName'], 'wb') as media:
            # save image by decoding BLOB, by finding image in the same row as the file_name
            file_media = main_cursor.execute("SELECT file_path FROM files WHERE (file_name='" +  args['mediaName'] + "')")
            file_media = main_cursor.fetchone()

            # transcodes video
            os.system(  "ffmpeg -i " + __location__ + "\\assets\\" + args['mediaName'] + 
                        " -vf scale=" + args['mediaScale'] +
                        " -c:v " + args['mediaEncoding'] + " -preset veryslow"  +
                        " " + __location__ + "\\" + args['mediaNameOutput'] 
            )           

            db_connection.close()
            return convertToBinaryData(__location__ + "\\transcoded-assets\\" + args['mediaName'])
        else:
            db_connection.close()
            return "ERROR: Media   not found."

# API endpoint
api.add_resource(transcoder, '/transcoder')

# db connection 
# NOTE: Should probably have a try catch statement
def connection(db):
    conn = sqlite3.connect(db)
    return conn

# create BLOB
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

# runs program if running from this file
if __name__ == '__main__':
    app.run(port=4000, debug=True)