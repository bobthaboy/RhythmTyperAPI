import requests
from dataclasses import dataclass
from datetime import date, datetime, timezone


def parse_timestamp(ts):
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
class RankHistory:
    pp: float
    rank: int
    date: date

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            pp=data.get("pp"),
            rank=data.get("rank"),
            date=datetime.strptime(data.get("date"), "%Y-%m-%d").date()
        )


@dataclass
class RecentPlays:
    score_id: str
    beatmap_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty: str
    pp: float
    acc: float
    score: int
    combo: int
    grade: str
    mods: list[str]
    timestamp: datetime
    perfect: int
    good: int
    ok: int
    misses: int
    star_rating: float
    length: float
    od: int
    bpm: int
    mapper: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            score_id=data.get("sid"),
            beatmap_id=data.get("bid"),
            beatmap_title=data.get("bt"),
            beatmap_artist=data.get("ba"),
            difficulty=data.get("diff"),
            pp=data.get("pp"),
            acc=data.get("acc"),
            score=data.get("sc"),
            combo=data.get("cb"),
            grade=data.get("gr"),
            mods=data.get("mods"),
            timestamp=datetime.fromisoformat(data.get("at").replace("Z", "+00:00")),
            perfect=data.get("pf"),
            good=data.get("gd"),
            ok=data.get("ok"),
            misses=data.get("ms"),
            star_rating=data.get("sr"),
            length=data.get("len"),
            od=data.get("od"),
            bpm=data.get("bpm"),
            mapper=data.get("mn")
        )


@dataclass
class TopPlays:
    score_id: str
    beatmap_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty: str
    pp: float
    acc: float
    score: int
    combo: int
    grade: str
    mods: list[str]
    timestamp: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            score_id=data.get("sid"),
            beatmap_id=data.get("bid"),
            beatmap_title=data.get("bt"),
            beatmap_artist=data.get("ba"),
            difficulty=data.get("diff"),
            pp=data.get("pp"),
            acc=data.get("acc"),
            score=data.get("sc"),
            combo=data.get("cb"),
            grade=data.get("gr"),
            mods=data.get("mods"),
            timestamp=datetime.fromisoformat(data.get("at").replace("Z", "+00:00")),
        )


@dataclass
class RecentActivity:
    type: str
    beatmap_id: str
    difficulty: str
    beatmap_title: str
    beatmap_artist: str
    taken_by_user_id: str
    taken_by_username: str
    timestamp: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            type=data.get("type"),
            beatmap_id=data.get("beatmapId"),
            difficulty=data.get("difficultyName"),
            beatmap_title=data.get("beatmapTitle"),
            beatmap_artist=data.get("beatmapArtist"),
            taken_by_user_id=data.get("takenByUserId"),
            taken_by_username=data.get("takenByUsername"),
            timestamp=datetime.fromisoformat(data.get("timestamp").replace("Z", "+00:00")),
        )


