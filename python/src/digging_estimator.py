import math
from enum import Enum


class WORKER(Enum):
    MINERS = 1
    HEALERS = 2
    SMITHIES = 3
    LIGHTERS = 4
    INN_KEEPERS = 5
    GUARDS = 6
    GUARD_MANAGERS = 7
    WASHERS = 8


class TunnelTooLongForDelayException(Exception):
    pass


class InvalidFormatException(Exception):
    pass


class Team:
    def __init__(self):
        self.miners = 0
        self.healers = 0
        self.smithies = 0
        self.lighters = 0
        self.inn_keepers = 0
        self.guards = 0
        self.guard_managers = 0
        self.washers = 0

    def get_nb_worker(self):
        return self.miners + self.healers + self.smithies + self.lighters + self.inn_keepers + self.guards + self.guard_managers + self.washers

    def add_worker(self, worker_type, nb_worker_to_add=1):

        if worker_type == WORKER.MINERS:
            self.miners += nb_worker_to_add
        elif worker_type == WORKER.HEALERS:
            self.healers += nb_worker_to_add
        elif worker_type == WORKER.SMITHIES:
            self.smithies += nb_worker_to_add
        elif worker_type == WORKER.LIGHTERS:
            self.lighters += nb_worker_to_add
        elif worker_type == WORKER.INN_KEEPERS:
            self.inn_keepers += nb_worker_to_add
        elif worker_type == WORKER.GUARDS:
            self.guards += nb_worker_to_add
        elif worker_type == WORKER.GUARD_MANAGERS:
            self.guard_managers += nb_worker_to_add
        elif worker_type == WORKER.WASHERS:
            self.washers += nb_worker_to_add
        else:
            raise Exception("Not a valid worker type")


class TeamComposition:
    def __init__(self):
        self.day_team: Team = Team()
        self.night_team: Team = Team()
        self.total = 0


class DiggingEstimator:
    def tunnel(self, length, days, rock_type):
        dig_per_rotation = self.get(rock_type)
        max_dig_per_rotation = dig_per_rotation[len(dig_per_rotation) - 1]
        max_dig_per_day = 2 * max_dig_per_rotation

        if math.floor(length) != length or math.floor(days) != days or length < 0 or days < 0:
            raise InvalidFormatException()
        if math.floor(length / days) > max_dig_per_day:
            raise TunnelTooLongForDelayException()

        composition = TeamComposition()

        # Miners
        for i in range(0, len(dig_per_rotation) - 1):
            if dig_per_rotation[i] < math.floor(length / days):
                composition.day_team.miners += 1

        if math.floor(length / days) > max_dig_per_rotation:
            for i in range(0, len(dig_per_rotation) - 1):
                if dig_per_rotation[i] + max_dig_per_rotation < math.floor(length / days):
                    composition.night_team.miners += 1

        DAY_TEAM = composition.day_team
        NIGHT_TEAM = composition.night_team

        if DAY_TEAM.miners > 0:
            DAY_TEAM.add_worker(WORKER.HEALERS)
            DAY_TEAM.add_worker(WORKER.SMITHIES, 2)

            nb_inn_keepers_to_add = math.ceil((DAY_TEAM.miners + DAY_TEAM.healers + DAY_TEAM.smithies) / 4.0) * 4
            DAY_TEAM.add_worker(WORKER.INN_KEEPERS, nb_inn_keepers_to_add)

            nb_inn_washers_to_add = math.ceil((DAY_TEAM.miners + DAY_TEAM.healers + DAY_TEAM.smithies +
                                               DAY_TEAM.inn_keepers) / 10.0)
            DAY_TEAM.add_worker(WORKER.WASHERS, nb_inn_washers_to_add)

        if NIGHT_TEAM.miners > 0:
            NIGHT_TEAM.add_worker(WORKER.HEALERS)
            NIGHT_TEAM.add_worker(WORKER.SMITHIES, 2)
            NIGHT_TEAM.add_worker(WORKER.LIGHTERS, NIGHT_TEAM.miners + 1)

            nb_inn_washers_to_add_for_night_team = math.ceil(
                (NIGHT_TEAM.miners + NIGHT_TEAM.healers + NIGHT_TEAM.smithies +
                 NIGHT_TEAM.lighters) / 4.0) * 4
            NIGHT_TEAM.add_worker(WORKER.INN_KEEPERS, nb_inn_washers_to_add_for_night_team)

        while True:
            old_washers = NIGHT_TEAM.washers
            old_guards = NIGHT_TEAM.guards
            old_chief_guard = NIGHT_TEAM.guard_managers

            NIGHT_TEAM.washers = math.ceil((
                                                   NIGHT_TEAM.miners + NIGHT_TEAM.healers + NIGHT_TEAM.smithies +
                                                   NIGHT_TEAM.inn_keepers + NIGHT_TEAM.lighters + NIGHT_TEAM.guards +
                                                   NIGHT_TEAM.guard_managers) / 10.0)
            NIGHT_TEAM.guards = math.ceil((
                                                  NIGHT_TEAM.healers + NIGHT_TEAM.miners + NIGHT_TEAM.smithies +
                                                  NIGHT_TEAM.lighters + NIGHT_TEAM.washers) / 3.0)

            NIGHT_TEAM.guard_managers = math.ceil(NIGHT_TEAM.guards / 3.0)

            if old_washers == NIGHT_TEAM.washers and old_guards == NIGHT_TEAM.guards and old_chief_guard == NIGHT_TEAM.guard_managers:
                break

        composition.total = DAY_TEAM.get_nb_worker() + NIGHT_TEAM.get_nb_worker()

        return composition

    def get(self, rock_type):
        # for example for granite it returns [0, 3, 5.5, 7]
        # if you put 0 dwarf, you dig 0m / d / team
        # if you put 1 dwarf, you dig 3m / d / team
        # 2 dwarves = 5.5 m / d / team
        # so a day team on 2 miners and a night team of 1 miner dig 8.5 m / d
        url = "dtp://research.vin.co/digging-rate/" + rock_type
        print("Trying to fetch" + url)
        raise Exception("Does not work in test mode")
