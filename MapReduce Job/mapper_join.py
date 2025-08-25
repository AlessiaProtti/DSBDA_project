#!/usr/bin/python3
"""mapper_join.py"""
import sys

for line in sys.stdin:
  line=line.strip()
  splits=line.split(",")

  #first dataset
  title = "-"
  authors = "-"
  avg_rating = "-"
  isbn13 = "-"
  num_pages = "-"
  ratings_count = "-"
  text_reviews_count = "-"
  publisher = "-"
  publication_date = "-"

  #second dataset
  counter = "-"

  if len(splits)==9:
    title = splits[0]
    authors = splits[1]
    avg_rating = splits[2]
    isbn13 = splits[3]
    num_pages = splits[4]
    ratings_count = splits[5]
    text_reviews_count = splits[6]
    publisher = splits[7]
    publication_date = splits[8]
  elif len(splits)==2:
      title = splits[0]
      counter = splits[1]
  else:
    continue

  print(title.lower().strip(), "\t", authors, "\t", avg_rating, "\t", isbn13, "\t", num_pages, "\t", ratings_count, "\t", text_reviews_count, "\t", publisher, "\t", publication_date, "\t", counter)
