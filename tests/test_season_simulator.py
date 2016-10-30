""" Unit test SeasonSimulator base class """
import numpy as np
import pandas as pd
from context import ffl_predictor
from ffl_predictor import Season
from ffl_predictor import SeasonSimulator
import pytest

@pytest.fixture(scope="session")
def sample_season():
    scores = pd.DataFrame(np.array([
        ('team1', 1, 1.0), ('team1', 2, 1.0),
        ('team2', 1, 0.0), ('team2', 2, 10.0),
        ('team3', 1, 1.0), ('team3', 2, 2.0),
        ('team4', 1, 3.0), ('team4', 2, 4.0)],
        dtype=[('team', np.str, 8), ('week', np.int), ('score', np.float)]))
    schedule = pd.DataFrame(np.array([
        ('team1', 'team2', 1),
        ('team3', 'team4', 1),
        ('team1', 'team3', 2),
        ('team2', 'team4', 2)],
        dtype=[('t1', np.str, 8), ('t2', np.str, 8), ('week', np.int)]))
    return Season(schedule, scores)

class DummySeasonSimulator(SeasonSimulator):
    """ Dummy implementation to allow instantiation and testing of class methods """

    def simulate(self, season):
        return season

def test_check_number_played_games_equal(sample_season):
    DummySeasonSimulator(sample_season).check_number_played_games_equal()
    assert(1 == 2)
