import random
import copy

# CONFIG
simulations = 1
verbose = True
power_ups = True
accounting_error_win_boost_factor = 1.1


def score(position: int, power_up: str):

    # gives double points then subtracts 3
    if power_up == "double_edged_sword":
        if position == 1:
            return 37
        if position == 2:
            return 21
        if position == 3:
            return 13
        if position == 4:
            return 9
        if position == 5:
            return 5
        if position == 6:
            return 3
        if position == 7:
            return -1
        return -1

    if position == 1:
        return 20
    if position == 2:
        return 12
    if position == 3:
        return 8
    if position == 4:
        return 6
    if position == 5:
        return 4
    if position == 6:
        return 3
    if position == 7:
        return 2
    return 1


games = [
    "world_of_warcraft",
    "battleblock_theater",
    "kerbal_space_program",
    "geoguessr",
    "jump_king",
    "planet_coaster",
    "war_thunder",
    "hollow_knight",
    "pummel_party",
    "pubg"
]

people = [
    "vegard",
    "karl_yngve",
    "sondre",
    "ingvild",
    "hilde",
    "sunniva",
    "robin",
    "ivar"
]

game_chosen_by = {
    "world_of_warcraft": "ingvild",
    "battleblock_theater": "hilde",
    "kerbal_space_program": "vegard",
    "geoguessr": "karl_yngve",
    "jump_king": "sondre",
    "planet_coaster": "karl_yngve",
    "war_thunder": "vegard",
    "hollow_knight": "hilde",
    "pummel_party": "sondre",
    "pubg": "ingvild"
}


win_chances = {
    "vegard":     {"world_of_warcraft": 0.10, "battleblock_theater": 0.30, "kerbal_space_program": 0.10, "geoguessr": 0.10, "jump_king": 0.10, "planet_coaster": 0.10, "war_thunder": 0.10, "hollow_knight": 0.10, "pummel_party": 0.10, "pubg": 0.10},
    "karl_yngve": {"world_of_warcraft": 0.10, "battleblock_theater": 0.10, "kerbal_space_program": 0.10, "geoguessr": 0.30, "jump_king": 0.10, "planet_coaster": 0.10, "war_thunder": 0.10, "hollow_knight": 0.10, "pummel_party": 0.10, "pubg": 0.10},
    "sondre":     {"world_of_warcraft": 0.10, "battleblock_theater": 0.10, "kerbal_space_program": 0.10, "geoguessr": 0.10, "jump_king": 0.10, "planet_coaster": 0.10, "war_thunder": 0.10, "hollow_knight": 0.10, "pummel_party": 0.30, "pubg": 0.10},
    "ingvild":    {"world_of_warcraft": 0.10, "battleblock_theater": 0.10, "kerbal_space_program": 0.10, "geoguessr": 0.10, "jump_king": 0.10, "planet_coaster": 0.30, "war_thunder": 0.10, "hollow_knight": 0.10, "pummel_party": 0.10, "pubg": 0.10},
    "hilde":      {"world_of_warcraft": 0.30, "battleblock_theater": 0.10, "kerbal_space_program": 0.10, "geoguessr": 0.10, "jump_king": 0.10, "planet_coaster": 0.10, "war_thunder": 0.10, "hollow_knight": 0.10, "pummel_party": 0.10, "pubg": 0.10},
    "sunniva":    {"world_of_warcraft": 0.10, "battleblock_theater": 0.10, "kerbal_space_program": 0.10, "geoguessr": 0.10, "jump_king": 0.10, "planet_coaster": 0.10, "war_thunder": 0.10, "hollow_knight": 0.30, "pummel_party": 0.10, "pubg": 0.10},
    "robin":      {"world_of_warcraft": 0.10, "battleblock_theater": 0.10, "kerbal_space_program": 0.30, "geoguessr": 0.10, "jump_king": 0.10, "planet_coaster": 0.10, "war_thunder": 0.10, "hollow_knight": 0.10, "pummel_party": 0.10, "pubg": 0.10},
    "ivar":       {"world_of_warcraft": 0.10, "battleblock_theater": 0.10, "kerbal_space_program": 0.10, "geoguessr": 0.10, "jump_king": 0.10, "planet_coaster": 0.10, "war_thunder": 0.10, "hollow_knight": 0.10, "pummel_party": 0.10, "pubg": 0.30},
}

