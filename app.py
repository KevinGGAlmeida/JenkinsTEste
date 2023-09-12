from flask import render_template,flash,Flask

app = Flask(__name__,static_folder='static', template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)