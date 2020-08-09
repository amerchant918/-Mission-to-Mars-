from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Scrape Data and pull into Mongo DB
@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    marsdata = scraping.scrape_all()
    mars.replace_one({}, marsdata, upsert=True)
    return "Scraping Successful"



if __name__ == "__main__":
    app.run()