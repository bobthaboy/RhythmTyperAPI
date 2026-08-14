import requests
from dataclasses import dataclass
from datetime import date, datetime, timezone


def parse_timestamp(ts) -> datetime | None:
    if isinstance(ts, str):
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    elif isinstance(ts, dict):
        return datetime.fromtimestamp(ts.get("_seconds", 0), tz=timezone.utc)
    else:
        return None


@dataclass
class Grades:
    ss: int = 0
    s: int = 0
    a: int = 0
    b: int = 0
    c: int = 0
    d: int = 0
    f: int = 0


@dataclass
class RankHistoryEntry:
    date: date
    rank: int
    pp: float | int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            pp=data["pp"],
            rank=data["rank"],
            date=datetime.strptime(data["date"], "%Y-%m-%d").date()
        )


@dataclass
class Play:
    score_id: str
    beatmap_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty: str
    pp: float | int
    acc: float | int
    score: int
    combo: int
    grade: str
    mods: list[str]
    timestamp: datetime
    perfect: int
    good: int
    ok: int
    misses: int
    star_rating: float | int
    length: float | int
    od: float | int
    bpm: float | int
    mapper_id: str
    mapper: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            score_id=data["sid"],
            beatmap_id=data["bid"],
            beatmap_title=data["bt"],
            beatmap_artist=data["ba"],
            difficulty=data["diff"],
            pp=data["pp"],
            acc=data["acc"],
            score=data["sc"],
            combo=data["cb"],
            grade=data["gr"],
            mods=data["mods"],
            timestamp=datetime.fromisoformat(data["at"].replace("Z", "+00:00")),
            perfect=data["pf"],
            good=data["gd"],
            ok=data["ok"],
            misses=data["ms"],
            star_rating=data["sr"],
            length=data["len"],
            od=data["od"],
            bpm=data["bpm"],
            mapper_id=data["mid"],
            mapper=data["mn"]
        )


@dataclass
class RecentActivity:
    type: str
    beatmap_id: str
    timestamp: datetime
    beatmap_title: str
    beatmap_artist: str
    taken_by_user_id: str | None
    difficulty: str | None
    taken_by_username: str | None
    pp: float | int | None
    version: int | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            type=data["type"],
            beatmap_id=data["beatmapId"],
            difficulty=data.get("difficultyName"),
            beatmap_title=data["beatmapTitle"],
            beatmap_artist=data["beatmapArtist"],
            taken_by_user_id=data.get("takenByUserId"),
            taken_by_username=data.get("takenByUsername"),
            timestamp=datetime.fromisoformat(data["timestamp"].replace("Z", "+00:00")),
            pp=data.get("pp"),
            version=data.get("version"),
        )


@dataclass
class UserProfile:
    user_id: str
    username: str
    # username_lower: str
    country: str
    region: str | None
    # total_pp: float| int
    pp: float | int
    accuracy: float | int
    play_count: int
    # total_plays: int
    total_score: int
    ranked_score: int
    play_time: int
    # total_play_time: int
    # level: int
    # experience: int
    grades: Grades
    play_heatmap: dict
    recent_activity: list[RecentActivity]
    rank_history: list[RankHistoryEntry]
    top_plays: list[Play]
    # top_plays_expanded: list[TopPlays]
    top_plays_count: int
    top_plays_format: str
    recent_plays: list[Play]
    recent_plays_format: str
    profile_description: str
    follower_count: int
    following_count: int
    profile_picture_url: str
    global_rank: int
    country_rank: int
    created_at: datetime

    # profile_picture_version: str | None
    # profile_picture_updated_at: datetime
    # last_pp_recalculation: datetime
    # last_ranked_score_recalculation: datetime
    # last_top_plays_update: datetime
    # last_updated: datetime
    # raw_pp: float | int | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=data["userId"],
            username=data["username"],
            # total_plays=data["totalPlays"],
            # level=data["level"],
            # experience=data["experience"],
            # total_play_time=data["totalPlaytime"],
            country=data["country"],
            region=data["region"],
            created_at=data["createdAt"],
            recent_plays_format=data["recentPlaysFormat"],
            top_plays_format=data["topPlaysFormat"],
            profile_picture_url=data["profilePictureUrl"],
            # profile_picture_version=data.get("profilePictureVersion"),
            # profile_picture_updated_at=data["profilePictureUpdatedAt"],
            # username_lower=data["usernameLower"],
            top_plays_count=data["topPlaysCount"],
            # last_pp_recalculation=data["lastPPRecalculation"],
            # last_ranked_score_recalculation=data["lastRankedScoreRecalculation"],
            rank_history=data["rankHistory"],
            # last_top_plays_update=data["lastTopPlaysUpdate"],
            # last_updated=data["lastUpdated"],
            # raw_pp=data.get("rawPP"),
            global_rank=data["globalRank"],
            country_rank=data["countryRank"],
            pp=data["pp"],
            play_count=data["playCount"],
            accuracy=data["accuracy"],
            # total_pp=data["totalPP"],
            play_time=data["playTime"],
            grades=data["grades"],
            recent_plays=data["recentPlays"],
            ranked_score=data["rankedScore"],
            total_score=data["totalScore"],
            top_plays=data["topPlays"],
            play_heatmap=data["playHeatmap"],
            recent_activity=data["recentActivity"],
            # top_plays_expanded=data["topPlaysExpanded"],
            profile_description=data["profileDescription"],
            follower_count=data["followerCount"],
            following_count=data["followingCount"]
        )