power_up_chances = {

    "vegard": {
        "double_edged_sword": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125},
        "accounting_error": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125}
    },
    "karl_yngve": {
        "double_edged_sword": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125},
        "accounting_error": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125}
    },
    "sondre": {
        "double_edged_sword": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125},
        "accounting_error": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125}
    },
    "ingvild": {
        "double_edged_sword": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125},
        "accounting_error": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125}
    },
    "hilde": {
        "double_edged_sword": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125},
        "accounting_error": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125}
    },
    "sunniva": {
        "double_edged_sword": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125},
        "accounting_error": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125}
    },
    "robin": {
        "double_edged_sword": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125},
        "accounting_error": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125}
    },
    "ivar": {
        "double_edged_sword": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125},
        "accounting_error": {"world_of_warcraft": 0.125, "battleblock_theater": 0.125, "kerbal_space_program": 0.125, "geoguessr": 0.125, "jump_king": 0.125, "planet_coaster": 0.125, "war_thunder": 0.125, "hollow_knight": 0.125, "pummel_party": 0.125, "pubg": 0.125}
    },
}

crystal_ballin_win_chance = {
    "vegard": 0.5,
    "karl_yngve": 0.5,
    "sondre": 0.5,
    "ingvild": 0.5,
    "hilde": 0.5,
    "sunniva": 0.5,
    "robin": 0.5,
    "ivar": 0.5
}


class player:
    def __init__(self, name: str, win_chances: dict, crystal_ballin_win_chance: float, power_up_chances: dict):
        self.name = name
        self.points = 0
        self.win_chances = win_chances
        self.crystal_ballin_win_chance = crystal_ballin_win_chance
        self.power_up_chances = power_up_chances
        self.power_ups_choices = {
            "double_edged_sword": pick_from_probabilities([(game, self.power_up_chances["double_edged_sword"][game]) for game in self.power_up_chances["double_edged_sword"]]),
        }

    def add_points(self, points: int):
        self.points += points

    def __str__(self):
        return self.name + ": " + str(self.points)


def pick_from_probabilities(options_with_probabilities: list):
    win_number = random.random() * sum([option[1]
                                        for option in options_with_probabilities])
    for option in options_with_probabilities:
        if win_number <= option[1]:
            return option[0]
        win_number -= option[1]
    Exception("No winner found")


def pick_gamba_power_up(gamba_power_up_chances: dict):
    game_picked = pick_from_probabilities(
        [(game, gamba_power_up_chances[game][0]) for game in gamba_power_up_chances])
    player_picked = gamba_power_up_chances[game_picked][1]
    return (game_picked, player_picked)


def check_crystal_ballin_points(player: player, verbose: bool):
    if random.random() <= player.crystal_ballin_win_chance:
        if verbose:
            print(player.name, "won crystal ballin")
        player.add_points(3)


def pick_next_best_position(game: str, players: list):
    # construct list of players with win probabilities
    players_with_probabilities = []
    for player in players:
        players_with_probabilities.append(
            (player.name, player.win_chances[game]))

    # pick winner
    winner = pick_from_probabilities(players_with_probabilities)

    # remove winner from player list
    players = [player for player in players if player.name != winner]

    return winner, players


def check_if_power_up(player: player, game: str, verbose: bool):
    if power_ups and player.power_ups_choices["double_edged_sword"] == game:
        if verbose:
            print(player.name + " used double up")
        return "double_edged_sword"
    return "none"


