from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from datetime import datetime

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

posts = []
posts.append({
    "author": "dev",
    "content": "j'ai finit de dev jvais dormir 😴😴😴",
    "date": "17/11",
    "time": "4h09"
})
posts.append({
    "author": "Eagle",
    "content": "Bonjour c'est le cm, ceci est mon premier post !",
    "date": "18/11",
    "time": "20h25"
})

@app.route("/")
def index():
    if 'username' in session:
        return render_template("index.html", last_posts=list(reversed(posts)), username=session['username'])
    return render_template("index.html", last_posts=list(reversed(posts)), username=None)

@app.route("/post/<post_id>", methods=['GET'])
def get_post(post_id):
    return render_template("post.html", post=posts[int(post_id)])

@app.route("/post/send", methods=['GET'])
def send_post():
    if request.args.get('content', '') != "":
        dt = datetime.now()
        posts.append({
            "author": request.args.get('author', ''),
            "content": request.args.get('content', ''),
            "date": str(dt.day) + "/" + str(dt.month),
            "time": str(dt.hour) + "h" + str(dt.minute)
        })
    return redirect(url_for("index"))

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("index"))