from flask import Flask

app = Flask(__name__)

app.secret_key = b'\x0f\x1d\xe1\x98\xed\xc8n\x85\xf4\x95Cg\xdbGC\xf2'


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
