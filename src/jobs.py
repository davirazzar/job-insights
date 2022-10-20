from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        result_list = []
        for row in reader:
            result_list.append(row)
    return result_list