@dataclass
class UserProfile:
    user_id: str
    username: str
    # total_plays: int
    # level: int
    # experience: int
    # total_play_time: int
    country: str
    created_at: datetime
    # recent_plays_format: str
    # top_plays_format: str
    profile_picture_url: str
    profile_picture_version: str
    profile_picture_updated_at: datetime
    # username_lower: str
    top_plays_count: int
    last_pp_recalculation: datetime
    last_ranked_score_recalculation: datetime
    rank_history: list[RankHistory]
    last_top_plays_update: datetime
    last_updated: datetime
    raw_pp: float
    global_rank: int
    country_rank: int
    pp: float
    play_count: int
    accuracy: float
    # total_pp: float
    play_time: int
    grades: Grades
    recent_plays: list[RecentPlays]
    ranked_score: int
    total_score: int
    top_plays: list[TopPlays]
    play_heatmap: dict
    recent_activity: list[RecentActivity]
    # top_plays_expanded: list[TopPlays]
    profile_description: str
    follower_count: int
    following_count: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=data.get("userId"),
            username=data.get("username"),
            # total_plays=data.get("totalPlays"),
            # level=data.get("level"),
            # experience=data.get("experience"),
            # total_play_time=data.get("totalPlaytime"),
            country=data.get("country"),
            created_at=data.get("createdAt"),
            # recent_plays_format=data.get("recentPlaysFormat"),
            # top_plays_format=data.get("topPlaysFormat"),
            profile_picture_url=data.get("profilePictureUrl"),
            profile_picture_version=data.get("profilePictureVersion"),
            profile_picture_updated_at=data.get("profilePictureUpdatedAt"),
            # username_lower=data.get("usernameLower"),
            top_plays_count=data.get("topPlaysCount"),
            last_pp_recalculation=data.get("lastPPRecalculation"),
            last_ranked_score_recalculation=data.get("lastRankedScoreRecalculation"),
            rank_history=data.get("rankHistory"),
            last_top_plays_update=data.get("lastTopPlaysUpdate"),
            last_updated=data.get("lastUpdated"),
            raw_pp=data.get("rawPP"),
            global_rank=data.get("globalRank"),
            country_rank=data.get("countryRank"),
            pp=data.get("pp"),
            play_count=data.get("playCount"),
            accuracy=data.get("accuracy"),
            # total_pp=data.get("totalPP"),
            play_time=data.get("playTime"),
            grades=data.get("grades"),
            recent_plays=data.get("recentPlays"),
            ranked_score=data.get("rankedScore"),
            total_score=data.get("totalScore"),
            top_plays=data.get("topPlays"),
            play_heatmap=data.get("playHeatmap"),
            recent_activity=data.get("recentActivity"),
            # top_plays_expanded=data.get("topPlaysExpanded"),
            profile_description=data.get("profileDescription"),
            follower_count=data.get("followerCount"),
            following_count=data.get("followingCount")
        )


@dataclass
class Scores:
    score_id: str
    beatmap_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty: str
    acc: float
    pp: float
    score: int
    timestamp: datetime
    mods: list[str]
    combo: int
    grade: str
    tied_for_first: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            score_id=data.get("sid"),
            beatmap_id=data.get("bid"),
            beatmap_title=data.get("bt"),
            beatmap_artist=data.get("ba"),
            difficulty=data.get("diff"),
            acc=data.get("acc"),
            pp=data.get("pp"),
            score=data.get("score"),
            timestamp=datetime.fromisoformat(data.get("at").replace("Z", "+00:00")),
            mods=data.get("mods"),
            combo=data.get("cb"),
            grade=data.get("gr"),
            tied_for_first=data.get("isTiedFor1st"),
        )


@dataclass
class FirstPlaceScores:
    scores: list[Scores]
    count: int


@dataclass
class Favorites:
    beatmap_id: str
    beatmap_title: str
    beatmap_artist: str
    mapper: str
    background_image_url: str
    background_urls: list[str]
    status: str
    ranked: bool
    play_count: int
    favorite_count: int
    difficulties: list
    difficulty_count: int
    explicit: bool
    language: str
    nomination_count: int
    rtm_url: str
    uploaded_at: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            beatmap_id=data.get("mapsetId"),
            beatmap_title=data.get("songName"),
            beatmap_artist=data.get("artistName"),
            mapper=data.get("mapper"),
            background_image_url=data.get("backgroundImageUrl"),
            background_urls=data.get("backgroundUrls"),
            status=data.get("status"),
            ranked=data.get("ranked"),
            play_count=data.get("playCount"),
            favorite_count=data.get("favoriteCount"),
            difficulties=data.get("difficulties"),
            difficulty_count=data.get("difficultyCount"),
            explicit=data.get("explicit"),
            language=data.get("language"),
            nomination_count=data.get("nominationCount"),
            rtm_url=data.get("rtmUrl"),
            uploaded_at=datetime.fromisoformat(data.get("uploadedAt").replace("Z", "+00:00")),
        )


@dataclass
class MostPlayed:
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
            beatmap_id=data.get("beatmapId"),
            # mapset_id=data.get("mapsetId"),
            beatmap_artist=data.get("artist"),
            beatmap_title=data.get("title"),
            difficulty=data.get("difficultyName"),
            background_image_url=data.get("backgroundImageUrl"),
            play_count=data.get("status"),
            last_played=data.get("lastPlayed")
        )


