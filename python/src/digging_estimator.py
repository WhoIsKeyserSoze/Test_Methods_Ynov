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
    PROTECTORS = 9


class TunnelTooLongForDelayException(Exception):
    pass


class InvalidFormatException(Exception):
    pass

class ApiErrorException(Exception):
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
        self.protectors = 0

    def get_nb_worker(self):
        return self.miners \
               + self.healers \
               + self.smithies \
               + self.lighters \
               + self.inn_keepers \
               + self.guards \
               + self.guard_managers \
               + self.washers \
               + self.protectors

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
        elif worker_type == WORKER.PROTECTORS:
            self.protectors += nb_worker_to_add
        else:
            raise Exception("Not a valid worker type")

    def calculate_nb_washers_guard_and_guard_managers(self, nb_washers, nb_guards, nb_guard_managers):
        new_nb_washers = math.ceil(
            (self.miners + self.healers + self.smithies + self.inn_keepers + self.lighters + nb_guards +
             nb_guard_managers + self.protectors) / 10)
        new_nb_guards = math.ceil((self.miners + self.healers + self.smithies + self.lighters + new_nb_washers) / 3)
        new_nb_guard_managers = math.ceil(new_nb_guards / 3)

        if nb_washers == new_nb_washers \
                and nb_guards == new_nb_guards \
                and nb_guard_managers == new_nb_guard_managers:
            return new_nb_washers, new_nb_guards, new_nb_guard_managers
        else:
            return self.calculate_nb_washers_guard_and_guard_managers(new_nb_washers, new_nb_guards,
                                                                      new_nb_guard_managers)


class TeamComposition:
    def __init__(self):
        self.day_team: Team = Team()
        self.night_team: Team = Team()
        self.total = 0


class DiggingEstimator:
    def create_team(self, length, days, rock_type, mining_location="safe_zone"):
        dig_per_rotation = self.ask_api_for_dwarfs_mining_distance_per_rock_type(rock_type)
        max_dig_per_rotation = dig_per_rotation[len(dig_per_rotation) - 1]
        max_dig_per_day = 2 * max_dig_per_rotation

        if math.floor(length) != length or math.floor(days) != days or length < 0 or days < 0:
            raise InvalidFormatException()
        if math.floor(length / days) > max_dig_per_day:
            raise TunnelTooLongForDelayException()

        presence_of_goblins = self.ask_api_presence_of_goblins(mining_location)
        composition = TeamComposition()

        # Miners
        for i in range(0, len(dig_per_rotation) - 1):
            if dig_per_rotation[i] < math.floor(length / days):
                composition.day_team.miners += 1

        if math.floor(length / days) > max_dig_per_rotation:
            for i in range(0, len(dig_per_rotation) - 1):
                if dig_per_rotation[i] + max_dig_per_rotation < math.floor(length / days):
                    composition.night_team.miners += 1

        day_team = composition.day_team
        night_team = composition.night_team

        if day_team.miners > 0:
            if presence_of_goblins:
                day_team.add_worker(WORKER.PROTECTORS, 2)
            day_team.add_worker(WORKER.HEALERS)
            day_team.add_worker(WORKER.SMITHIES, 2)

            nb_inn_keepers_to_add = math.ceil((day_team.miners
                                               + day_team.healers
                                               + day_team.smithies
                                               + day_team.protectors) / 4.0) * 4
            day_team.add_worker(WORKER.INN_KEEPERS, nb_inn_keepers_to_add)

            nb_inn_washers_to_add = math.ceil((day_team.miners + day_team.healers + day_team.smithies +
                                               day_team.inn_keepers + day_team.protectors) / 10.0)
            day_team.add_worker(WORKER.WASHERS, nb_inn_washers_to_add)

        if night_team.miners > 0:
            if presence_of_goblins:
                night_team.add_worker(WORKER.PROTECTORS, 2)
            night_team.add_worker(WORKER.HEALERS)
            night_team.add_worker(WORKER.SMITHIES, 2)
            night_team.add_worker(WORKER.LIGHTERS, night_team.miners + 1 + night_team.protectors)

            nb_inn_keepers_to_add_for_night_team = math.ceil(
                (night_team.miners
                 + night_team.healers
                 + night_team.smithies
                 + night_team.lighters
                 + night_team.protectors) / 4.0) * 4
            night_team.add_worker(WORKER.INN_KEEPERS, nb_inn_keepers_to_add_for_night_team)

        nb_washers, nb_guards, nb_guard_managers = night_team.calculate_nb_washers_guard_and_guard_managers(0, 0, 0)
        night_team.add_worker(WORKER.WASHERS, nb_washers)
        night_team.add_worker(WORKER.GUARDS, nb_guards)
        night_team.add_worker(WORKER.GUARD_MANAGERS, nb_guard_managers)

        composition.total = day_team.get_nb_worker() + night_team.get_nb_worker()

        return composition

    def ask_api_for_dwarfs_mining_distance_per_rock_type(self, rock_type):
        # for example for granite it returns [0, 3, 5.5, 7]
        # if you put 0 dwarf, you dig 0m / d / team
        # if you put 1 dwarf, you dig 3m / d / team
        # 2 dwarves = 5.5 m / d / team
        # so a day team on 2 miners and a night team of 1 miner dig 8.5 m / d
        url = "dtp://research.vin.co/digging-rate/" + rock_type
        print("Trying to fetch" + url)
        raise ApiErrorException("Does not work in test mode")

    def ask_api_presence_of_goblins(self, location):
        # for example for "safe_zone" it returns False
        # for example, for "moria's mine" it returns True
        if location == "safe_zone":
            return False
        else:
            url = "dtp://research.vin.co/are-there-goblins/" + location
            print("Trying to fetch" + url)
            raise ApiErrorException("Does not work in test mode")