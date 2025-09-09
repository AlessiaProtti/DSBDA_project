#!/usr/bin/python3
"""reducer_title_occurrences.py"""
import sys

cur_title = None
title = None
cur_count = 0

# Preprocessing line
for line in sys.stdin:
  line = line.strip()

  title, count = line.split("\t", 1)
  count = int(count)

  # We count the title occurrences
  if cur_title == title:
    cur_count += count
  else:
    if cur_title:
      print(cur_title, "\t", cur_count)

    cur_title = title
    cur_count = count

# Printing the last title
if cur_title:
  print(cur_title.strip(), ",", cur_count)