@dataclass
class CustomDifficulty:
    beatmap_id: str
    difficulty_name: str
    od: int
    star_rating: int
    star_rating_dt: int
    od_dt: float
    star_rating_ht: int
    od_ht: float
    tap_count: int
    catch_count: int
    hold_count: int
    typing_count: int
    length: float

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            beatmap_id=data.get("diffId"),
            difficulty_name=data.get("name"),
            od=data.get("overallDifficulty"),
            star_rating=data.get("starRating"),
            star_rating_dt=data.get("starRatingNC"),
            od_dt=data.get("overallDifficultyNC"),
            star_rating_ht=data.get("starRatingHT"),
            od_ht=data.get("overallDifficultyHT"),
            tap_count=data.get("tapCount"),
            catch_count=data.get("catchCount"),
            hold_count=data.get("holdCount"),
            typing_count=data.get("typingCount"),
            length=data.get("length")
        )


@dataclass
class VersionHistory:
    version: int
    type: str
    timestamp: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            version=data.get("version"),
            type=data.get("type"),
            timestamp=parse_timestamp(data.get("timestamp")),
        )


@dataclass
class BeatmapsExtended:
    beatmap_id: str
    # mapset_id: str
    beatmap_title: str
    beatmap_artist: str
    mapper: str
    mapper_id: str
    description: str
    tags: list[str]
    language: str
    explicit: bool
    bpm: int
    offset: int
    preview_time: int
    duration: float
    rtm_url: str
    audio_preview_url: str
    background_urls: list[str]
    background_image_url: str
    version: int
    has_video: bool
    has_custom_hitsounds: bool
    rtm_size: int
    search_text: str
    search_tokens: list[str]
    # uploaded_by: str
    download_count: int
    status: str
    # rating: int
    # rating_count: int
    # difficulty_play_counts: dict
    version_history: list[VersionHistory]
    last_updated: datetime
    uploaded_at: datetime
    favorite_count: int
    difficulties: list[CustomDifficulty]
    play_count: int
    last_played: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            beatmap_id=data.get("id"),
            # mapset_id=data.get("mapsetId"),
            beatmap_title=data.get("songName"),
            beatmap_artist=data.get("artistName"),
            mapper=data.get("mapper"),
            mapper_id=data.get("mapperId"),
            description=data.get("description"),
            tags=data.get("tags"),
            language=data.get("language"),
            explicit=data.get("explicit"),
            bpm=data.get("bpm"),
            offset=data.get("offset"),
            preview_time=data.get("previewTime"),
            duration=data.get("duration"),
            rtm_url=data.get("rtmUrl"),
            audio_preview_url=data.get("audioPreviewUrl"),
            background_urls=data.get("backgroundUrls"),
            background_image_url=data.get("backgroundImageUrl"),
            version=data.get("version"),
            has_video=data.get("hasVideo"),
            has_custom_hitsounds=data.get("hasCustomHitsounds"),
            rtm_size=data.get("rtmSize"),
            search_text=data.get("searchText"),
            search_tokens=data.get("searchTokens"),
            # uploaded_by=data.get("uploadedBy"),
            download_count=data.get("downloadCount"),
            status=data.get("status"),
            # rating=data.get("rating"),
            # rating_count=data.get("ratingCount"),
            # difficulty_play_counts=data.get("difficultyPlayCounts"),
            version_history=data.get("versionHistory"),
            last_updated=data.get("lastUpdatedAt"),
            uploaded_at=datetime.fromisoformat(data.get("uploadedAt").replace("Z", "+00:00")),
            favorite_count=data.get("favoriteCount"),
            difficulties=data.get("difficulties"),
            play_count=data.get("playCount"),
            last_played=data.get("lastPlayed")
        )


@dataclass
class UserBeatmaps:
    beatmaps: list[BeatmapsExtended]
    has_more: bool
    next_cursor: str
    limit: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            beatmaps=[BeatmapsExtended.from_dict(b) for b in data["beatmaps"]],
            has_more=data["hasMore"],
            next_cursor=data["nextCursor"],
            limit=data["limit"]
        )


@dataclass
class Nominator:
    nominator_id: str
    nominator_username: str
    nominated_at: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nominator_id=data.get("nominatorId"),
            nominator_username=data.get("nominatorUsername"),
            nominated_at=parse_timestamp(data.get("nominatedAt")),
        )


