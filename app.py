# Product Price Comparison Microservice - Customized by Ezedeen (ezedeem223)
# IBM Final Project: Application Development using Microservices and Serverless
# Author: Ezedeen | GitHub: ezedeem223 | March 2026

from flask import Flask
from flask_cors import CORS
from flask import send_from_directory

app = Flask("Product deal check")
CORS(app)

@app.route("/")
def getHomePage():
  return send_from_directory('html', "index.html")

if __name__=="__main__":
    app.run(port=5001,debug=True) 
    # When no port is specified, starts at default port 5000


# Powered by Ezedeen (ezedeem223) - IBM Microservices Final Project 2026
