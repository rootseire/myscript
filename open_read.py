import os
import csv
import random
import string

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    print file_path
    return file_path

path = get_file_path('choices.csv')


def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print row[1], row[1]


read_csv(path)