@dataclass
class NominatedBeatmaps:
    beatmap_id: str
    # mapset_id: str
    beatmap_title: str
    beatmap_artist: str
    mapper: str
    mapper_id: str
    description: str
    tags: str
    language: str
    explicit: bool
    bpm: float
    offset: int
    preview_time: int
    duration: float
    rtm_url: str
    audio_preview_url: str
    background_urls: list[str]
    background_image_url: str
    version: int
    has_video: bool
    has_custom_hitsounds: bool
    rtm_size: int
    search_text: str
    search_tokens: list[str]
    uploaded_by: str
    uploaded_at: datetime
    download_count: int
    favorite_count: int
    # rating: int
    # rating_count: int
    # difficulty_play_counts: dict
    version_history: list[VersionHistory]
    last_updated_at: datetime
    qualified_by_username: str
    qualified_date: datetime
    nomination_count: int
    qualified_by: str
    nominations: list[Nominator]
    status: str
    difficulties: list[CustomDifficulty]
    play_count: int
    last_played: datetime
    nominated_at: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            beatmap_id=data.get("id"),
            # mapset_id=data.get("mapsetId"),
            beatmap_title=data.get("songName"),
            beatmap_artist=data.get("artistName"),
            mapper=data.get("mapper"),
            mapper_id=data.get("mapperId"),
            description=data.get("description"),
            tags=data.get("tags"),
            language=data.get("language"),
            explicit=data.get("explicit"),
            bpm=data.get("bpm"),
            offset=data.get("offset"),
            preview_time=data.get("previewTime"),
            duration=data.get("duration"),
            rtm_url=data.get("rtmUrl"),
            audio_preview_url=data.get("audioPreviewUrl"),
            background_urls=data.get("backgroundUrls"),
            background_image_url=data.get("backgroundImageUrl"),
            version=data.get("version"),
            has_video=data.get("hasVideo"),
            has_custom_hitsounds=data.get("hasCustomHitsounds"),
            rtm_size=data.get("rtmSize"),
            search_text=data.get("searchText"),
            search_tokens=data.get("searchTokens"),
            uploaded_by=data.get("uploadedBy"),
            uploaded_at=parse_timestamp(data.get("uploadedAt")),
            download_count=data.get("downloadCount"),
            favorite_count=data.get("favoriteCount"),
            # rating=data.get("rating"),
            # rating_count=data.get("ratingCount"),
            # difficulty_play_counts=data.get("difficultyPlayCounts"),
            version_history=data.get("versionHistory"),
            last_updated_at=parse_timestamp(data.get("lastUpdatedAt")),
            qualified_by_username=data.get("qualifiedByUsername"),
            qualified_date=parse_timestamp(data.get("qualifiedDate")),
            nomination_count=data.get("nominationCount"),
            qualified_by=data.get("qualifiedBy"),
            nominations=data.get("nominations"),
            status=data.get("status"),
            difficulties=data.get("difficulties"),
            play_count=data.get("playCount"),
            last_played=parse_timestamp(data.get("lastPlayed")),
            nominated_at=parse_timestamp(data.get("nominatedAt")),
        )


@dataclass
class GlobalLeaderboard:
    accuracy: float
    rank: int
    pp: float
    ranked_score: int
    user_id: str
    previous_rank: int
    profile_picture_url: str
    country: str
    username: str
    play_time: int
    rank_change: int
    play_count: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            accuracy=data.get("accuracy"),
            rank=data.get("rank"),
            pp=data.get("totalPP"),
            ranked_score=data.get("rankedScore"),
            user_id=data.get("userId"),
            previous_rank=data.get("previousRank"),
            profile_picture_url=data.get("profilePictureUrl"),
            country=data.get("country"),
            username=data.get("username"),
            play_time=data.get("playTime"),
            rank_change=data.get("rankChange"),
            play_count=data.get("playCount")
        )


@dataclass
class CountryLeaderboard:
    last_updated: datetime
    country_code: str
    players_count: int
    total_score: int
    country_name: str
    total_play_count: int
    total_pp: int
    rank: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            last_updated=parse_timestamp(data.get("lastUpdated")),
            country_code=data.get("countryCode"),
            players_count=data.get("playerCount"),
            total_score=data.get("totalScore"),
            country_name=data.get("countryName"),
            total_play_count=data.get("totalPlayCount"),
            total_pp=data.get("totalPP"),
            rank=data.get("rank")
        )


