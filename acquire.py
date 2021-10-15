import pandas as pd

def acquire_file():
    df = pd.read_csv(r'/Users/malachihale/codeup-data-science/End-to-End-Project/tracks.csv')

    return df