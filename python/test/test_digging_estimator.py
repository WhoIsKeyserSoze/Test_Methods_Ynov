import pytest

from src.digging_estimator import DiggingEstimator, TunnelTooLongForDelayException, InvalidFormatException
from unittest.mock import MagicMock


def test_returns_as_doctor_Pockosky_says():
  estimator = DiggingEstimator()

  estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

  result = estimator.tunnel(28, 2, "granite")

  assert result.total == 48


def test_returns_0_for_0_meters_long_mountain() :
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(0, 1, "granite")

    assert result.total == 0

def test_returns_error_for_0_days() :
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(ZeroDivisionError):
        estimator.tunnel(0, 0, "granite")

def test_returns_error_for_TunnelTooLongForDelayException() :
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(TunnelTooLongForDelayException):
        estimator.tunnel(1000, 1, "granite")

def test_returns_error_for_InvalidFormatException() :
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(InvalidFormatException):
        estimator.tunnel(5.5, 1.2, "granite")

