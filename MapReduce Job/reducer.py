#!/usr/bin/python3
"""reducer.py"""
import sys
import string

# first dataset
cur_title = None
title = None
cur_count = 0

for line in sys.stdin:
  line = line.strip()

  title, count = line.split("\t", 1)
  count=int(count)

  if cur_title == title:
    cur_count += count
  else:
    if cur_title:
      print(cur_title, "\t", cur_count)

    cur_title = title
    cur_count = count

if cur_title:
  print(cur_title, "\t", cur_count)