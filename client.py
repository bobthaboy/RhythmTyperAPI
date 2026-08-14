import requests
from helper import find_new_data
from endpoints import get_beatmap, user_lookup, get_user_profile, first_place_scores, activity_heatmap, \
    get_user_favorites, get_most_played_beatmaps, get_user_beatmaps, get_beatmaps, get_nominations, leaderboard_global, \
    leaderboard_countries, leaderboard_top_plays, get_difficulties, beatmap_leaderboard, beatmap_comments, \
    unplayed_difficulties, user_best_scores


class RhythmTyperClient:
    BASE_URL = "https://api.rhythmtyper.net"

    def __init__(self, api_testing=False):
        self.api_testing = api_testing

    def get(self, path, **params):
        response = requests.get(
            f"{self.BASE_URL}/{path.lstrip('/')}",
            params=params,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        if self.api_testing:
            find_new_data(data)

        return data

    get_beatmap = get_beatmap
    user_lookup = user_lookup
    get_user_profile = get_user_profile
    first_place_scores = first_place_scores
    activity_heatmap = activity_heatmap
    get_user_favorites = get_user_favorites
    get_most_played_beatmaps = get_most_played_beatmaps
    get_user_beatmaps = get_user_beatmaps
    get_beatmaps = get_beatmaps
    get_nominations = get_nominations
    leaderboard_global = leaderboard_global
    leaderboard_countries = leaderboard_countries
    leaderboard_top_plays = leaderboard_top_plays
    get_difficulties = get_difficulties
    beatmap_leaderboard = beatmap_leaderboard
    beatmap_comments = beatmap_comments
    unplayed_difficulties = unplayed_difficulties
    user_best_scores = user_best_scores
