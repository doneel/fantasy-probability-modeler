import numpy as np
import pandas as pd
from ffl_predictor import RegularSeasonSimulator
from ffl_predictor import mean_var_scores


class IndividualNormalSeasonSimulator(RegularSeasonSimulator):
    """ Treats team scores as independent static normal distributions """

    def __init__(self, season):
        super().__init__(season)

    def simulate(self):
        all_scheduled = (
            self.season.schedule[['t1', 'week']]
                .rename(columns={'t1': 'team'})
                .append(self.season.schedule[['t2', 'week']]
                            .rename(columns={'t2': 'team'}))
                .set_index(['team', 'week'])
                .join(self.season.scores, how='outer')
        )
        unplayed = all_scheduled['score'].isnull()
        combined_data = (mean_var_scores(self.season.scores)
                         .join(all_scheduled[unplayed]))
        all_scheduled['score'][unplayed] = (
                np.random.normal(size=unplayed.sum())
                * np.sqrt(combined_data['var'])
                + combined_data['mean'])
        return all_scheduled