@dataclass
class Score:
    score_id: str
    beatmap_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty: str
    acc: float | int
    pp: float | int
    score: int
    timestamp: datetime
    mods: list[str]
    combo: int
    grade: str
    tied_for_first: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            score_id=data["sid"],
            beatmap_id=data["bid"],
            beatmap_title=data["bt"],
            beatmap_artist=data["ba"],
            difficulty=data["diff"],
            acc=data["acc"],
            pp=data["pp"],
            score=data["score"],
            timestamp=datetime.fromisoformat(data["at"].replace("Z", "+00:00")),
            mods=data["mods"],
            combo=data["cb"],
            grade=data["gr"],
            tied_for_first=data["isTiedFor1st"],
        )


@dataclass
class FirstPlaceScores:
    scores: list[Score]
    count: int


@dataclass
class MostPlayedBeatmap:
    beatmap_id: str
    # mapset_id: str
    beatmap_artist: str
    beatmap_title: str
    difficulty: str
    background_image_url: str
    play_count: int
    last_played: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            beatmap_id=data["beatmapId"],
            # mapset_id=data["mapsetId"],
            beatmap_artist=data["artist"],
            beatmap_title=data["title"],
            difficulty=data["difficultyName"],
            background_image_url=data["backgroundImageUrl"],
            play_count=data["playCount"],
            last_played=data["lastPlayed"]
        )


@dataclass
class CustomDifficulty:
    beatmap_id: str
    difficulty_name: str
    star_rating: int
    star_rating_dt: int
    star_rating_ht: int
    od: int
    od_dt: float | int
    od_ht: float | int
    note_count: int
    tap_count: int
    catch_count: int
    hold_count: int
    typing_count: int
    length: float | int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            beatmap_id=data["diffId"],
            difficulty_name=data["name"],
            od=data["overallDifficulty"],
            star_rating=data["starRating"],
            star_rating_dt=data["starRatingNC"],
            od_dt=data["overallDifficultyNC"],
            star_rating_ht=data["starRatingHT"],
            od_ht=data["overallDifficultyHT"],
            tap_count=data["tapCount"],
            catch_count=data["catchCount"],
            hold_count=data["holdCount"],
            typing_count=data["typingCount"],
            length=data["length"],
            note_count=data["noteCount"],
        )


@dataclass
class VersionHistory:
    version: int
    type: str
    timestamp: datetime | None
    patch_notes: str | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            version=data["version"],
            type=data["type"],
            timestamp=parse_timestamp(data["timestamp"]),
            patch_notes=data.get("patchNotes")
        )


