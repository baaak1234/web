from flask import Flask, render_template,request,jsonify
from routes import register_blueprints


app = Flask(__name__)

register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)
