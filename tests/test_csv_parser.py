""" Unit tests for individual file reading methods """
import numpy as np
import pandas as pd
from context import ffl_predictor
from helpers import assert_frames_equal
import pytest


@pytest.fixture()
def scores_file_fixture(tmpdir):
    p = tmpdir.mkdir("sub").join("fake_scores.csv")
    p.write("""
            team1, 1, 1.0
            team1, 2, 1.0
            team2, 1, 0.0
            team2, 2, 10.0
            team3, 1, 1.0
            team3, 1, 2.0
            team3, 1, 3.0
            team3, 1, 4.0""")
    return p

def test_read_scores(scores_file_fixture):
    expected = pd.DataFrame(np.array([
        ('team1', 1, 1.0), ('team1', 2, 1.0),
        ('team2', 1, 0.0), ('team2', 2, 10.0),
        ('team3', 1, 1.0), ('team3', 1, 2.0), ('team3', 1, 3.0), ('team3', 1, 4.0)],
        dtype=[('team', np.str, 8), ('week', np.int), ('score', np.float)]))
    assert_frames_equal(expected, ffl_predictor.read_scores(scores_file_fixture.strpath))

