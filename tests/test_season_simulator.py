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
        ('team2', 'team4', 2),
        ('team1', 'team4', 3),
        ('team2', 'team3', 3)],
        dtype=[('t1', np.str, 8), ('t2', np.str, 8), ('week', np.int)]))
    return Season(schedule, scores)

class DummySeasonSimulator(SeasonSimulator):
    """ Dummy implementation to allow instantiation and testing of class methods """

    def simulate(self, season):
        return season

def test_valid_season_for_simulation_true(sample_season):
    assert DummySeasonSimulator(sample_season).is_valid_season_for_simulation()

def test_valid_season_for_simulation_false(sample_season):
    invalid_scores = sample_season.scores.append(pd.DataFrame(np.array(
        [('team1', 3, 4.0)],
        dtype=[('team', np.str, 8), ('week', np.int), ('score', np.float)])))
    invalid_season = Season(sample_season.schedule, invalid_scores)
    assert not DummySeasonSimulator(invalid_season).is_valid_season_for_simulation()