def mutate_win_chances(win_chances: dict, power_up_chances: dict):
    mutated_win_chances = copy.deepcopy(win_chances)
    for player in power_up_chances:
        mutate_win_probabilities = [(game, power_up_chances[player]["accounting_error"][game])
                                    for game in power_up_chances[player]["accounting_error"]]
        chosen_game = pick_from_probabilities(mutate_win_probabilities)
        mutated_win_chances[player][chosen_game] = mutated_win_chances[player][chosen_game] * \
            accounting_error_win_boost_factor
    return mutated_win_chances


def do_turn(game: str, players: list, verbose: bool):
    if verbose:
        print("\n" + game + " round:")

    players_of_round = players

    first, players_of_round = pick_next_best_position(game, players_of_round)
    second, players_of_round = pick_next_best_position(game, players_of_round)
    third, players_of_round = pick_next_best_position(game, players_of_round)
    fourth, players_of_round = pick_next_best_position(game, players_of_round)
    fifth, players_of_round = pick_next_best_position(game, players_of_round)
    sixth, players_of_round = pick_next_best_position(game, players_of_round)
    seventh, players_of_round = pick_next_best_position(game, players_of_round)
    eighth, players_of_round = pick_next_best_position(game, players_of_round)

    # Add points to players
    for player in players:
        if player.name == first:
            player.add_points(
                score(1, check_if_power_up(player, game, verbose)))
        if player.name == second:
            player.add_points(
                score(2, check_if_power_up(player, game, verbose)))
        if player.name == third:
            player.add_points(
                score(3, check_if_power_up(player, game, verbose)))
        if player.name == fourth:
            player.add_points(
                score(4, check_if_power_up(player, game, verbose)))
        if player.name == fifth:
            player.add_points(
                score(5, check_if_power_up(player, game, verbose)))
        if player.name == sixth:
            player.add_points(
                score(6, check_if_power_up(player, game, verbose)))
        if player.name == seventh:
            player.add_points(
                score(7, check_if_power_up(player, game, verbose)))
        if player.name == eighth:
            player.add_points(
                score(8, check_if_power_up(player, game, verbose)))

    if verbose:
        print("First:", first, "| Second:", second, "| Third:",
              third, "| Fourth:", fourth, "| Fifth:", fifth,
              "| Sixth:", sixth, "| Seventh:", seventh, "| Eighth:", eighth)


def simulate_tournament(win_chances: dict, power_up_chances: dict, verbose: bool = False):
    mutated_win_chances = mutate_win_chances(win_chances, power_up_chances)

    players = [
        player("vegard", mutated_win_chances["vegard"],
               crystal_ballin_win_chance["vegard"], power_up_chances["vegard"]),
        player("karl_yngve", mutated_win_chances["karl_yngve"],
               crystal_ballin_win_chance["karl_yngve"], power_up_chances["karl_yngve"]),
        player("sondre", mutated_win_chances["sondre"],
               crystal_ballin_win_chance["sondre"], power_up_chances["sondre"]),
        player("ingvild", mutated_win_chances["ingvild"],
               crystal_ballin_win_chance["ingvild"], power_up_chances["ingvild"]),
        player("hilde", mutated_win_chances["hilde"],
               crystal_ballin_win_chance["hilde"], power_up_chances["hilde"]),
        player("sunniva", mutated_win_chances["sunniva"],
               crystal_ballin_win_chance["sunniva"], power_up_chances["sunniva"]),
        player("robin", mutated_win_chances["robin"],
               crystal_ballin_win_chance["robin"], power_up_chances["robin"]),
        player("ivar", mutated_win_chances["ivar"],
               crystal_ballin_win_chance["ivar"], power_up_chances["ivar"])
    ]

    for player_looked_at in players:
        check_crystal_ballin_points(player_looked_at, verbose)

    for game in games:
        do_turn(game, players, verbose)
        if verbose:
            print("Point scores after " + game + ":")
            for p in players:
                print(p)

    return players


