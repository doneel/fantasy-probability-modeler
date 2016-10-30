""" Unit tests for individual file reading methods """
import numpy as np
import pandas as pd
from context import ffl_predictor
from helpers import assert_frames_equal
import pytest

@pytest.fixture()
def scores_file_fixture(tmpdir):
    scores_file = tmpdir.join("fake_scores.csv")
    scores_file.write("""
            team1, 1, 1.0
            team1, 2, 1.0
            team2, 1, 0.0
            team2, 2, 10.0
            team3, 1, 1.0
            team3, 1, 2.0
            team3, 1, 3.0
            team3, 1, 4.0""")
    return scores_file

def test_read_scores(scores_file_fixture):
    expected = pd.DataFrame(np.array([
        ('team1', 1, 1.0), ('team1', 2, 1.0),
        ('team2', 1, 0.0), ('team2', 2, 10.0),
        ('team3', 1, 1.0), ('team3', 1, 2.0), ('team3', 1, 3.0), ('team3', 1, 4.0)],
        dtype=[('team', np.str, 8), ('week', np.int), ('score', np.float)]))
    assert_frames_equal(ffl_predictor.read_scores(scores_file_fixture.strpath), expected)

@pytest.fixture()
def schedule_file_fixture(tmpdir):
    schedule_file = tmpdir.join("fake_schedule.csv")
    schedule_file.write("""
                       do,rj, 1
                       rt,js, 1
                       km,sh, 1
                       va,es, 1
                       rt,do, 2
                       rj,js, 2
                       va,km, 2
                       sh,es, 2
                       do,js, 3
                       rj,rt, 3
                       km,es, 3
                       sh,va, 3
                       km,do, 4
                       va,rt, 4
                       sh,rj, 4
                       es,js, 4""")
    return schedule_file

def test_read_schedule(schedule_file_fixture):
    expected = pd.DataFrame(np.array([
        ('do', 'rj', 1),
        ('rt', 'js', 1),
        ('km', 'sh', 1),
        ('va', 'es', 1),
        ('rt', 'do', 2),
        ('rj', 'js', 2),
        ('va', 'km', 2),
        ('sh', 'es', 2),
        ('do', 'js', 3),
        ('rj', 'rt', 3),
        ('km', 'es', 3),
        ('sh', 'va', 3),
        ('km', 'do', 4),
        ('va', 'rt', 4),
        ('sh', 'rj', 4),
        ('es', 'js', 4)],
        dtype=[('t1', np.str, 8), ('t2', np.str, 8), ('week', np.int)]))
    assert_frames_equal(ffl_predictor.read_schedule(schedule_file_fixture.strpath), expected, use_close=True)
