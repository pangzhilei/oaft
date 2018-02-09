from flask import Flask,render_template,request
from models.project import Project
from urllib.parse import unquote


#从头学起
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
    return render_template('main.html')

@app.route('/test/')
def test():
    return render_template('projects_list.html')

@app.route('/get/')
def get():
    return render_template('/get.html/')

if __name__ == '__main__':
    app.run(debug=True)