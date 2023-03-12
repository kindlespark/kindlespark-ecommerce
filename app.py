from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page() -> str:
    print("Inside home")
    return "Hello from KindleSpark Team on the landing page v.0.0.3!"

@app.route("/shop")
def shop_page() -> str:
    print("Method added by Rakesh Jagtap")
    return "Hello from Rakesh the landing page v.0.0.1!"

@app.route("/toaster")
def toaster_page() -> str:
    print("Method added by Ashwini Shimpi")
    return "Hello from Ashwini the landing page v.0.0.1!"