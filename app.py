from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api, reqparse
import werkzeug, os

from mat import process_image

app = Flask(__name__)
api = Api(app)

app.config['SITE_TITLE'] = 'My cool site.'

app.config['NAVBAR'] = [
              { 'text':'Homepage', 'url':'/' },
              { 'text':'About Page', 'url':'/about' },
              {'text':'More', 'sublinks': [ 
                        {'text':'Stack Overflow','url':'https://stackoverflow.com'},
                        {'text':'Google','url':'https://google.com/'},
                         ], 
                         },
              # {'text':'Github','url':'https://github.com/'}
                         ]  
                        

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = ['csv','txt']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

parser = reqparse.RequestParser()
parser.add_argument('file',
    type=werkzeug.datastructures.FileStorage,
    location='files')

class FileUpload(Resource):
    def post(self):
        data = parser.parse_args()
        if data['file'] == None:
            return jsonify({'result':'No file was uploaded.'})

        if data['file'] == '':
            return jsonify({'result':'Invalid file.'})

        if not allowed_file(data['file'].filename):
            return jsonify({'result':'Invalid File'})

        csv = data['file']

        if csv:
            #photo.save(os.path.join(UPLOAD_FOLDER, filename))
            process_image(csv,'output_from_flask.png')
            return jsonify({'result':'success'})

api.add_resource(FileUpload, '/upload')




@app.context_processor 
def inject_dict_for_all_templates():
    """ Build the navbar and pass this to Jinja for every route
    """
    # Build the Navigation Bar
    nav =[]
    

    for item in app.config['NAVBAR']:
        nav.append(item)
        
    return dict(navbar = nav)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)