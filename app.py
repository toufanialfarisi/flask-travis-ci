from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])


@app.route("/", methods=["POST", "GET"])
def index():
    if "log_message" in session:
        return render_template("index.html", message=session["log_message"])
    else:
        return render_template("index.html")


@app.route("/about", methods=["POST", "GET"])
def about():
    if "log_message" in session:
        return render_template("about.html")
    else:
        return render_template("login.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if "log_message" in session:
        return render_template("contact.html")
    else:
        return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if "log_message" in session:
        return redirect(url_for("index"))
    else:
        if request.method == "POST":
            nama = request.form.get("nama", None)
            username = request.form.get("username", None)
            if nama == "admin" and username == "admin":
                session["log_message"] = "login sukses"
                print("login sukses")
                return redirect(url_for("index"))
            else:
                print("login gagal")
                return redirect(url_for("login"))
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