@dataclass
class TopPlaysLeaderboard:
    rank: int
    difficulty_id: str
    user_id: str
    beatmap_artist: str
    difficulty_name: str
    username: str
    max_combo: int
    country: str
    mods: list[str]
    score_id: str
    score: int
    accuracy: float
    beatmap_title: str
    pp: float
    grade: str
    played_at: datetime
    beatmap_id: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rank=data.get("rank"),
            difficulty_id=data.get("difficultyId"),
            user_id=data.get("userId"),
            beatmap_artist=data.get("beatmapArtist"),
            difficulty_name=data.get("difficultyName"),
            username=data.get("username"),
            max_combo=data.get("maxCombo"),
            country=data.get("country"),
            mods=data.get("mods"),
            score_id=data.get("scoreId"),
            score=data.get("score"),
            accuracy=data.get("accuracy"),
            beatmap_title=data.get("beatmapTitle"),
            pp=data.get("pp"),
            grade=data.get("grade"),
            played_at=parse_timestamp(data.get("playedAt")),
            beatmap_id=data.get("beatmapId")
        )


@dataclass
class TopScore:
    score_id: str
    user_id: str
    username: str
    pp: float
    accuracy: float
    # sc: int
    combo: int
    grade: str
    mods: list[str]
    timestamp: datetime
    perfect: int
    good: int
    ok: int
    miss: int
    replay_id: str
    score: int

    # max_combo: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            score_id=data.get("sid"),
            user_id=data.get("uid"),
            username=data.get("un"),
            pp=data.get("pp"),
            accuracy=data.get("acc"),
            # sc=data.get("sc"),
            combo=data.get("cb"),
            grade=data.get("gr"),
            mods=data.get("mods"),
            timestamp=parse_timestamp(data.get("at")),
            perfect=data.get("jc", {}).get("perfect"),
            good=data.get("jc", {}).get("good"),
            ok=data.get("jc", {}).get("ok"),
            miss=data.get("jc", {}).get("miss"),
            replay_id=data.get("replayId"),
            score=data.get("score")
            # max_combo=data.get("maxCombo")
        )


@dataclass
class Difficulty:
    name: str
    star_rating: float
    note_count: int
    play_count: int
    top_score: TopScore

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            star_rating=data.get("starRating"),
            note_count=data.get("noteCount"),
            play_count=data.get("playCount"),
            top_score=data.get("topScore")
        )


@dataclass
class BeatmapLeaderboard:
    rank: str
    score_id: str
    user_id: str
    username: str
    pp: float
    accuracy: float
    score: int
    combo: int
    grade: str
    mods: list[str]
    timestamp: datetime
    perfect: int
    good: int
    ok: int
    miss: int
    replay_id: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rank=data.get("rank"),
            score_id=data.get("sid"),
            user_id=data.get("uid"),
            username=data.get("un"),
            pp=data.get("pp"),
            accuracy=data.get("acc"),
            score=data.get("sc"),
            combo=data.get("cb"),
            grade=data.get("gr"),
            mods=data.get("mods"),
            timestamp=parse_timestamp(data.get("at")),
            perfect=data.get("jc", {}).get("perfect"),
            good=data.get("jc", {}).get("good"),
            ok=data.get("jc", {}).get("ok"),
            miss=data.get("jc", {}).get("miss"),
            replay_id=data.get("replayId")
        )


@dataclass
class Comments:
    comment_id: str
    beatmap_id: str
    user_id: str
    username: str
    profile_picture_url: str
    comment: str
    likes: int
    timestamp: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            comment_id=data.get("id"),
            beatmap_id=data.get("beatmapId"),
            user_id=data.get("uid"),
            username=data.get("username"),
            profile_picture_url=data.get("profilePictureUrl"),
            comment=data.get("gr"),
            likes=int(data.get("likes")),
            timestamp=parse_timestamp(data.get("at"))
        )


