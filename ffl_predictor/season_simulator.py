""" Abstract class representing a simulation of a remaining season """
from abc import ABCMeta
from abc import abstractmethod
from ffl_predictor import SeasonStateException

class SeasonSimulator(metaclass=ABCMeta):
    """ Simulates remaining games in schedule for which there are no recorded scores """

    def __init__(self, season):
        self.season = season

    @abstractmethod
    def simulate(self, season):
        pass

    def has_unplayed_games(self):
        remaining_games = (self.__get_schedule_length_per_team()
                .subtract(self.__get_played_games_per_team()))
        if remaining_games.sum() < 1:
            raise SeasonSimulationException("There are no unplayed regular season games remaining in this season")

    def is_valid_season_for_simulation(self):
        played_games = self.__get_played_games_per_team()
        schedule_lengths = self.__get_schedule_length_per_team()

        if not (self.__get_schedule_length_per_team()
                .subtract(self.__get_played_games_per_team())
                .loc[lambda x: x < 0]
                .empty):
            raise SeasonStateException('Teams cannot have more scores than games on their schedule')

        if(len(played_games.unique()) != 1 or \
                len(schedule_lengths.unique()) != 1):
            raise SeasonStateException('All teams must have same schedule length')

    def __get_played_games_per_team(self):
        return (self.season.scores[['team', 'week']]
            .groupby('team', as_index=False)
            .size())

    def __get_schedule_length_per_team(self):
        return (self.season.schedule['t1']
                .append(self.season.schedule['t2'])
                .value_counts())


class SeasonSimulationException(Exception):
    """ Signifies an unrecoverable error during simulation """
    pass
