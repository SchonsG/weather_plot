import datetime
from unittest.mock import MagicMock

from app import App
from urban_climate_csv import DataSource


def test_read():
    app = App(data_source=DataSource(), plot=MagicMock())

    for key, value in app.read(file_name='./london.csv').items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value
