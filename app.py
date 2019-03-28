import pymongo
import json
import requests
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from bson import json_util, ObjectId

import shopify


app = Flask(__name__)
client = pymongo.MongoClient(
    "mongodb+srv://new-user:newuser1234@golangcluster-hqxdo.mongodb.net/test?retryWrites=true")

db = client.omnisend


# API for comments from mongodb

@app.route("/reviews_api", methods=['GET'])
def reviews_api_all():
    review = db.reviews
    limit = int(request.args['limit'])
    offset = int(request.args['offset'])

    rev = review.find().sort(
        '_id', pymongo.ASCENDING).limit(limit)

    output = []
    for q in rev:
        output.append(
            {'rating': q['rating'], 'comment': q['comment'], 'author': q['author']})

    next_url = '/reviews_api' + '?limit=' + str(limit) + \
        '&offset=' + str(offset + limit)
    prev_url = '/reviews_api' + '?limit=' + str(limit) + \
        '&offset=' + str(max(0, (offset - limit)))

    return jsonify({'result': output, 'prev_url': prev_url, 'next_url': next_url})


@app.route("/reviews_api/<rating>", methods=['GET'])
def reviews_api(rating):
    new_rating = rating.replace('_', ' ')
    review = db.reviews
    limit = int(request.args['limit'])
    offset = int(request.args['offset'])

    rev = review.find({'rating': new_rating}).sort(
        '_id', pymongo.ASCENDING).limit(limit)

    output = []
    for q in rev:
        output.append(
            {'rating': q['rating'], 'comment': q['comment'], 'author': q['author']})

    next_url = '/reviews_api/' + \
        rating.replace(' ', '_') + '?limit=' + str(limit) + \
        '&offset=' + str(offset + limit)
    prev_url = '/reviews_api/' + \
        rating.replace(' ', '_') + '?limit=' + str(limit) + \
        '&offset=' + str(max(0, (offset - limit)))

    return jsonify({'result': output, 'prev_url': prev_url, 'next_url': next_url})


# //Routes

@app.route("/")
def ratings_all():
    r = requests.get(
        'https://shopify-reviews-api.herokuapp.com/reviews_api?limit=3000&offset=0')
    reviews_data = r.json()
    comments = reviews_data['result']
    # next_page = reviews_data['next_url']
    prev_page = reviews_data['prev_url']
    return render_template('index.html', name="Omnisend reviews", comments=comments, api=prev_page)


@app.route("/rating_1")
def rating_1():
    r = requests.get(
        'https://shopify-reviews-api.herokuapp.com/reviews_api/1_of_5_stars?limit=3000&offset=0')
    reviews_data = r.json()
    comments = reviews_data['result']
    # next_page = reviews_data['next_url']
    prev_page = reviews_data['prev_url']
    return render_template('rating_1.html', name="Omnisend reviews", comments=comments, api=prev_page)


@app.route("/rating_2")
def rating_2():
    r = requests.get(
        'https://shopify-reviews-api.herokuapp.com/reviews_api/2_of_5_stars?limit=3000&offset=0')
    reviews_data = r.json()
    comments = reviews_data['result']
    # next_page = reviews_data['next_url']
    prev_page = reviews_data['prev_url']
    return render_template('rating_2.html', name="Omnisend reviews", comments=comments, api=prev_page)


@app.route("/rating_3")
def rating_3():
    r = requests.get(
        'https://shopify-reviews-api.herokuapp.com/reviews_api/3_of_5_stars?limit=3000&offset=0')
    reviews_data = r.json()
    comments = reviews_data['result']
    # next_page = reviews_data['next_url']
    prev_page = reviews_data['prev_url']
    return render_template('rating_3.html', name="Omnisend reviews", comments=comments, api=prev_page)


@app.route("/rating_4")
def rating_4():
    r = requests.get(
        'https://shopify-reviews-api.herokuapp.com/reviews_api/4_of_5_stars?limit=3000&offset=0')
    reviews_data = r.json()
    comments = reviews_data['result']
    # next_page = reviews_data['next_url']
    prev_page = reviews_data['prev_url']
    return render_template('rating_4.html', name="Omnisend reviews", comments=comments, api=prev_page)


@app.route("/rating_5")
def rating_5():
    r = requests.get(
        'https://shopify-reviews-api.herokuapp.com/reviews_api/5_of_5_stars?limit=3000&offset=0')
    reviews_data = r.json()
    comments = reviews_data['result']
    # next_page = reviews_data['next_url']
    prev_page = reviews_data['prev_url']
    return render_template('rating_5.html', name="Omnisend reviews", comments=comments, api=prev_page)


@app.route('/scrape', methods=['GET'])
def scrape():
    comments = shopify.scrape_comments()
    shopify.write_comments_to_db(comments)
    status = "Reviews scraped"

    r = requests.get(
        'https://shopify-reviews-api.herokuapp.com/reviews_api/5_of_5_stars?limit=3000&offset=0')
    reviews_data = r.json()
    comments = reviews_data['result']
    # next_page = reviews_data['next_url']
    prev_page = reviews_data['prev_url']
    return render_template('scraped.html', name="Omnisend reviews", comments=comments, api=prev_page, status=status)
