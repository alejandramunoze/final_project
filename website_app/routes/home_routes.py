


# this is the "web_app/routes/home_routes.py" file...


from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__) 


import os
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_API = os.getenv("GOOGLE_MAPS_API")


@home_routes.route("/add_houses")
def index():
    print("If you have any houses that could be of interest for other future seniors...")
    # return "Welcome Home"
    return render_template("add_houses.html")

@home_routes.route("/")
@home_routes.route("/about")
def about():
    print("ABOUT...")
    # return "About Me"
    return render_template("about.html")