@dataclass
class Unplayed:
    key: str
    beatmap_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty_name: str
    star_rating: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            key=data.get("key"),
            beatmap_id=data.get("beatmapId"),
            beatmap_title=data.get("beatmapTitle"),
            beatmap_artist=data.get("beatmapArtist"),
            difficulty_name=data.get("difficultyName"),
            star_rating=data.get("starRating")
        )


@dataclass
class UnplayedDifficulties:
    unplayed: list[Unplayed]
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
    pp: float
    accuracy: float
    max_combo: int
    grade: str
    best_grade: str
    mods: list[str]
    played_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            key=data.get("difficultyKey"),
            beatmap_id=data.get("beatmapId"),
            beatmap_title=data.get("beatmapTitle"),
            beatmap_artist=data.get("beatmapArtist"),
            difficulty_name=data.get("difficultyName"),
            difficulty_id=data.get("difficultyId"),
            score=int(data.get("score")),
            pp=float(data.get("pp")),
            accuracy=float(data.get("accuracy")),
            max_combo=int(data.get("maxCombo")),
            grade=data.get("grade"),
            best_grade=data.get("bestGrade"),
            mods=data.get("mods"),
            played_at=parse_timestamp(data.get("playedAt")),
            updated_at=parse_timestamp(data.get("updatedAt"))
        )


@dataclass
class BestScores:
    scores: list[BestScore]
    count: int


