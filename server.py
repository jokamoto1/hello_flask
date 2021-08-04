from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!' 
# @app.route('/dojo')          
# def dojo():
#     return 'Dojo!' 
# @app.route('/say/flask')          
# def flask():
#     return 'Hi Flask!'
# @app.route('/say/michael')          
# def michael():
#     return 'Hi Michael!'
# @app.route('/say/john')          
# def john():
#     return 'Hi John!'
@app.route('/35/hello')          
def hello():
    return 'hello\n'*35
# @app.route('/int(80)/bye')          
# def bye():
#     return 'bye\n'*80
# @app.route('/99/dogs')          
# def dog():
#     return 'dogs\n'*99
if __name__=="__main__":   
    app.run(debug=True)   
