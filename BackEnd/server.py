from flask import Flask, request, flash, redirect
from flask_restful import Resource, Api
import find_cordinate as fc

app = Flask(__name__)
api = Api(app)
app.secret_key = "super secret key"

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Image(Resource):
    def get(self):
        return {'hello': 'Image'}

    def post( self ):

        print( "imageeeeeeeeeeeeeee" )
        file = request.files['file_field']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        #filename = secure_filename(file.filename)
        file.save( "ReceivedImages/" + file.filename )



        print( "Before return" )
        return fc.find_cordinate( file.filename )


api.add_resource(HelloWorld, '/')

api.add_resource( Image, '/image')


#app.run(debug=True)
app.run(host='0.0.0.0', port=5000)
