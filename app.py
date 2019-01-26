from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

@app.route('/upload/', methods=['GET','POST'])
def upload():
    return render_template('upload.html')

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
    app.run(debug=True)