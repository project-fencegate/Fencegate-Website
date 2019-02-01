from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = b'\x0f\x1d\xe1\x98\xed\xc8n\x85\xf4\x95Cg\xdbGC\xf2'


@app.route('/')
def main_page():
    return render_template("browse/plugins.html")


if __name__ == '__main__':
    app.run()
