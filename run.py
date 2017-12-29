from flask import Flask,render_template
from models.project import Project



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects_list/')
def projects_list():
    project=Project('OA','大地惊雷','panda',None,0.03,0,0,0,0,0,0,0,0,0,'pangzhilei',None,None,None,None,None,None,None,None,None,False,False,None)
    return render_template('projects_list.html', project=project)    


if __name__ == '__main__':
    app.run(debug=True)