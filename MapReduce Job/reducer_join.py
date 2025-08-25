#!/usr/bin/python3
"""reducer_join.py"""
import sys
import string

last_title = None

# first dataset
cur_title = "-"
cur_authors = "-"
cur_avg_rating = "-"
cur_isbn13 = "-"
cur_num_pages = "-"
cur_ratings_count = "-"
cur_text_reviews_count = "-"
cur_publisher = "-"
cur_publication_date = "-"

# second dataset
cur_counter = "-"

for line in sys.stdin:
  line = line.strip()

  title, authors, avg_rating, isbn13, num_pages, ratings_count, text_reviews_count, publisher, publication_date, counter = line.split("\t")
  title=title.strip()

  if not last_title or title != last_title:
    last_title = title
    cur_counter = counter
    cur_authors = authors
    cur_avg_rating = avg_rating
    cur_isbn13 = isbn13
    cur_num_pages = num_pages
    cur_ratings_count = ratings_count
    cur_text_reviews_count = text_reviews_count
    cur_publisher = publisher
    cur_publication_date = publication_date
  elif title == last_title:
    print(title, cur_counter, authors, avg_rating, isbn13, num_pages, ratings_count, text_reviews_count, publisher, publication_date)
