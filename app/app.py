from flask import Flask,  request, render_template
from genel import Genel
genel = Genel()

app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        link=request.form["username"]
        email=request.form["email"]

        genel.download_video(link,'hey.mp4')
        print(link)
        print(email)

    return render_template("add_user.html")

if __name__=='__main__':
    app.run()
