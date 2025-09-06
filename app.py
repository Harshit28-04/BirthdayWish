from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age_raw = request.form.get("age", "0").strip()

        # Basic validation & friendly defaults
        try:
            age = int(age_raw)
        except ValueError:
            age = 1
        age = max(1, min(120, age))  # clamp between 1 and 120

        if not name:
            name = "Birthday Star"

        return render_template("birthday.html", name=name, age=age)

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)