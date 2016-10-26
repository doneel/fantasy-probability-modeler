""" Unit tests for Season class """
import numpy as np
import pandas as pd
from context import ffl_predictor
from ffl_predictor import Season
from helpers import assert_frames_equal

def test_season():
    """ Ensures the Season class correctly returns its inputs """
    schedule = pd.DataFrame(np.array([
        ('team1', 'team2', 1), ('team3', 'team4', 1),
        ('team2', 'team3', 2), ('team1', 'team4', 2),
        ('team1', 'team3', 3), ('team2', 'team4', 3)],
        dtype=[('home_team', np.str, 8), ('away_team', np.str, 8), ('week', np.int)]))

    scores = pd.DataFrame(np.array([
        ('team1', 95.1, 1), ('team2', 115.0, 1),
        ('team2', 90.3, 2), ('team1', 102.7, 2),
        ('team1', 95.8, 3), ('team2', 82.3, 3)],
        dtype=[('home_team', np.str, 8), ('score', np.float), ('week', np.int)]))

    test_season = Season(schedule, scores)
    assert_frames_equal(test_season.schedule, schedule, use_close = False)
    assert_frames_equal(test_season.scores, scores, use_close = False)
