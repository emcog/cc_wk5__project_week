from flask import Flask, render_template

from controllers.controller_farmer import farmer_blueprint

app = Flask(__name__)

app.register_blueprint(farmer_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)