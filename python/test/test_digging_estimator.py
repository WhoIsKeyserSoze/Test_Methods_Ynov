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

    assert estimator.tunnel(0, 0, "granite") == 0