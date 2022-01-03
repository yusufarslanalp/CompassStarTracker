from flask import Flask, request, flash, redirect
from flask_restful import Resource, Api

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
        print( "HEREEE00000" )

        # check if the post request has the file part
        print( request.headers )
        print( request.form.get('image124') )
        print( request.files )
        """if 'img.png' not in request.files:
            print( "HEREEE0.1" )
            flash('No file part')
            return redirect(request.url)"""

        print( "HEREEE1111111111111111111111111111111" )
        file = request.files['file_field']
        print( "HEREEE2222222222222222222222222222222" )

        # if user does not select file, browser also
        # submit an empty part without filename
        print( ":::::::" + file.name )
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        #if file and allowed_file(file.filename):
        print( "HEREEE2" )
        #filename = secure_filename(file.filename)
        file.save( "ReceivedImages/" + file.filename )
        """new_image = Image(
            path= ".",
            filename="fff.png",
            ext= "png"
        )"""
        # Save new_image model
        #return redirect(url_for('uploaded_file', filename="fff.png"))
        print( "Before return" )
        return { "lat": 40.809, "longi": 29.362 }


api.add_resource(HelloWorld, '/')

api.add_resource( Image, '/image')


#app.run(debug=True)
app.run(host='0.0.0.0', port=80)