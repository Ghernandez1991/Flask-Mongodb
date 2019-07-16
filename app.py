#import libraries

from flask import Flask, render_template
import pymongo
import scrape

#create flask instance
app = Flask(__name__)

#create mongo connection
client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data_entries

@app.rout("/")
def home():
    mars_data = list(db.collecion.find())[0]
    return render_template('index.html', mars_data=mars_data)

@app.rout("/scrape")
def scrape():
    db.collection.remove({})

    db.collection.insert_one(mars_data)
    return render_template('scrape.html')


if __name__ == "__main__":
    app.run(debug=True)
