import numpy as np
import pandas as pd
from ffl_predictor import RegularSeasonSimulator
from ffl_predictor import mean_var_scores


class IndividualNormalSeasonSimulator(RegularSeasonSimulator):
    """ Treats team scores as independent static normal distributions """

    def __init__(self, season):
        super().__init__(season) #TODO: Figure out this syntax

    def simulate(self):
        distrubution_params = mean_var_scores(self.season.scores)
        print(self.season.scores)

        new_frame = self.season.scores[['week', 'score']]
        new_frame.index = self.season.scores['team']
        print(new_frame)
        return
        print(self.season.scores[['week', 'score']])
        print(pd.DataFrame(self.season.scores[['week', 'score']], index=self.season.scores['team'], columns=['week', 'score']))
        #TODO: Does append return a new array or same?

    def scores_remaining_per_team(self):
        """ Ok so to be fastest, I should just generate N std normals and then multiply / add them by the relevant team columns then what? Map these into a new dataframe and append ok smart"""
        """ Another way to look at this is that I could do the simulations in batch: Generate 100000 of these results at one time by just duplicating the dataframe 100000 times and doing the same process, then splitting it back up into the right size.
            That batch computation is probably only of limited use though. Not gonna worry about that optimization yet.
        """
        #self.season.scores.index = self.season.scores['team']
        #self.season.scores = self.season.scores[['week', 'score']]
        all_scheduled = (
            self.season.schedule[['t1', 'week']]
                .rename(columns={'t1': 'team'})
                .append(self.season.schedule[['t2', 'week']]
                            .rename(columns={'t2': 'team'}))
                .merge(self.season.scores, on=['team', 'week'], how='outer')
        )
        all_scheduled.index = pd.MultiIndex.from_arrays(
                [all_scheduled['team'], all_scheduled['week']])
        all_scheduled = all_scheduled['score']
        unplayed = all_scheduled.isnull()
        combined_data = (mean_var_scores(self.season.scores)
                         .join(all_scheduled[unplayed]))
        combined_data['score'] = (
                np.random.normal(size = unplayed.sum())
                * np.sqrt(combined_data['var'])
                + combined_data['mean'])
        combined_data.index = pd.MultiIndex.from_arrays(
            [combined_data['team'], combined_data['week']])
        combined_data = combined_data['score']
        print(all_scheduled[unplayed_2])
        print(combined_data)
        all_scheduled[unplayed_2] = combined_data
        print(all_scheduled)
        return all_scheduled
