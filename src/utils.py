import numpy as np


def get_data():
    file_path = "data\wordlist.10000.txt"

    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        
        return np.array(words)