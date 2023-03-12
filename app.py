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
    return "Hello from Kindlespark the landing page v.0.0.1!"

@app.route("/modem")
def modem_page() -> str:
    print("Method added by Rahul Sanyasi")
    return "Hello from Rahul Sanyasi the landing page v.0.0.2!"

@app.route("/mixer")
def mixer_page() -> str:
    print("Method added by Kiran Bhamare")
    return "Hello from Kiran the landing page v.0.0.1!"

@app.route("/bike")
def bike_page() -> str:
    print("Method added by Aniruddha Bhamare")
    return "Hello from Aniruddha the landing page v.0.0.1!"

@app.route("/stove")
def stove_page() -> str:
    print("Method added by Ananta Sonawane")
    return "Hello from Ananta-kindlespark the landing page v.0.0.2!"