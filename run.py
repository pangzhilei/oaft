from flask import Flask,render_template,request
from models.project import Project
from urllib.parse import unquote



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects_list/')
def projects_list():
    project=Project('OA','大地惊雷','panda',None,0.03,0,0,0,0,0,0,0,0,0,'pangzhilei',None,None,None,None,None,None,None,None,None,False,False,None)
    return render_template('projects_list.html', project=project)    

@app.route('/rq/')
def rq():
    return 'heloo',404,{'content-type':text/plain}

@app.route('/test/')
def test():
    return render_template('test.html')

@app.route('/get/',methods=['post'])
def get():
    name=request.values.get('user')

    return f'my name is {name}'

if __name__ == '__main__':
    app.run(debug=True)