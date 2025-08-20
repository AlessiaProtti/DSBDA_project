#!/usr/bin/python3
"""mapper.py"""
import sys

for line in sys.stdin:
  line=line.strip()
  line=str(line).replace('\"','\'').replace('\\','')
  splits=line.split("', '")

  #first dataset
  book_id = "-"
  title = "-"
  authors = "-"
  isbn = "-"
  isbn13 = "-"
  language_code = "-"
  num_pages = "-"
  ratings_count = "-"
  ratings_average = "-"
  text_reviews_count = "-"
  publication_date = "-"
  publisher = "-"

  #second dataset
  book_format = "-"
  description = "-"
  genre = "-"
  image = "-"
  link = "-"

  if len(splits)==12:
    book_id = splits[0]
    title = splits[1]
    authors = splits[2]
    ratings_average = splits[3]
    isbn = splits[4]
    isbn13 = splits[5]
    language_code = splits[6]
    num_pages = splits[7]
    ratings_count = splits[8]
    text_reviews_count = splits[9]
    publication_date = splits[10]
    publisher = splits[11]
  elif len(splits)==13:
    authors= splits[0]
    book_format = splits[1]
    description = splits[2]
    genre = splits[3]
    image = splits[4]
    isbn = splits[5]
    isbn13 = splits[6]
    link = splits[7]
    num_pages = splits[8]
    ratings_average = splits[9]
    text_reviews_count = splits[10]
    title = splits[11]
    ratings_count = splits[12]
  else:
    continue

  print(isbn, "\t", book_id, "\t", language_code, "\t", publication_date, "\t", publisher, "\t", isbn13, "\t", title, "\t", authors, "\t", description, "\t", book_format, "\t", num_pages, "\t", genre, "\t", image, "\t", link, "\t", ratings_count, "\t", ratings_average, "\t", text_reviews_count)