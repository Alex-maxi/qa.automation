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
