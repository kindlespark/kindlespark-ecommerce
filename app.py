from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page() -> str:
    print("Inside home")
    return "Hello from Vinay on the landing page v.0.0.1!"