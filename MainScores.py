from Utils import general_information
from flask import Flask, redirect, request
app = Flask(__name__)
SCORES_FILE_NAME = general_information()[0]


def score_server():
    try:
        file = open(SCORES_FILE_NAME, "r")
        the_score = file.read()
        sending = f'''<html>
    <head>
    <title>Scores Game</title>
    </head>
    <body>
    <h1>The score is <div id="score">{the_score}</div></h1>
    </body>
    </html>'''
    except:
        sending = f'''<html>
    <head>
    <title>Scores Game</title>
    </head>
    <body>
    <body>
    <h1><div id="score" style="color:red">{'ERROR'}</div></h1>
    </body>
    </html>'''

    @app.route("/")
    def web_score():
        if request.method == "GET":
            return sending
        elif request.method == "POST":
            return "you are doing something wrong"

    app.run(host="0.0.0.0", port=5001, debug=True)


score_server()