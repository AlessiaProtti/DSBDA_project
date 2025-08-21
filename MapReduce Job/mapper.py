#!/usr/bin/python3
"""mapper.py"""
import sys

for line in sys.stdin:
  line=line.strip()
  line=str(line).replace('\"','\'').replace('\\','')
  splits=line.split("', '")

  #first dataset
  title = "-"

  if len(splits)==12:
    title = splits[1]
  else:
    continue

  print(title.lower(), "\t", 1)