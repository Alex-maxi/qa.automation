import secrets
import string
import csv


def read_data_from_csv(pathtofile: str) -> str:
    """

    Args:
        pathtofile (str): Path to file

    Yields:
        str: Each row of file
    """
    with open(pathtofile, mode='r', encoding="ASCII") as csvdata:
        reader = csv.reader(csvdata)
        next(reader)
        for rows in reader:
            yield rows

def text_generator(length: int) -> str:
    """
        Function for genereting of unique text
    Args:
        length (int): Length of genereted string.

    Returns:
        str: String with letters and synbols of specified length.
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))
