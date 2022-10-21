import pytest

from src.digging_estimator import DiggingEstimator, TunnelTooLongForDelayException, InvalidFormatException
from unittest.mock import MagicMock


def test_returns_as_doctor_Pockosky_says():
  estimator = DiggingEstimator()

  estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

  result = estimator.tunnel(28, 2, "granite")

  assert result.total == 48

# ---------------------- Day team --------------------
def test_returns_number_of_each_dwarf_dayteam_miners():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.day_team.miners == 3
def test_returns_number_of_each_dwarf_dayteam_healers():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.day_team.healers == 1
def test_returns_number_of_each_dwarf_dayteam_smithies():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.day_team.smithies == 2
def test_returns_number_of_each_dwarf_dayteam_lighters():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.day_team.lighters == 0
def test_returns_number_of_each_dwarf_dayteam_inn_keepers():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.day_team.inn_keepers == 8
def test_returns_number_of_each_dwarf_dayteam_guards():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.day_team.guards == 0
def test_returns_number_of_each_dwarf_dayteam_guard_managers():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.day_team.guard_managers == 0

# ---------------------- Night team --------------------
def test_returns_number_of_each_dwarf_nightteam_miners():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.night_team.miners == 3
def test_returns_number_of_each_dwarf_nightteam_healers():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.night_team.healers == 1
def test_returns_number_of_each_dwarf_nightteam_smithies():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.night_team.smithies == 2
def test_returns_number_of_each_dwarf_nightteam_lighters():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.night_team.lighters == 4
def test_returns_number_of_each_dwarf_nightteam_inn_keepers():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.night_team.inn_keepers == 12
def test_returns_number_of_each_dwarf_nightteam_guards():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.night_team.guards == 5
def test_returns_number_of_each_dwarf_nightteam_guard_managers():
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.tunnel(28, 2, "granite")

    assert result.night_team.guard_managers == 2

#----------------- Exception tests ------------------
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
def test_returns_error_for_InvalidFormatException_none_int_value_length() :
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(InvalidFormatException):
        estimator.tunnel(5.5, 1, "granite")
def test_returns_error_for_InvalidFormatException_none_int_value_days() :
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(InvalidFormatException):
        estimator.tunnel(5, 1.2, "granite")
def test_returns_error_for_InvalidFormatException_negative_length() :
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(InvalidFormatException):
        estimator.tunnel(-5, 1, "granite")

def test_returns_error_for_InvalidFormatException_negative_days() :
    estimator = DiggingEstimator()

    estimator.get = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(InvalidFormatException):
        estimator.tunnel(5, -1, "granite")
