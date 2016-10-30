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

    def is_valid_schedule(self):
        return self.check_number_played_games_equal()

    def check_number_played_games_equal(self):
        games_played = (self.season.scores[['team', 'week']]
            .groupby('team', as_index=False)
            .count())
        total_games = (self.season.schedule[['t1', 't2']]
            .groupby('t1', as_index=False)
            .union(
                self.season.schedule[['t1', 't2']]
                    .groupby('t2', as_index=False))
            .count())

