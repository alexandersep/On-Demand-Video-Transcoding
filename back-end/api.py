from flask import Flask
from flask_restful import Resource, Api, reqparse
import sqlite3
import base64
import tempfile
import os

app = Flask(__name__)
api = Api(app)

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
        db_connection = connection('image-database.db')

        # creates db cursor
        main_cursor = db_connection.cursor()

        # NOTE: below probably doesn't work
        # searches for requested file
        file_name = main_cursor.execute("SELECT file_name FROM files WHERE (file_name = " +  args['mediaName'] + ")")

        # if the file is found
        if(file_name == args['mediaName']):
            # save as image temporarily under the same name
            with tempfile.NamedTemporaryFile(mode="wb") as media:
                # save image by decoding BLOB, by finding image in the same row as the file_name
                media.write(base64.decodebytes(main_cursor.execute("SELECT media, file_name FROM files WHERE (file_name = " +  args['mediaName'] + ")")))

                # transcodes image
                os.system(  "ffmpeg -i " + media.name + " \\ "           +
                            "-vf scale=" + args['mediaScale'] + " \\ "           +
                            "-c:v " + args['mediaEncoding'] + " -preset veryslow \\ "  +
                            "-crf 0 ./transcoded-images/" + args['mediaNameOutput'] 
                            )
            
            db_connection.close()

            return 1
        else:
            db_connection.close()
            return "ERROR: Media not found."

# API endpoint
api.add_resource(transcoder, '/transcoder')


# db connection 
# NOTE: Should probably have a try catch statement
def connection(db):
    conn = sqlite3.connect(db)

    return conn

# runs program if running from this file
if __name__ == '__main__':
    app.run()