import requests
import pymongo
from bs4 import BeautifulSoup
from time import sleep
from random import randint, choice

BASE_URL = "https://apps.shopify.com"


def scrape_comments():

    all_comments = []
    url = "/omnisend/reviews?page=1"
    while url:
        response = requests.get(f"{BASE_URL}{url}")
        print(f"Gathering data from {BASE_URL}{url}")
        soup = BeautifulSoup(response.text, "html.parser")
        comments = soup.find_all(class_="review-listing")

        for comment in comments:
            all_comments.append({
                "comment": comment.find(class_="truncate-content-copy").get_text().strip('\n'),
                "rating": comment.find(class_="ui-star-rating").get_text().strip('\n').strip(' '),
                "author": comment.find(class_="review-listing-header__text").get_text().strip('\n').strip(' ').rstrip('\n'),
            })

        next_btn = soup.find(class_="search-pagination__next-page-text")
        next_btn_dis = soup.find(
            class_="search-pagination__next-page-text disabled")
        url = next_btn["href"] if next_btn != next_btn_dis else None
        sleep(randint(1, 2))

    print("DONE")
    return all_comments


def write_comments_to_db(comments):

    client = pymongo.MongoClient(
        "mongodb+srv://new-user:newuser1234@golangcluster-hqxdo.mongodb.net/test?retryWrites=true")
    db = client.omnisend
    db.reviews.drop()
    posts = db.reviews
    posts.insert_many(comments)
