""" Data manipulation helpers """
import pandas

def mean_var_scores(raw_scores):
    """ Generate table with mean and variance scores for each team """
    scores_by_team = (raw_scores[['team', 'score']]
            .groupby(['team'], as_index=False))
    return pandas.merge(
        scores_by_team.mean().rename(columns={'score': 'mean'}),
        scores_by_team.var().rename(columns={'score': 'var'}))
