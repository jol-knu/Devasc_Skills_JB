from flask import Flask
from flask import request

sample = Flask(__name__)

@sample.route("/")
def main():
    return "Jenkins listen to port 5050" + "\n"
    
    
if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050