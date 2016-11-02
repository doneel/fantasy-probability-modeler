class Season:

    def __init__(self, schedule, scores):
        self.schedule = schedule
        self.scores = scores

class SeasonStateException(Exception):
    """ Used to signify a season is in an invalid state """
    pass
