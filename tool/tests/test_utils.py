# test utils
import pandas
import numpy
from tool import utils


def test_read_csv_of_year():
    df = utils.read_csv_of_year(2022)
    assert type(df) == pandas.core.frame.DataFrame


def test_time_processing():
    df = utils.read_csv_of_year(2022)
    utils.time_processing(df)
    assert type(df['CRASH DATE'][0]) == pandas._libs.tslibs.timestamps.Timestamp
    assert type(df['CRASH HOUR'][0]) == numpy.int64