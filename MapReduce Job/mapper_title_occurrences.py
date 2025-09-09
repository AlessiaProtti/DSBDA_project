#!/usr/bin/python3
"""mapper_title_occurrences.py"""
import sys

# Preprocessing and splitting each line
for line in sys.stdin:
  line=line.strip()
  splits=line.split(",")

  title = "-"

  # We only keep the title in order to count its occurrences
  if len(splits)==8:
    title = splits[0]
  else:
    continue

  print(title.lower(), "\t", 1)