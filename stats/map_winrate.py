import numpy
from collections import Counter

class TotalRates:
    @staticmethod
    def get_total_map_rates(maps):
        winrate = TotalRates.get_total_winrates(maps)
        lossrate = TotalRates.get_total_lossrates(maps)
        drawrate = TotalRates.get_total_drawrates(maps)

        return [winrate, lossrate, drawrate]

    @staticmethod
    def get_total_winrates(maps):
        results = Counter([map_data.result for map_data in maps])

        total_matches = sum(results.values())
        win_rate = results["Win"]/total_matches

        return win_rate

    @staticmethod
    def get_total_lossrates(maps):
        results = Counter([map_data.result for map_data in maps])

        total_matches = sum(results.values())
        loss_rate = results["Loss"]/total_matches

        return loss_rate

    @staticmethod
    def get_total_drawrates(maps):
        results = Counter([map_data.result for map_data in maps])

        total_matches = sum(results.values())
        draw_rate = results["Draw"]/total_matches

        return draw_rate

class SpecificRates:
    @staticmethod
    def get_all_specific_map_rates(maps):
        winrate = SpecificRates.get_all_specific_map_winrates(maps)
        lossrate = SpecificRates.get_all_specific_map_lossrates(maps)
        drawrate = SpecificRates.get_all_specific_map_drawrates(maps)

        return [winrate, lossrate, drawrate]

    @staticmethod
    def get_all_specific_map_winrates(maps):
        map_results = {match.map_name: Counter() for match in maps}

        for match in maps:
            map_results[match.map_name][match.result] += 1

        map_winrates = {map_name: map_results[map_name]["Win"] / sum(map_results[map_name].values()) for map_name in map_results}

        return map_winrates

    @staticmethod
    def get_all_specific_map_lossrates(maps):
        map_results = {match.map_name: Counter() for match in maps}

        for match in maps:
            map_results[match.map_name][match.result] += 1

        map_lossrates = {map_name: map_results[map_name]["Loss"] / sum(map_results[map_name].values()) for map_name in map_results}

        return map_lossrates

    @staticmethod
    def get_all_specific_map_drawrates(maps):
        map_results = {match.map_name: Counter() for match in maps}

        for match in maps:
            map_results[match.map_name][match.result] += 1

        map_drawrates = {map_name: map_results[map_name]["Draw"] / sum(map_results[map_name].values()) for map_name in map_results}

        return map_drawrates