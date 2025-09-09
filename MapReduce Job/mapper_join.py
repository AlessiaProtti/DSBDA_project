#!/usr/bin/python3
"""mapper_join.py"""
import sys

# Preprocessing and splitting each line
for line in sys.stdin:
  line=line.strip()
  splits=line.split(",")

  # First dataset to be joined
  title = "-"
  authors = "-"
  avg_rating = "-"
  num_pages = "-"
  ratings_count = "-"
  text_reviews_count = "-"
  publisher = "-"
  publication_date = "-"

  # Second dataset to be joined
  counter = "-"

  if len(splits)==8:
    title = splits[0]
    authors = splits[1]
    avg_rating = splits[2]
    num_pages = splits[3]
    ratings_count = splits[4]
    text_reviews_count = splits[5]
    publisher = splits[6]
    publication_date = splits[7]
  elif len(splits)==2:
      title = splits[0]
      counter = splits[1]
  else:
    continue

  print(title.lower().strip(), "\t", authors, "\t", avg_rating, "\t", num_pages, "\t", ratings_count, "\t", text_reviews_count, "\t", publisher, "\t", publication_date, "\t", counter)
