""" Unit tests for team_summary helpers """
import numpy as np
import pandas as pd
from context import ffl_predictor
from helpers import assert_frames_equal



def test_mean_var_scores():
    """ Test accurate summarizing of mean and variance of scores for individual teams """
    raw_data = pd.DataFrame(np.array([
        ('team1', 1, 1.0), ('team1', 2, 1.0),
        ('team2', 1, 0.0), ('team2', 2, 10.0),
        ('team3', 1, 1.0), ('team3', 1, 2.0), ('team3', 1, 3.0), ('team3', 1, 4.0)],
        dtype=[('team', np.str, 8), ('week', np.int), ('score', np.float)]))

    expected = pd.DataFrame({
        'team1': [1, 0],
        'team2': [5.0, 50.0],
        'team3': [2.5, 5/3]
      }) \
     .transpose() \
     .reset_index(level=0) \
     .rename(columns={'index': 'team', 0: 'mean', 1: 'var'})

    actual = ffl_predictor.mean_var_scores(raw_data)
    assert_frames_equal(expected, actual, use_close=True)
