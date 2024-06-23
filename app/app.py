from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Trying to work with jenkins pipeline and email notification!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
