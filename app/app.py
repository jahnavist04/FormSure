
from flask import Flask, render_template, request
from validator import validate_application

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

@app.route("/", methods=["GET", "POST"])
def home():

    errors = []
    success = False

    if request.method == "POST":

        data = request.form
        files = request.files

        errors = validate_application(data, files)

        if not errors:
            success = True

    return render_template(
        "index.html",
        errors=errors,
        success=success
    )


if __name__ == "__main__":
    app.run(debug=True)
