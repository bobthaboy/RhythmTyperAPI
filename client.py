import requests
from datetime import datetime, date
from .helper import find_new_data, parse_timestamp
from .models import Grades, RankHistoryEntry, Play, RecentActivity, UserProfile, Score, FirstPlaceScores, \
    MostPlayedBeatmap, CustomDifficulty, VersionHistory, Beatmap, BeatmapList, GlobalLeaderboard, CountryLeaderboard, \
    TopPlaysLeaderboard, BeatmapDifficulty, LeaderboardScore, Comment, UnplayedDifficulty, UnplayedDifficulties, \
    BestScore, BestScores, UserSearchResult


class RhythmTyperClient():
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

    def get_beatmap(self, mapset_id: str) -> Beatmap:
        """
        Returns given beatmap.
        """
        response = self.get(
            "getBeatmaps",
            limit=1,
            mapsetId=mapset_id,
        )

        song_list = response.get("beatmaps", [])

        if not song_list:
            raise ValueError(f"No beatmap found for mapset ID {mapset_id}")

        song = song_list[0]

        for diff in song["difficulties"]:
            if "noteCount" in diff:
                diff["tapCount"] = diff["noteCount"]
                diff["holdCount"] = int(diff["holdCount"] / 2)

        song["difficulties"] = [
            CustomDifficulty.from_dict(item)
            for item in song["difficulties"]
        ]

        if "versionHistory" in song:
            song["versionHistory"] = [
                VersionHistory.from_dict(item)
                for item in song["versionHistory"]
            ]

        return Beatmap.from_dict(song)

    def user_lookup(self, username: str, limit: int = 50) -> list[UserSearchResult]:
        """Returns the users that show up on the search."""
        if len(username) < 2:
            raise ValueError("Username must be at least 2 characters long.")

        response = self.get(
            "v2/users/search",
            query=username,
            limit=limit,
        )

        return [UserSearchResult.from_dict(user) for user in response]

    def get_user_profile(self, user_id: str) -> UserProfile:
        """Return a user's profile."""
        response = self.get(f"v2/profile/{user_id}")

        response["createdAt"] = parse_timestamp(response.get("createdAt"))
        response["profilePictureUpdatedAt"] = parse_timestamp(response.get("profilePictureUpdatedAt"))
        response["lastPPRecalculation"] = parse_timestamp(response.get("lastPPRecalculation"))
        response["lastRankedScoreRecalculation"] = parse_timestamp(response.get("lastRankedScoreRecalculation"))
        response["lastTopPlaysUpdate"] = parse_timestamp(response.get("lastTopPlaysUpdate"))
        response["lastUpdated"] = parse_timestamp(response.get("lastUpdated"))
        response["playHeatmap"] = {
            datetime.strptime(date_str, "%Y-%m-%d").date(): value
            for date_str, value in response["playHeatmap"].items()
        }
        response["grades"] = Grades(**response["grades"])
        response["rankHistory"] = [
            RankHistoryEntry.from_dict(item)
            for item in response["rankHistory"]
        ]

        response["recentPlays"] = [
            Play.from_dict(item)
            for item in response["recentPlays"]
        ]

        response["topPlays"] = [
            Play.from_dict(item)
            for item in response["topPlays"]
        ]
        # response["topPlaysExpanded"] = [
        #     RecentPlays.from_dict(item)
        #     for item in response["topPlaysExpanded"]
        # ]
        response.setdefault("recentActivity", [])
        response["recentActivity"] = [
            RecentActivity.from_dict(item)
            for item in response["recentActivity"]
        ]
        return UserProfile.from_dict(response)

    def first_place_scores(self, user_id: str) -> FirstPlaceScores:
        """Returns all the first place scores of a user."""
        response = self.get(f"v2/user/{user_id}/firstPlaceScores")

        response["scores"] = [
            Score.from_dict(item)
            for item in response["scores"]
        ]
        return FirstPlaceScores(**response)

    def activity_heatmap(self, user_id: str) -> dict[date, int]:
        """Returns a dictionary containing a date as the key and play count as the value."""
        response = self.get(
            f"v2/stats/{user_id}/charts",
            type="heatmap"
        )

        response = {datetime.strptime(date_str, "%Y-%m-%d").date(): value
                    for date_str, value in response.items()}

        return response

    def get_user_favorites(self, user_id: str) -> list[Beatmap]:
        """Returns all maps a user favorited."""
        response = self.get(
            f"getUserFavorites/{user_id}",
        )

        favorites_list = response.get("favorites", [])
        return [Beatmap.from_dict(fav) for fav in favorites_list]

    def get_most_played_beatmaps(self, user_id: str, limit: int = 50) -> list[MostPlayedBeatmap]:
        """Returns user's most played maps."""
        response = self.get(
            f"getMostPlayedBeatmaps/{user_id}",
            limit=limit
        )

        most_played_list = response.get("mostPlayed", [])
        for song in most_played_list:
            song["lastPlayed"] = parse_timestamp(song.get("lastPlayed"))
        return [MostPlayedBeatmap.from_dict(song) for song in most_played_list]

    def get_user_beatmaps(self, mapper_id: str, cursor: str | None = None, limit: int = 50) -> BeatmapList:
        """
        Returns beatmaps uploaded by a mapper_id.
        """
        response = self.get(
            "getBeatmaps",
            mapperId=mapper_id,
            cursor=cursor,
            limit=limit
        )

        song_list = response.get("beatmaps", [])
        for song in song_list:
            for diff in song["difficulties"]:
                if "noteCount" in diff:
                    diff["tapCount"] = diff["noteCount"]
                    diff["holdCount"] = int(diff["holdCount"] / 2)

            song["difficulties"] = [
                CustomDifficulty.from_dict(item)
                for item in song["difficulties"]
            ]

            if "versionHistory" in song:
                song["versionHistory"] = [
                    VersionHistory.from_dict(item)
                    for item in song["versionHistory"]
                ]

        return BeatmapList.from_dict(response)

    def get_beatmaps(self, limit: int = 50, cursor: str | None = None, status: str = "ranked",
                     sort: str | None = None,
                     explicit: bool = True, language: str = "all") -> BeatmapList:
        """
        Returns beatmaps. \n
        Valid statuses are: "all", "ranked", "loved", "qualified", "nominated", "unranked", "custom".
        """
        response = self.get(
            "getBeatmaps",
            limit=limit,
            cursor=cursor,
            status=status,
            sortBy=sort,
            showExplicit=str(explicit).lower(),
            language=language,
        )

        song_list = response.get("beatmaps", [])
        for song in song_list:
            for diff in song["difficulties"]:
                if "noteCount" in diff:
                    diff["tapCount"] = diff["noteCount"]
                    diff["holdCount"] /= 2

            song["difficulties"] = [
                CustomDifficulty.from_dict(item)
                for item in song["difficulties"]
            ]

            if "versionHistory" in song:
                song["versionHistory"] = [
                    VersionHistory.from_dict(item)
                    for item in song["versionHistory"]
                ]

        return BeatmapList.from_dict(response)

    def get_nominations(self, user_id: str) -> list[Beatmap]:
        """Returns user's nominations."""
        response = self.get(f"getNominatedBeatmaps/{user_id}")

        song_list = response.get("beatmaps", [])
        for song in song_list:
            song["difficulties"] = [
                CustomDifficulty.from_dict(item)
                for item in song.get("difficulties", [])
            ]

            song["versionHistory"] = [
                VersionHistory.from_dict(item)
                for item in song.get("versionHistory", [])
            ]

        return [Beatmap.from_dict(song) for song in song_list]

    def leaderboard_global(self, limit: int = 50, offset: int = 0, country: str | None = None, sort: str = "pp") -> \
            list[
                GlobalLeaderboard]:
        """
        Returns global leaderboards. Accepts country. \n
        Valid sorts are: "pp", "score".
        """
        match sort:
            case "pp":
                sort = "totalPP"
            case "score":
                sort = "rankedScore"
            case _:
                raise ValueError('Sort must be "pp" or "score".')

        response = self.get(
            "v2/leaderboard",
            limit=limit,
            offset=offset,
            country=country,
            sortBy=sort
        )

        return [GlobalLeaderboard.from_dict(item) for item in response]

    def leaderboard_countries(self, limit: int = 50, offset: int = 0, sort: str = "pp") -> list[CountryLeaderboard]:
        """Returns the combined leaderboard of countries. Not to be confused with a country's individual leaderboard."""
        match sort:
            case "pp":
                sort = "totalPP"
            case "score":
                sort = "rankedScore"

        response = self.get(
            "v2/leaderboard/countries",
            limit=limit,
            offset=offset,
            sortBy=sort
        )

        return [CountryLeaderboard.from_dict(item) for item in response["countries"]]

    def leaderboard_top_plays(self, limit: int = 50, offset: int = 0, unique: bool = False) -> list[
        TopPlaysLeaderboard]:
        """Returns the top PP scores leaderboard."""
        response = self.get(
            "v2/leaderboard/plays",
            limit=limit,
            offset=offset,
            unique=str(unique).lower()
        )

        return [TopPlaysLeaderboard.from_dict(item) for item in response["plays"]]

    def get_difficulties(self, beatmap_id: str) -> list[BeatmapDifficulty]:
        """Returns the difficulties for a map."""
        response = self.get(f"v2/beatmap/{beatmap_id}/difficulties")

        return [BeatmapDifficulty.from_dict(item) for item in response]

    def beatmap_leaderboard(self, beatmap_id: str, difficulty: str, limit: int = 50) -> list[LeaderboardScore]:
        """Returns the leaderboards for a beatmap."""
        response = self.get(
            f"v2/beatmap/{beatmap_id}/leaderboard",
            difficulty=difficulty,
            limit=limit
        )

        return [LeaderboardScore.from_dict(item) for item in response]

    def beatmap_comments(self, beatmap_id: str, limit: int = 50) -> list[Comment]:
        """Returns the comments on a mapset."""
        response = self.get(
            f"getComments/{beatmap_id}",
            limit=limit
        )

        comments = response["comments"]
        return [Comment.from_dict(item) for item in comments]

    def unplayed_difficulties(self, user_id: str, limit: int = 100) -> UnplayedDifficulties:
        """Returns all the difficulties a user hasn't played."""
        response = self.get(
            f"v2/user/{user_id}/unplayedDifficulties",
            limit=limit
        )

        response["unplayed"] = [UnplayedDifficulty.from_dict(item) for item in response["unplayed"]]
        return UnplayedDifficulties(**response)

    def user_best_scores(self, user_id: str, limit: int = 100) -> BestScores:
        """Returns the user's best scores by highest Ranked Score."""
        response = self.get(
            f"v2/user/{user_id}/bestScores",
            limit=limit
        )

        response["scores"] = [BestScore.from_dict(item) for item in response["scores"]]
        return BestScores(**response)
