import pytest

from src.digging_estimator import DiggingEstimator, TunnelTooLongForDelayException, InvalidFormatException
from unittest.mock import MagicMock


def test_returns_as_doctor_Pockosky_says():
  estimator = DiggingEstimator()

  estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

  result = estimator.create_team(28, 2, "granite")

  assert result.total == 48

# ---------------------- Day team --------------------
def test_returns_number_of_each_dwarf_dayteam_miners():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.day_team.miners == 3
def test_returns_number_of_each_dwarf_dayteam_healers():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.day_team.healers == 1
def test_returns_number_of_each_dwarf_dayteam_smithies():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.day_team.smithies == 2
def test_returns_number_of_each_dwarf_dayteam_lighters():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.day_team.lighters == 0
def test_returns_number_of_each_dwarf_dayteam_inn_keepers():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.day_team.inn_keepers == 8
def test_returns_number_of_each_dwarf_dayteam_guards():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.day_team.guards == 0
def test_returns_number_of_each_dwarf_dayteam_guard_managers():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.day_team.guard_managers == 0

def test_returns_number_of_each_dwarf_dayteam_protectors():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.day_team.protectors == 0

# ---------------------- Night team --------------------
def test_returns_number_of_each_dwarf_nightteam_miners():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.night_team.miners == 3
def test_returns_number_of_each_dwarf_nightteam_healers():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.night_team.healers == 1
def test_returns_number_of_each_dwarf_nightteam_smithies():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.night_team.smithies == 2
def test_returns_number_of_each_dwarf_nightteam_lighters():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.night_team.lighters == 4
def test_returns_number_of_each_dwarf_nightteam_inn_keepers():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.night_team.inn_keepers == 12
def test_returns_number_of_each_dwarf_nightteam_guards():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.night_team.guards == 5
def test_returns_number_of_each_dwarf_nightteam_guard_managers():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.night_team.guard_managers == 2

def test_returns_number_of_each_dwarf_nightteam_protectors():
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(28, 2, "granite")

    assert result.night_team.protectors == 0

#----------------- Exception tests ------------------
def test_returns_0_for_0_meters_long_mountain() :
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    result = estimator.create_team(0, 1, "granite")

    assert result.total == 0
def test_returns_error_for_0_days() :
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(ZeroDivisionError):
        estimator.create_team(0, 0, "granite")
def test_returns_error_for_TunnelTooLongForDelayException() :
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(TunnelTooLongForDelayException):
        estimator.create_team(1000, 1, "granite")
def test_returns_error_for_InvalidFormatException_none_int_value_length() :
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(InvalidFormatException):
        estimator.create_team(5.5, 1, "granite")
def test_returns_error_for_InvalidFormatException_none_int_value_days() :
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(InvalidFormatException):
        estimator.create_team(5, 1.2, "granite")
def test_returns_error_for_InvalidFormatException_negative_length() :
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(InvalidFormatException):
        estimator.create_team(-5, 1, "granite")

def test_returns_error_for_InvalidFormatException_negative_days() :
    estimator = DiggingEstimator()

    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])

    with pytest.raises(InvalidFormatException):
        estimator.create_team(5, -1, "granite")

def test_return_error_when_rock_type_api_not_mokked() :
    estimator = DiggingEstimator()
    with pytest.raises(Exception):
        estimator.create_team(28, 2, "granite")

def test_return_error_when_goblin_api_not_mokked() :
    estimator = DiggingEstimator()
    estimator.ask_api_for_dwarfs_mining_distance_per_rock_type = MagicMock(return_value=[0, 3, 5.5, 7])
    with pytest.raises(Exception):
        estimator.create_team(28, 2, "granite", "moria's mine")

        