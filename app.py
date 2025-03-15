from flask import Flask, render_template
from flask_tailwind import Tailwind

app = Flask(__name__, static_folder='static')


tailwind = Tailwind(app)

@app.route('/')
def home():
    return render_template ("index.html")

if __name__ == "__main__":
    app.run(debug=True)
