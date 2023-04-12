import secrets
import string
import csv


def read_data_from_csv(filename):
    with open(filename, mode='r') as csvdata:
        reader = csv.reader(csvdata)
        next(reader)
        for rows in reader:
            yield rows

def text_generator(length: int):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))