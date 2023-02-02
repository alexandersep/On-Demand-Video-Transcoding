from flask import Flask
from flask_restful import Resource, Api, reqparse

import os

app = Flask(__name__)
api = Api(app)

class transcoder(Resource):
    def post(self):
        parser = reqparse.RequestParser() # checks for requirements
        parser.add_argument('mediaName', required = True)
        parser.add_argument('mediaScale', required = True)
        parser.add_argument('mediaEncoding', required = True)
        parser.add_argument('mediaNameOutput', required = True)

        args = parser.parse_args()

        # transcodes image
        os.system(  "ffmpeg -i " + args['mediaName'] + " \\ "           +
                    "-vf scale=" + args['mediaScale'] + " \\ "           +
                    "-c:v " + args['mediaEncoding'] + " -preset veryslow \\ "  +
                    "-crf 0 " + args['mediaNameOutput'] 
                    )

        # to be completed: 
        ## store images on database, 
        ## have image be stored after transcoding, 
        ## send image in return statement as BLOB.
        
        # placeholder
        return ("Media Name: " + args['mediaName'] + 
        "\nMedia Scale:  " + args['mediaScale'] + 
        "\nMedia Encoding" + args['mediaEncoding'] + 
        "\nMedia Output Name:  " + args['mediaNameOutput']) 

# API endpoint
api.add_resource(transcoder, '/transcoder')


# runs program if running from this file
if __name__ == '__main__':
    app.run()