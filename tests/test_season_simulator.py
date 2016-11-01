""" Unit test RegularSeasonSimulator base class """
import numpy as np
import pandas as pd
from ffl_predictor import Season
from ffl_predictor import SeasonStateException
from ffl_predictor import RegularSeasonSimulator
from ffl_predictor import RegularSeasonSimulationException
import pytest


class DummyRegularSeasonSimulator(RegularSeasonSimulator):
    """ Dummy implementation to allow instantiation and testing of class methods """

    def simulate(self, season):
        return season


@pytest.fixture()
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

def test_valid_season_for_simulation_true(sample_season):
    DummyRegularSeasonSimulator(sample_season)

def test_valid_season_for_simulation_extra_score(sample_season):
    with pytest.raises(SeasonStateException):
        sample_season.scores = sample_season.scores.append(pd.DataFrame(np.array(
            [('team1', 3, 4.0)],
            dtype=[('team', np.str, 8), ('week', np.int), ('score', np.float)])))
        DummyRegularSeasonSimulator(sample_season)

def test_valid_season_for_simulation_duplicate_game(sample_season):
    with pytest.raises(SeasonStateException):
        sample_season.schedule = sample_season.schedule.append(pd.DataFrame(np.array([
            ('team1', 'team3', 2)],
            dtype=[('t1', np.str, 8), ('t2', np.str, 8), ('week', np.int)])))
        DummyRegularSeasonSimulator(sample_season)

def test_valid_season_for_simulation_too_many_scores(sample_season):
    with pytest.raises(SeasonStateException):
        sample_season.scores = sample_season.scores.append(pd.DataFrame(np.array(
            [('team1', 3, 4.0), ('team1', 4, 4.0)],
            dtype=[('team', np.str, 8), ('week', np.int), ('score', np.float)])))
        DummyRegularSeasonSimulator(sample_season)

def test_has_unplayed_games_true(sample_season):
    DummyRegularSeasonSimulator(sample_season)

def test_has_unplayed_games_false(sample_season):
    with pytest.raises(RegularSeasonSimulationException):
        sample_season.scores = sample_season.scores.append(pd.DataFrame(np.array([
            ('team1', 4, 4.0),
            ('team2', 4, 4.0),
            ('team3', 4, 4.0),
            ('team4', 3, 4.0)],
            dtype=[('team', np.str, 8), ('week', np.int), ('score', np.float)])))
        DummyRegularSeasonSimulator(sample_season)
