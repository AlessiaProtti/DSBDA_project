#!/usr/bin/python3
"""reducer.py"""
import sys
import string

last_isbn = None

# first dataset
cur_book_id = "-"
cur_title = "-"
cur_authors = "-"
cur_isbn = "-"
cur_isbn13 = "-"
cur_language_code = "-"
cur_num_pages = "-"
cur_ratings_count = "-"
cur_ratings_average = "-"
cur_text_reviews_count = "-"
cur_publication_date = "-"
cur_publisher = "-"

# second dataset
cur_book_format = "-"
cur_description = "-"
cur_genre = "-"
cur_image = "-"
cur_link = "-"

for line in sys.stdin:
  line = line.strip()

  isbn, book_id, language_code, publication_date, publisher, isbn13, title, authors, description, book_format, num_pages, genre, image, link, ratings_count, ratings_average, text_reviews_count= line.split("\t")

  if not last_isbn or isbn != last_isbn:
    last_isbn = isbn
    cur_book_id = book_id
    cur_title = title
    cur_authors = authors
    cur_isbn13 = isbn13
    cur_language_code = language_code
    cur_num_pages = num_pages
    cur_ratings_count = ratings_count
    cur_ratings_average = ratings_average
    cur_text_reviews_count = text_reviews_count
    cur_publication_date = publication_date
    cur_publisher = publisher
    cur_book_format = book_format
    cur_description = description
    cur_genre = genre
    cur_image = image
    cur_link = link

  elif isbn == last_isbn:
    print(isbn, cur_book_id, cur_language_code, cur_publication_date, cur_publisher, cur_isbn13, title, authors, description, book_format, num_pages, genre, image, link, cur_ratings_count, cur_ratings_average, cur_text_reviews_count)