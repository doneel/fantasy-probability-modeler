"""Logic for loading data from csvs"""
import numpy as np
import pandas


def read_scores(file_path):
    """Load data into fully normalized numpy dataset"""
    return (pandas.DataFrame(np.genfromtxt(
            file_path,
            delimiter=',',
            dtype=[('team', np.str, 8), ('week', np.int), ('score', np.float)]))
        .set_index(['team', 'week']))


def read_schedule(file_path):
    """Load schedule into numpy array of games"""
    return pandas.DataFrame(
        np.genfromtxt(
            file_path,
            delimiter=',',
            dtype=[('t1', np.str, 8), ('t2', np.str, 8), ('week', np.int)]))