@dataclass
class Beatmap:
    mapset_id: str
    beatmap_title: str
    beatmap_artist: str
    mapper: str
    mapper_id: str
    bpm: int
    duration: float | int
    offset: int
    preview_time: int
    status: str
    ranked: bool
    description: str | None
    tags: list[str]
    language: str
    explicit: bool
    has_video: bool
    has_custom_hitsounds: bool
    audio_preview_url: str
    background_image_url: str
    background_urls: list[str]
    rtm_url: str
    rtm_size: int
    version: int
    play_count: int
    download_count: int
    favorite_count: int
    nomination_count: int
    version_history: list[VersionHistory]
    nominations: list[Nominator]
    difficulty_play_counts: dict
    uploaded_at: datetime
    ranked_date: datetime | None
    qualified_date: datetime | None
    last_played: datetime
    difficulties: list[CustomDifficulty]
    nominated_at: datetime | None

    # beatmap_id: str
    # search_text: str
    # search_tokens: list[str]
    # # uploaded_by: str
    # # rating: int
    # # rating_count: int
    # last_updated: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            # beatmap_id=data["id"],
            mapset_id=data["mapsetId"],
            beatmap_title=data["songName"],
            beatmap_artist=data["artistName"],
            mapper=data["mapper"],
            mapper_id=data["mapperId"],
            description=data["description"],
            tags=data["tags"],
            language=data["language"],
            explicit=data["explicit"],
            bpm=data["bpm"],
            offset=data["offset"],
            preview_time=data["previewTime"],
            duration=data["duration"],
            rtm_url=data["rtmUrl"],
            audio_preview_url=data["audioPreviewUrl"],
            background_urls=data["backgroundUrls"],
            background_image_url=data["backgroundImageUrl"],
            version=data["version"],
            has_video=data["hasVideo"],
            has_custom_hitsounds=data["hasCustomHitsounds"],
            rtm_size=data["rtmSize"],
            # search_text=data["searchText"],
            # search_tokens=data["searchTokens"],
            # uploaded_by=data["uploadedBy"],
            download_count=data["downloadCount"],
            status=data["status"],
            # rating=data["rating"],
            # rating_count=data["ratingCount"],
            difficulty_play_counts=data["difficultyPlayCounts"],
            version_history=data["versionHistory"],
            # last_updated=data["lastUpdatedAt"],
            uploaded_at=datetime.fromisoformat(data["uploadedAt"].replace("Z", "+00:00")),
            favorite_count=data["favoriteCount"],
            difficulties=data["difficulties"],
            play_count=data["playCount"],
            last_played=data["lastPlayed"],
            ranked=data["ranked"],
            nomination_count=data["nominationCount"],
            nominations=data["nominations"],
            nominated_at=data.get("nominatedAt"),
            ranked_date=parse_timestamp(data.get("rankedDate")),
            qualified_date=parse_timestamp(data.get("qualifiedDate"))
        )


@dataclass
class BeatmapList:
    beatmaps: list[Beatmap]
    has_more: bool
    next_cursor: str
    limit: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            beatmaps=[Beatmap.from_dict(b) for b in data["beatmaps"]],
            has_more=data["hasMore"],
            next_cursor=data["nextCursor"],
            limit=data["limit"]
        )


@dataclass
class Nominator:
    nominator_id: str
    nominator_username: str
    nominated_at: datetime | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nominator_id=data["nominatorId"],
            nominator_username=data["nominatorUsername"],
            nominated_at=parse_timestamp(data["nominatedAt"]),
        )


