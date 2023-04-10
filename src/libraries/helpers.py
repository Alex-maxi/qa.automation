import random
import string
from src.config.config import config
import csv


def read_data_from_csv(filename):
    datalist = []
    with open(filename, mode='r') as csvdata:
        reader = csv.reader(csvdata)
        next(reader)
        for rows in reader:
            datalist.append(rows)
            yield rows


def text_generator(len: int):
    letters = string.ascii_letters
    return (''.join(random.choice(letters) for i in range(len)))
