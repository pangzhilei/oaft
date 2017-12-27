from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'


@app.route('/nihao/')
def nihao():
    return 'ni hao'    


if __name__ == '__main__':
    app.run(debug=True)