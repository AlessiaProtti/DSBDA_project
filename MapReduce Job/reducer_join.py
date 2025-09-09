#!/usr/bin/python3
"""reducer_join.py"""
import sys
import string

last_title = None

# second dataset
cur_counter = "-"

for line in sys.stdin:
  line = line.strip()

  title, authors, avg_rating, num_pages, ratings_count, text_reviews_count, publisher, publication_date, counter = line.split("\t")
  title=title.strip()

  if not last_title or title != last_title:
    last_title = title
    cur_counter = counter
  elif title == last_title:
    print(title, cur_counter, authors, avg_rating, num_pages, ratings_count, text_reviews_count, publisher, publication_date)
