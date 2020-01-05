from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/form")
def form():
    return render_template('form.html')


app.run(debug="TRUE")