# @dataclass
# class NominatedBeatmaps:
#     beatmap_id: str
#     # mapset_id: str
#     beatmap_title: str
#     beatmap_artist: str
#     mapper: str
#     mapper_id: str
#     description: str
#     tags: str
#     language: str
#     explicit: bool
#     bpm: float | int
#     offset: int
#     preview_time: int
#     duration: float | int
#     rtm_url: str
#     audio_preview_url: str
#     background_urls: list[str]
#     background_image_url: str
#     version: int
#     has_video: bool
#     has_custom_hitsounds: bool
#     rtm_size: int
#     search_text: str
#     search_tokens: list[str]
#     uploaded_by: str
#     uploaded_at: datetime | None
#     download_count: int
#     favorite_count: int
#     # rating: int
#     # rating_count: int
#     # difficulty_play_counts: dict
#     version_history: list[VersionHistory]
#     last_updated_at: datetime | None
#     qualified_by_username: str
#     qualified_date: datetime | None
#     nomination_count: int
#     qualified_by: str
#     nominations: list[Nominator]
#     status: str
#     difficulties: list[CustomDifficulty]
#     play_count: int
#     last_played: datetime | None
#     nominated_at: datetime | None
#
#     @classmethod
#     def from_dict(cls, data: dict):
#         return cls(
#             beatmap_id=data["id"],
#             # mapset_id=data["mapsetId"],
#             beatmap_title=data["songName"],
#             beatmap_artist=data["artistName"],
#             mapper=data["mapper"],
#             mapper_id=data["mapperId"],
#             description=data["description"],
#             tags=data["tags"],
#             language=data["language"],
#             explicit=data["explicit"],
#             bpm=data["bpm"],
#             offset=data["offset"],
#             preview_time=data["previewTime"],
#             duration=data["duration"],
#             rtm_url=data["rtmUrl"],
#             audio_preview_url=data["audioPreviewUrl"],
#             background_urls=data["backgroundUrls"],
#             background_image_url=data["backgroundImageUrl"],
#             version=data["version"],
#             has_video=data["hasVideo"],
#             has_custom_hitsounds=data["hasCustomHitsounds"],
#             rtm_size=data["rtmSize"],
#             search_text=data["searchText"],
#             search_tokens=data["searchTokens"],
#             uploaded_by=data["uploadedBy"],
#             uploaded_at=parse_timestamp(data["uploadedAt"]),
#             download_count=data["downloadCount"],
#             favorite_count=data["favoriteCount"],
#             # rating=data["rating"],
#             # rating_count=data["ratingCount"],
#             # difficulty_play_counts=data["difficultyPlayCounts"],
#             version_history=data["versionHistory"],
#             last_updated_at=parse_timestamp(data["lastUpdatedAt"]),
#             qualified_by_username=data["qualifiedByUsername"],
#             qualified_date=parse_timestamp(data["qualifiedDate"]),
#             nomination_count=data["nominationCount"],
#             qualified_by=data["qualifiedBy"],
#             nominations=data["nominations"],
#             status=data["status"],
#             difficulties=data["difficulties"],
#             play_count=data["playCount"],
#             last_played=parse_timestamp(data["lastPlayed"]),
#             nominated_at=parse_timestamp(data["nominatedAt"]),
#         )


@dataclass
class GlobalLeaderboard:
    rank: int
    user_id: str
    username: str
    pp: float | int
    accuracy: float | int
    play_count: int
    play_time: int
    ranked_score: int
    country: str
    profile_picture_url: str
    rank_change: int
    previous_rank: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            accuracy=data["accuracy"],
            rank=data["rank"],
            pp=data["totalPP"],
            ranked_score=data["rankedScore"],
            user_id=data["userId"],
            previous_rank=data["previousRank"],
            profile_picture_url=data["profilePictureUrl"],
            country=data["country"],
            username=data["username"],
            play_time=data["playTime"],
            rank_change=data["rankChange"],
            play_count=data["playCount"]
        )


@dataclass
class CountryLeaderboard:
    rank: int
    country_code: str
    country_name: str
    total_pp: int
    total_score: int
    total_play_count: int
    player_count: int
    last_updated: datetime | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            last_updated=parse_timestamp(data["lastUpdated"]),
            country_code=data["countryCode"],
            player_count=data["playerCount"],
            total_score=data["totalScore"],
            country_name=data["countryName"],
            total_play_count=data["totalPlayCount"],
            total_pp=data["totalPP"],
            rank=data["rank"]
        )


@dataclass
class TopPlaysLeaderboard:
    rank: int
    score_id: str
    beatmap_id: str
    difficulty_id: str
    username: str
    beatmap_title: str
    beatmap_artist: str
    difficulty_name: str
    pp: float | int
    accuracy: float | int
    score: int
    max_combo: int
    grade: str
    mods: list[str]
    played_at: datetime | None
    user_id: str
    country: str
    profile_picture_url: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rank=data["rank"],
            difficulty_id=data["difficultyId"],
            user_id=data["userId"],
            beatmap_artist=data["beatmapArtist"],
            difficulty_name=data["difficultyName"],
            username=data["username"],
            max_combo=data["maxCombo"],
            country=data["country"],
            mods=data["mods"],
            score_id=data["scoreId"],
            score=data["score"],
            accuracy=data["accuracy"],
            beatmap_title=data["beatmapTitle"],
            pp=data["pp"],
            grade=data["grade"],
            played_at=parse_timestamp(data["playedAt"]),
            beatmap_id=data["beatmapId"],
            profile_picture_url=data["profilePictureUrl"]
        )


@dataclass
class TopScore:
    score_id: str
    user_id: str
    username: str
    pp: float | int
    accuracy: float | int
    score: int
    combo: int
    grade: str
    mods: list[str]
    timestamp: datetime | None
    judgements: Judgements
    replay_id: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            score_id=data["sid"],
            user_id=data["uid"],
            username=data["un"],
            pp=data["pp"],
            accuracy=data["acc"],
            combo=data["cb"],
            grade=data["gr"],
            mods=data["mods"],
            timestamp=parse_timestamp(data["at"]),
            judgements=Judgements.from_dict(data["jc"]),
            replay_id=data["replayId"],
            score=data["sc"]
        )


