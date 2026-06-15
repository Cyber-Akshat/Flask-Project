from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Required for flash messages
app.secret_key = "your-secret-key-here"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Example authentication
        if email == "admin@example.com" and password == "password123":
            return redirect(url_for("home"))

        flash("Invalid email or password")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Passwords do not match")
            return redirect(url_for("register"))

        # Save user to database here

        flash("Account created successfully!")
        return redirect(url_for("login"))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)