class RhythmTyperAPI:
    def _fetch(self, url):
        response = requests.get(url)
        return response.json()

    def get_user_profile(self, user_id: str) -> UserProfile:
        """Return a user's profile."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/profile/{user_id}"
        response = self._fetch(url)

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
            RankHistory.from_dict(item)
            for item in response["rankHistory"]
        ]
        response["recentPlays"] = [
            RecentPlays.from_dict(item)
            for item in response["recentPlays"]
        ]
        response["topPlays"] = [
            TopPlays.from_dict(item)
            for item in response["topPlays"]
        ]
        response["topPlaysExpanded"] = [
            TopPlays.from_dict(item)
            for item in response["topPlaysExpanded"]
        ]
        response.setdefault("recentActivity", {})
        response["recentActivity"] = [
            RecentActivity.from_dict(item)
            for item in response["recentActivity"]
        ]
        return UserProfile.from_dict(response)

    def first_place_scores(self, user_id: str) -> FirstPlaceScores:
        """Returns all the first place scores of a user."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/user/{user_id}/firstPlaceScores"
        response = self._fetch(url)
        response["scores"] = [
            Scores.from_dict(item)
            for item in response["scores"]
        ]
        return FirstPlaceScores(**response)

    def activity_heatmap(self, user_id: str) -> dict:
        """Returns a dictionary containing a date as the key and play count as the value."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/stats/{user_id}/charts?type=heatmap"
        response = self._fetch(url)
        response = {datetime.strptime(date_str, "%Y-%m-%d").date(): value
                    for date_str, value in response.items()}
        return response

    def get_user_favorites(self, user_id: str) -> list[Favorites]:
        """Returns all maps a user favorited."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/getUserFavorites/{user_id}"
        response = self._fetch(url)
        favorites_list = response.get("favorites", [])
        return [Favorites.from_dict(fav) for fav in favorites_list]

    def get_most_played_beatmaps(self, user_id: str, limit: int = 50) -> list[MostPlayed]:
        """Returns user's most played maps."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/getMostPlayedBeatmaps/{user_id}?limit={limit}"
        response = self._fetch(url)
        most_played_list = response.get("mostPlayed", [])
        for song in most_played_list:
            song["lastPlayed"] = parse_timestamp(response.get("lastPlayed"))
        return [MostPlayed.from_dict(song) for song in most_played_list]

    def get_beatmaps(self, mapper_id: str = None, limit: int = 50, cursor: str = None, status: str = "ranked",
                     sort: str = None,
                     explicit: bool = True, language: str = "all") -> UserBeatmaps:
        """
        Returns beatmaps. Accepts mapper_id. \n
        Valid statuses are: "all", "ranked", "loved", "qualified", "nominated", "unranked", "custom".
        """

        if mapper_id:
            mapper_id = "?mapperId=" + mapper_id
        else:
            mapper_id = ""
        if cursor:
            cursor = "&cursor=" + cursor
        else:
            cursor = ""
        if status:
            status = "&status=" + status
        else:
            status = ""
        if sort:
            sort = "&sortBy=" + sort
        else:
            sort = ""
        explicit = f"&showExplicit={str(explicit).lower()}"
        language = "&language=" + language

        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/getBeatmaps{mapper_id}?limit={limit}{cursor}{status}{sort}{explicit}{language}"
        response = self._fetch(url)

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

        return UserBeatmaps.from_dict(response)

    def get_nominations(self, user_id: str) -> list[NominatedBeatmaps]:
        """Returns user's nominations."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/getNominatedBeatmaps/{user_id}"
        response = self._fetch(url)
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

        return [NominatedBeatmaps.from_dict(song) for song in song_list]

    def leaderboard_global(self, limit: int = 50, offset: int = 0, country: str = None, sort: str = "pp") -> list[
        GlobalLeaderboard]:
        """
        Returns global leaderboards. Accepts country. \n
        Valid sorts are: "pp", "score".
        """
        if country:
            country = "&country=" + country
        else:
            country = ""

        match sort:
            case "pp":
                sort = "totalPP"
            case "score":
                sort = "rankedScore"

        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/leaderboard?limit={limit}&offset={offset}{country}&sortBy={sort}"
        response = self._fetch(url)
        return [GlobalLeaderboard.from_dict(item) for item in response]

    def leaderboard_countries(self, limit: int = 50, offset: int = 0, sort: str = "pp") -> list[CountryLeaderboard]:
        """Returns the combined leaderboard of countries. Not to be confused with a country's individual leaderboard."""
        match sort:
            case "pp":
                sort = "totalPP"
            case "score":
                sort = "rankedScore"

        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/leaderboard/countries?limit={limit}&offset={offset}&sortBy={sort}"
        response = self._fetch(url)
        return [CountryLeaderboard.from_dict(item) for item in response["countries"]]

    def leaderboard_top_plays(self, limit: int = 50, offset: int = 0, unique: bool = None) -> list[TopPlaysLeaderboard]:
        """Returns the top PP scores leaderboard."""
        if unique is not None:
            unique = f"&unique={str(unique).lower()}"
        else:
            unique = ""

        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/leaderboard/plays?limit={limit}&offset={offset}{unique}"
        response = self._fetch(url)
        return [TopPlaysLeaderboard.from_dict(item) for item in response["plays"]]

    def get_difficulties(self, beatmap_id: str) -> list[Difficulty]:
        """Returns the difficulties for a map."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/beatmap/{beatmap_id}/difficulties"
        response = self._fetch(url)
        return [Difficulty.from_dict(item) for item in response]

    def beatmap_leaderboard(self, beatmap_id: str, difficulty: str, limit: int = 50) -> list[BeatmapLeaderboard]:
        """Returns the leaderboards for a beatmap."""
        difficulty = difficulty.replace("+", "%2B")
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/beatmap/{beatmap_id}/leaderboard?difficulty={difficulty}&limit={limit}"
        response = self._fetch(url)
        return [BeatmapLeaderboard.from_dict(item) for item in response]

    def beatmap_comments(self, beatmap_id: str, limit: int = 50) -> list[Comments]:
        """Returns the comments on a mapset."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/getComments/{beatmap_id}?limit={limit}"
        response = self._fetch(url)
        comments = response["comments"]
        return [Comments.from_dict(item) for item in comments]

    def unplayed_difficulties(self, user_id: str, limit: int = 100) -> UnplayedDifficulties:
        """Returns all the difficulties a user hasn't played."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/user/{user_id}/unplayedDifficulties?limit={limit}"
        response = self._fetch(url)
        response["unplayed"] = [Unplayed.from_dict(item) for item in response["unplayed"]]
        return UnplayedDifficulties(**response)

    def user_best_scores(self, user_id: str, limit: int = 100) -> BestScores:
        """Returns the user's best scores by highest Ranked Score."""
        url = f"https://us-central1-rhythm-typer.cloudfunctions.net/api/v2/user/{user_id}/bestScores?limit={limit}"
        response = self._fetch(url)
        response["scores"] = [BestScore.from_dict(item) for item in response["scores"]]
        return BestScores(**response)

# # CODE GOES HERE

# for attr, value in vars(me[0]).items():
#     print(f"{attr}: {value}")
