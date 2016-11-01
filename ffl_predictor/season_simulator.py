""" Abstract class representing a simulation of a remaining season """
from abc import ABCMeta
from abc import abstractmethod

class SeasonSimulator(metaclass=ABCMeta):
    """ Simulates remaining games in schedule for which there are no recorded scores """

    def __init__(self, season):
        self.season = season

    @abstractmethod
    def simulate(self, season):
        pass

    def is_valid_season_for_simulation(self):
        return self.__check_played_games_equal() and \
                  self.__check_equal_schedule_length()

    def __check_played_games_equal(self):
        unique_games_played = (self.season.scores[['team', 'week']]
            .groupby('team', as_index=False)
            .count()
            ['week']
            .unique())
        return len(unique_games_played) == 1

    def __check_equal_schedule_length(self):
        unique_schedule_lengths = (
                self.season.schedule['t1']
                .append(self.season.schedule['t2'])
                .value_counts()
                .unique())
        return len(unique_schedule_lengths) == 1
