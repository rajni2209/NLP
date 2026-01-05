from flask import Flask, render_template, request, redirect, session, url_for
import model

app = Flask(__name__)
app.secret_key = "secret123"   # for session

# 🔹 Create table
model.create_table()

# 🔹 AUTO CREATE DEFAULT USER (runs once)
try:
    model.add_user("admin", "admin123")
except:
    pass   # user already exists, ignore error

@app.route("/")
def home():
    if "user" in session:
        return render_template("index.html", user=session["user"])
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = model.validate_user(username, password)
        if user:
            session["user"] = username
            return redirect("/")
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
