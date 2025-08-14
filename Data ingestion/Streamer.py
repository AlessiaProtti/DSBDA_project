#!/usr/bin/env python

import socket
import time
import sys
import csv
import random
import pickle
import json

API_dataset_csv_path = "../Datasets/goodreads_API_dataset.csv"
scraped_dataset_csv_path = "../Datasets/goodreads_scraped_dataset.csv"


serialized_shuffled_dataset_path = '/home/ubuntu/DATASET/shuffled_dataset.json'

## here i collect all the paths

dataset_paths = [API_dataset_csv_path, scraped_dataset_csv_path]

# this function is responsible to write the dataset on the socket line by line so that spark
# reads it on the other end.
# the line is a touple from a randoom table

def sendData(connection, dataset):

    print("Start sending data")
    count = 0

    # Open file
    with open(dataset) as file_obj:
        # Create reader object by passing the file
        # object to reader method

        heading=next(file_obj)

        reader_obj = csv.reader(file_obj)

        # Iterate over each row in the csv
        # file using reader object
        for line in reader_obj:
            print(line)

            try:

                line_string = f'{str(line)}\n'
                byte_message = line_string.encode('utf-8')
                print(f'Debug byte_message {byte_message}')
                connection.sendall(byte_message)
                time.sleep(random.uniform(0, 0.5))  # Aggiungi un delay per non sovraccaricare il ricevitore
                count += 1
                print("Sent:", line_string)
            except Exception as e:
                print("Error sending data:", e)
                break

for path in dataset_paths:
    host = "localhost"
    port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("Server is listening on", port)

    try:
        connection, addr = s.accept()
        print("Connected by", addr)
        sendData(connection, s, path)
    except Exception as e:
        print("Connection error:", e)
    finally:
        connection.close()