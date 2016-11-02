""" Abstract class representing a simulation of a remaining season """
from abc import ABCMeta
from abc import abstractmethod
from ffl_predictor import SeasonStateException

class RegularSeasonSimulator(metaclass=ABCMeta):
    """ Simulates remaining games in schedule for which there are no recorded scores """

    def __init__(self, season):
        RegularSeasonSimulator._is_valid_season_for_simulation(season)
        RegularSeasonSimulator._has_unplayed_games(season)
        self.season = season

    @abstractmethod
    def simulate(self):
        pass

    @staticmethod
    def _is_valid_season_for_simulation(season):
        played_games = RegularSeasonSimulator._get_played_games_per_team(season.scores)
        schedule_lengths = RegularSeasonSimulator._get_schedule_length_per_team(season.schedule)

        if not (schedule_lengths
                .subtract(played_games)
                .loc[lambda x: x < 0]
                .empty):
            raise SeasonStateException('Teams cannot have more scores than games on their schedule')

        if(len(played_games.unique()) != 1 or \
           len(schedule_lengths.unique()) != 1):
            raise SeasonStateException('All teams must have same schedule length')

    @staticmethod
    def _has_unplayed_games(season):
        remaining_games = (RegularSeasonSimulator._get_schedule_length_per_team(season.schedule)
                .subtract(RegularSeasonSimulator._get_played_games_per_team(season.scores)))
        if remaining_games.sum() < 1:
            raise RegularSeasonSimulationException("There are no unplayed regular season games remaining in this season")

    @staticmethod
    def _get_played_games_per_team(scores):
        return (scores[['team', 'week']]
            .groupby('team', as_index=False)
            .size())

    @staticmethod
    def _get_schedule_length_per_team(schedule):
        return (schedule['t1']
                .append(schedule['t2'])
                .value_counts())


class RegularSeasonSimulationException(Exception):
    """ Signifies an unrecoverable error during simulation """
    pass
