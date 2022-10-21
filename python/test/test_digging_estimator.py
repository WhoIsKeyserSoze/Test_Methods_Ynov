import pytest

from src.digging_estimator import DiggingEstimator
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
