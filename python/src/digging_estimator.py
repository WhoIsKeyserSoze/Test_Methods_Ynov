import math
from enum import Enum

class WORKER(Enum):
    MINER = 1
    HEALER = 2
    SMITHIE = 3
    LIGTHER = 4
    INN_KEEPER = 5
    GUARD = 6
    GUARD_MANAGER = 7
    WASHER = 8

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
        return self.miners+self.healers+self.smithies+self.lighters+self.inn_keepers+self.guards+self.guard_managers+self.washers

    def add_worker(self, worker_type, nb_worker_to_add=1):

        match worker_type:
            case WORKER.MINER:
                self.miners += nb_worker_to_add
            case WORKER.HEALER:
                self.miners += nb_worker_to_add
            case WORKER.SMITHIE:
                self.miners += nb_worker_to_add
            case WORKER.LIGTHER:
                self.miners += nb_worker_to_add
            case WORKER.INN_KEEPER:
                self.miners += nb_worker_to_add
            case WORKER.GUARD:
                self.miners += nb_worker_to_add
            case WORKER.GUARD_MANAGER:
                self.miners += nb_worker_to_add
            case WORKER.WASHER:
                self.miners += nb_worker_to_add
            case _:
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
        for i in range(0, len(dig_per_rotation)-1):
            if dig_per_rotation[i] < math.floor(length / days):
                composition.day_team.miners += 1

        if math.floor(length / days) > max_dig_per_rotation:
            for i in range(0, len(dig_per_rotation) -1):
                if dig_per_rotation[i] + max_dig_per_rotation < math.floor(length / days):
                    composition.night_team.miners += 1

        dt = composition.day_team
        nt = composition.night_team

        if dt.miners > 0:
            dt.healers += 1
            dt.smithies += 1
            dt.smithies += 1

        if nt.miners > 0:
            nt.healers += 1
            nt.smithies += 1
            nt.smithies += 1

        if nt.miners > 0:
            nt.lighters = nt.miners + 1

        if dt.miners > 0:
            dt.inn_keepers = math.ceil((dt.miners + dt.healers + dt.smithies) / 4.0) * 4
            dt.washers = math.ceil((dt.miners + dt.healers + dt.smithies + dt.inn_keepers) / 10.0)

        if nt.miners > 0:
            nt.inn_keepers = math.ceil((nt.miners + nt.healers + nt.smithies + nt.lighters) / 4.0) * 4

        while True:
            old_washers = nt.washers
            old_guards = nt.guards
            old_chief_guard = nt.guard_managers

            nt.washers = math.ceil((nt.miners + nt.healers + nt.smithies + nt.inn_keepers + nt.lighters + nt.guards + nt.guard_managers) / 10.0)
            nt.guards = math.ceil((nt.healers + nt.miners + nt.smithies + nt.lighters + nt.washers) / 3.0)
            nt.guard_managers = math.ceil((nt.guards) / 3.0)

            if old_washers == nt.washers and old_guards == nt.guards and old_chief_guard == nt.guard_managers:
                break

        composition.total = dt.get_nb_worker() + nt.get_nb_worker()

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