def simulationRun(print_results_per_simulation: bool, win_chances: dict, power_up_chances: dict, simulations: int):
    wins = {
        "vegard": 0,
        "karl_yngve": 0,
        "sondre": 0,
        "ingvild": 0,
        "hilde": 0,
        "sunniva": 0,
        "robin": 0,
        "ivar": 0
    }

    point_sums = {
        "vegard": 0,
        "karl_yngve": 0,
        "sondre": 0,
        "ingvild": 0,
        "hilde": 0,
        "sunniva": 0,
        "robin": 0,
        "ivar": 0
    }

    for i in range(simulations):
        players = simulate_tournament(
            win_chances, power_up_chances, verbose=verbose)
        for p in players:
            point_sums[p.name] += p.points
            if p.points == max([p.points for p in players]):
                wins[p.name] += 1

    point_averges = {
        "vegard": point_sums["vegard"] / simulations,
        "karl_yngve": point_sums["karl_yngve"] / simulations,
        "sondre": point_sums["sondre"] / simulations,
        "ingvild": point_sums["ingvild"] / simulations,
        "hilde": point_sums["hilde"] / simulations,
        "sunniva": point_sums["sunniva"] / simulations,
        "robin": point_sums["robin"] / simulations,
        "ivar": point_sums["ivar"] / simulations
    }

    win_percentage = {
        "vegard": str(round(wins["vegard"] / simulations * 100, 2)) + "%",
        "karl_yngve": str(round(wins["karl_yngve"] / simulations * 100, 2)) + "%",
        "sondre": str(round(wins["sondre"] / simulations * 100, 2)) + "%",
        "ingvild": str(round(wins["ingvild"] / simulations * 100, 2)) + "%",
        "hilde": str(round(wins["hilde"] / simulations * 100, 2)) + "%",
        "sunniva": str(round(wins["sunniva"] / simulations * 100, 2)) + "%",
        "robin": str(round(wins["robin"] / simulations * 100, 2)) + "%",
        "ivar": str(round(wins["ivar"] / simulations * 100, 2)) + "%"
    }

    if print_results_per_simulation:
        print("\n------------------------------------------\n")
        print(simulations, "simulations completed, results:")
        print("\nWin distribution: ")
        print(win_percentage)
        print("\nAverage point distribution: ")
        print(point_averges)

    return win_percentage, point_averges


def optimize_power_ups(power_up_chances: dict, simulation_player: str):
    power_up_combinations = []

    # Construct list of all valid combinations of powerup choices by the player
    for double_edged_sword_game in games:
        if game_chosen_by[double_edged_sword_game] != simulation_player:
            for accounting_error_game in games:
                if double_edged_sword_game != accounting_error_game:
                    power_up_combinations.append({"double_edged_sword": {
                                                 double_edged_sword_game: 1}, "accounting_error": {accounting_error_game: 1}})

    print("Number of combinations:", len(power_up_combinations), "\nnumber of simulations:",
          simulations, "\ntotal number of simulations:", len(power_up_combinations) * simulations)

    results = []
    for combo in power_up_combinations:
        if False:
            # TODO fix
            print(combo)
        power_up_chances = {
            # TODO generate this dynamically based on simulation_player
            simulation_player: combo,
            "ingvild": power_up_chances["ingvild"],
            "karl_yngve": power_up_chances["karl_yngve"],
            "sondre": power_up_chances["sondre"],
            "hilde": power_up_chances["hilde"]
        }
        run_wins, run_point_averages = simulationRun(
            False, win_chances, power_up_chances, simulations)
        results.append({"win_distribution": run_wins,
                       "point_averages": run_point_averages, "power_up_combo": combo})

    sorted_results = sorted(
        results, key=lambda k: k['win_distribution'][simulation_player], reverse=True)
    print("Top 3 combinations:")
    print("\n------------------------------------------\n")
    print(sorted_results[0])
    print("\n------------------------------------------\n")
    print(sorted_results[1])
    print("\n------------------------------------------\n")
    print(sorted_results[2])
    print("\n------------------------------------------\n")


simulationRun(True, win_chances, power_up_chances, simulations)

# optimize_power_ups(power_up_chances, "vegard")
