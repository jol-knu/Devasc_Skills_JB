from flask import Flask
from flask import request

sample = Flask(__name__)

@sample.route("/")
def main():
    return "listen to port 8080" + "\n"
    
    
if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)
