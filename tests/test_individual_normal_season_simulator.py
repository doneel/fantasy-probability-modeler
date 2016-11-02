""" Unit test IndividualNormalSeasonSimulator """
from ffl_predictor import IndividualNormalSeasonSimulator
from test_season_simulator import sample_season

def test_simulate(sample_season):
    IndividualNormalSeasonSimulator(sample_season).simulate()