@dataclass
class BeatmapDifficulty:
    name: str
    star_rating: float | int
    note_count: int
    play_count: int
    top_score: TopScore

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            star_rating=data["starRating"],
            note_count=data["noteCount"],
            play_count=data["playCount"],
            top_score=data["topScore"]
        )


@dataclass
class Judgements:
    perfect: int
    good: int
    ok: int
    miss: int
    caught: int
    catch_miss: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            perfect=data["perfect"],
            good=data["good"],
            ok=data["ok"],
            miss=data["miss"],
            caught=data["caught"],
            catch_miss=data["catch_miss"]
        )


@dataclass
class LeaderboardScore:
    rank: int
    score_id: str
    user_id: str
    username: str
    pp: float | int
    accuracy: float | int
    score: int
    combo: int
    grade: str
    mods: list[str]
    timestamp: datetime | None
    judgements: Judgements
    replay_id: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rank=data["rank"],
            score_id=data["sid"],
            user_id=data["uid"],
            username=data["un"],
            pp=data["pp"],
            accuracy=data["acc"],
            score=data["sc"],
            combo=data["cb"],
            grade=data["gr"],
            mods=data["mods"],
            timestamp=parse_timestamp(data["at"]),
            judgements=Judgements.from_dict(data["jc"]),
            replay_id=data["replayId"]
        )


@dataclass
class Comment:
    comment_id: str
    beatmap_id: str
    user_id: str
    username: str
    profile_picture_url: str
    comment: str
    likes: int
    # liked: bool
    timestamp: datetime | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            comment_id=data["id"],
            beatmap_id=data["beatmapId"],
            user_id=data["uid"],
            username=data["username"],
            profile_picture_url=data["profilePictureUrl"],
            comment=data["comment"],
            likes=data["likes"],
            # liked=data["liked"],
            timestamp=parse_timestamp(data.get("at"))
        )


@dataclass
class UnplayedDifficulty:
    key: str
    beatmap_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty_name: str
    star_rating: float | int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            key=data["key"],
            beatmap_id=data["beatmapId"],
            beatmap_title=data["beatmapTitle"],
            beatmap_artist=data["beatmapArtist"],
            difficulty_name=data["difficultyName"],
            star_rating=data["starRating"]
        )


@dataclass
class UnplayedDifficulties:
    unplayed: list[UnplayedDifficulty]
    count: int
    totalRanked: int
    totalPlayed: int


@dataclass
class BestScore:
    key: str
    beatmap_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty_name: str
    difficulty_id: str
    score: int
    pp: float | int
    accuracy: float | int
    max_combo: int
    grade: str
    best_grade: str
    mods: list[str]
    played_at: datetime | None
    updated_at: datetime | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            key=data["difficultyKey"],
            beatmap_id=data["beatmapId"],
            beatmap_title=data["beatmapTitle"],
            beatmap_artist=data["beatmapArtist"],
            difficulty_name=data["difficultyName"],
            difficulty_id=data["difficultyId"],
            score=data["score"],
            pp=data["pp"],
            accuracy=data["accuracy"],
            max_combo=data["maxCombo"],
            grade=data["grade"],
            best_grade=data["bestGrade"],
            mods=data["mods"],
            played_at=parse_timestamp(data["playedAt"]),
            updated_at=parse_timestamp(data["updatedAt"])
        )


@dataclass
class BestScores:
    scores: list[BestScore]
    count: int


@dataclass
class UserSearchResult:
    user_id: str
    username: str
    display_name: str
    profile_picture: str
    total_pp: float | int
    global_rank: int
    country: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=data["userId"],
            username=data["username"],
            display_name=data["displayName"],
            profile_picture=data["profilePicture"],
            total_pp=data["totalPP"],
            global_rank=data["globalRank"],
            country=data["country"]
        )


