# shopify reviews api
app built on python3 with flask. 
To run locally: FLASK_APP=app.py flask run 
To run only scraper for reviews: python3 scraper.py
  all scraped reviews are stored in mongodb or csv file. To view them from database you should visit working app url (watch below)
  
Scraping might take a while, it depends on number of reviews. Scraping speed is between 1-2 secs/page.

to view API: /reviews_api/1_of_5_stars?limit=10&offset=0 where: 1_of_5_stars is rating variable. 1 can be changed from 1 to 5. 
Or removed to view all reviews: /reviews_api?limit=10&offset=0

working app: https://shopify-reviews-api.herokuapp.com
