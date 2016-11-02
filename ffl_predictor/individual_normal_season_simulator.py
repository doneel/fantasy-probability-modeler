from ffl_predictor import RegularSeasonSimulator
from ffl_predictor import mean_var_scores


class IndividualNormalSeasonSimulator(RegularSeasonSimulator):
    """ Treats team scores as independent static normal distributions """

    def __init__(self, season):
        super().__init__(season) #TODO: Figure out this syntax

    def simulate(self):
        distrubution_params = mean_var_scores(self.season.scores)
        print(distrubution_params)
        #TODO: Does append return a new array or same?