class RhythmTyperAPI:
    BASE_URL = "https://api.rhythmtyper.net"

    def _fetch(self, path, **params):
        response = requests.get(
            f"{self.BASE_URL}/{path.lstrip('/')}",
            params=params,
        )
        response.raise_for_status()
        return response.json()

    def get_beatmap(self, mapset_id: str) -> Beatmap:
        """
        Returns given beatmap.
        """
        response = self._fetch(
            "getBeatmaps",
            limit=1,
            mapsetId=mapset_id,
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        song_list = response.get("beatmaps", [])

        if not song_list:
            raise ValueError(f"No beatmap found for mapset ID {mapset_id}")

        song = song_list[0]

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

        return Beatmap.from_dict(song)

    def user_lookup(self, username: str, limit: int = 50) -> list[UserSearchResult]:
        """Returns the users that show up on the search."""
        if len(username) < 2:
            raise ValueError("Username must be at least 2 characters long.")

        response = self._fetch(
            "v2/users/search",
            query=username,
            limit=limit,
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        return [UserSearchResult.from_dict(user) for user in response]

    def get_user_profile(self, user_id: str) -> UserProfile:
        """Return a user's profile."""
        response = self._fetch(f"v2/profile/{user_id}")

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

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
        response = self._fetch(f"v2/user/{user_id}/firstPlaceScores")

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        response["scores"] = [
            Score.from_dict(item)
            for item in response["scores"]
        ]
        return FirstPlaceScores(**response)

    def activity_heatmap(self, user_id: str) -> dict[date, int]:
        """Returns a dictionary containing a date as the key and play count as the value."""
        response = self._fetch(
            f"v2/stats/{user_id}/charts",
            type="heatmap"
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        response = {datetime.strptime(date_str, "%Y-%m-%d").date(): value
                    for date_str, value in response.items()}

        return response

    def get_user_favorites(self, user_id: str) -> list[Beatmap]:
        """Returns all maps a user favorited."""
        response = self._fetch(
            f"getUserFavorites/{user_id}",
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        favorites_list = response.get("favorites", [])
        return [Beatmap.from_dict(fav) for fav in favorites_list]

    def get_most_played_beatmaps(self, user_id: str, limit: int = 50) -> list[MostPlayedBeatmap]:
        """Returns user's most played maps."""
        response = self._fetch(
            f"getMostPlayedBeatmaps/{user_id}",
            limit=limit
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        most_played_list = response.get("mostPlayed", [])
        for song in most_played_list:
            song["lastPlayed"] = parse_timestamp(song.get("lastPlayed"))
        return [MostPlayedBeatmap.from_dict(song) for song in most_played_list]

    def get_user_beatmaps(self, mapper_id: str, cursor: str | None = None, limit: int = 50) -> BeatmapList:
        """
        Returns beatmaps uploaded by a mapper_id.
        """
        response = self._fetch(
            "getBeatmaps",
            mapperId=mapper_id,
            cursor=cursor,
            limit=limit
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

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

    def get_beatmaps(self, limit: int = 50, cursor: str | None = None, status: str = "ranked",
                     sort: str | None = None,
                     explicit: bool = True, language: str = "all") -> BeatmapList:
        """
        Returns beatmaps. \n
        Valid statuses are: "all", "ranked", "loved", "qualified", "nominated", "unranked", "custom".
        """
        response = self._fetch(
            "getBeatmaps",
            limit=limit,
            cursor=cursor,
            status=status,
            sortBy=sort,
            showExplicit=str(explicit).lower(),
            language=language,
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

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
        response = self._fetch(f"getNominatedBeatmaps/{user_id}")

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

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

        response = self._fetch(
            "v2/leaderboard",
            limit=limit,
            offset=offset,
            country=country,
            sortBy=sort
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        return [GlobalLeaderboard.from_dict(item) for item in response]

    def leaderboard_countries(self, limit: int = 50, offset: int = 0, sort: str = "pp") -> list[CountryLeaderboard]:
        """Returns the combined leaderboard of countries. Not to be confused with a country's individual leaderboard."""
        match sort:
            case "pp":
                sort = "totalPP"
            case "score":
                sort = "rankedScore"

        response = self._fetch(
            "v2/leaderboard/countries",
            limit=limit,
            offset=offset,
            sortBy=sort
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        return [CountryLeaderboard.from_dict(item) for item in response["countries"]]

    def leaderboard_top_plays(self, limit: int = 50, offset: int = 0, unique: bool = False) -> list[
        TopPlaysLeaderboard]:
        """Returns the top PP scores leaderboard."""
        response = self._fetch(
            "v2/leaderboard/plays",
            limit=limit,
            offset=offset,
            unique=str(unique).lower()
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        return [TopPlaysLeaderboard.from_dict(item) for item in response["plays"]]

    def get_difficulties(self, beatmap_id: str) -> list[BeatmapDifficulty]:
        """Returns the difficulties for a map."""
        response = self._fetch(f"v2/beatmap/{beatmap_id}/difficulties")

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        return [BeatmapDifficulty.from_dict(item) for item in response]

    def beatmap_leaderboard(self, beatmap_id: str, difficulty: str, limit: int = 50) -> list[LeaderboardScore]:
        """Returns the leaderboards for a beatmap."""
        response = self._fetch(
            f"v2/beatmap/{beatmap_id}/leaderboard",
            difficulty=difficulty,
            limit=limit
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        return [LeaderboardScore.from_dict(item) for item in response]

    def beatmap_comments(self, beatmap_id: str, limit: int = 50) -> list[Comment]:
        """Returns the comments on a mapset."""
        response = self._fetch(
            f"getComments/{beatmap_id}",
            limit=limit
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        comments = response["comments"]
        return [Comment.from_dict(item) for item in comments]

    def unplayed_difficulties(self, user_id: str, limit: int = 100) -> UnplayedDifficulties:
        """Returns all the difficulties a user hasn't played."""
        response = self._fetch(
            f"v2/user/{user_id}/unplayedDifficulties",
            limit=limit
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        response["unplayed"] = [UnplayedDifficulty.from_dict(item) for item in response["unplayed"]]
        return UnplayedDifficulties(**response)

    def user_best_scores(self, user_id: str, limit: int = 100) -> BestScores:
        """Returns the user's best scores by highest Ranked Score."""
        response = self._fetch(
            f"v2/user/{user_id}/bestScores",
            limit=limit
        )

        if find_new_data(response):
            raise RuntimeError("API testing: inspect response above.")

        response["scores"] = [BestScore.from_dict(item) for item in response["scores"]]
        return BestScores(**response)


def find_new_data(data, indent=0, api_testing=False):
    if not api_testing:
        return False

    def type_name(value):
        if isinstance(value, bool):
            return "bool"
        if isinstance(value, int):
            return "int"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "str"
        if value is None:
            return "None"
        if isinstance(value, dict):
            return "dict"
        if isinstance(value, list):
            return "list"
        return type(value).__name__

    def merge_types(values):
        types = {type_name(v) for v in values if v is not None}

        # int + float → float | int
        if "int" in types and "float" in types:
            types.discard("int")
            types.add("float | int")

        return " | ".join(sorted(types)) or "None"

    def walk(value, level):
        prefix = " " * level

        if isinstance(value, dict):
            for key, val in value.items():
                if isinstance(val, list):
                    if not val:
                        print(f"{prefix}{key}: list")
                    elif all(isinstance(x, dict) for x in val):
                        print(f"{prefix}{key}: list[dict]")
                        walk_list_dicts(val, level + 4)
                    else:
                        print(f"{prefix}{key}: list[{merge_types(val)}]")

                elif isinstance(val, dict):
                    print(f"{prefix}{key}: dict")
                    walk(val, level + 4)

                else:
                    print(f"{prefix}{key}: {type_name(val)}")

    def walk_list_dicts(items, level):
        # Collect all keys from every dict in the list
        keys = {}
        for item in items:
            for key, value in item.items():
                keys.setdefault(key, []).append(value)

        prefix = " " * level

        for key, values in keys.items():
            first = next((v for v in values if v is not None), None)

            if isinstance(first, dict):
                print(f"{prefix}{key}: dict")
                walk(first, level + 4)

            elif isinstance(first, list):
                if first and all(isinstance(x, dict) for x in first):
                    print(f"{prefix}{key}: list[dict]")
                    walk_list_dicts(
                        [x for v in values if isinstance(v, list) for x in v],
                        level + 4
                    )
                else:
                    print(f"{prefix}{key}: list[{merge_types(
                        [x for v in values if isinstance(v, list) for x in v]
                    )}]")

            else:
                print(f"{prefix}{key}: {merge_types(values)}")

    if isinstance(data, list):
        if not data:
            print("list")
        elif all(isinstance(x, dict) for x in data):
            print("list[dict]")
            walk_list_dicts(data, indent + 4)
        else:
            print(f"list[{merge_types(data)}]")
    else:
        walk(data, indent)

    return True
