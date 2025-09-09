#!/usr/bin/python3
"""mapper_title_occurrences.py"""
import sys

for line in sys.stdin:
  line=line.strip()
  splits=line.split(",")

  #first dataset
  title = "-"

  if len(splits)==8:
    title = splits[0]
  else:
    continue

  print(title.lower(), "\t", 1)