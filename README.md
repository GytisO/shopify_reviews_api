# shopify_reviews_api
app built on python with flask to run locally: FLASK_APP=app.py flask run to run only scraper for reviews: python3 scraper.py

Scraping might take a while, it depends on number of reviews. Scraping speed is between 2-4 secs/page.

to view API: /reviews_api/1_of_5_stars?limit=10&offset=0 or /reviews_api?limit=10&offset=0 where: 1_of_5_stars is rating variable. 1 can be changed from 1 to 5. or removed to view all reviews.
