from dataclasses import dataclass
from datetime import date, datetime
from .helper import parse_timestamp


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
            date=datetime.strptime(data["date"], "%Y-%m-%d").date(),
            rank=data["rank"],
            pp=data["pp"]
        )


@dataclass
class Play:
    score_id: str
    mapset_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty_name: str
    pp: float | int
    acc: float | int
    score: int
    combo: int
    grade: str
    mods: list[str]
    timestamp: datetime
    judgements: Judgements

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            score_id=data["sid"],
            mapset_id=data["bid"],
            beatmap_title=data["bt"],
            beatmap_artist=data["ba"],
            difficulty_name=data["diff"],
            pp=data["pp"],
            acc=data["acc"],
            score=data["sc"],
            combo=data["cb"],
            grade=data["gr"],
            mods=data["mods"],
            timestamp=datetime.fromisoformat(data["at"].replace("Z", "+00:00")),
            judgements=Judgements.from_dict(data["judgments"])
        )


@dataclass
class RecentActivity:
    type: str
    version: int | None
    mapset_id: str
    timestamp: datetime
    beatmap_title: str
    beatmap_artist: str
    taken_by_user_id: str | None
    difficulty_name: str | None
    taken_by_username: str | None
    pp: float | int | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            type=data["type"],
            version=data.get("version"),
            mapset_id=data["beatmapId"],
            timestamp=datetime.fromisoformat(data["timestamp"].replace("Z", "+00:00")),
            beatmap_title=data["beatmapTitle"],
            beatmap_artist=data["beatmapArtist"],
            taken_by_user_id=data.get("takenByUserId"),
            difficulty_name=data.get("difficultyName"),
            taken_by_username=data.get("takenByUsername"),
            pp=data.get("pp")
        )


@dataclass
class UserProfile:
    user_id: str
    username: str
    country: str
    region: str | None
    pp: float | int
    acc: float | int
    play_count: int
    ranked_score: int
    play_time: int
    grades: Grades
    recent_activity: list[RecentActivity]
    rank_history: list[RankHistoryEntry]
    top_plays: list[Play]
    recent_plays: list[Play]
    profile_description: str
    follower_count: int
    profile_picture_url: str
    global_rank: int
    country_rank: int
    created_at: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=data["userId"],
            username=data["username"],
            country=data["country"],
            region=data["region"],
            pp=data["totalPP"],
            acc=data["accuracy"],
            play_count=data["playCount"],
            ranked_score=data["rankedScore"],
            play_time=data["playTime"],
            grades=data["grades"],
            recent_activity=data["recentActivity"],
            rank_history=data["rankHistory"],
            top_plays=data["topPlays"],
            recent_plays=data["recentPlays"],
            profile_description=data["profileDescription"],
            follower_count=data["followerCount"],
            profile_picture_url=data["profilePictureUrl"],
            global_rank=data["globalRank"],
            country_rank=data["countryRank"],
            created_at=data["createdAt"]
        )


@dataclass
class Score:
    rank: int | None
    score_id: str
    user_id: str
    username: str
    pp: float | int
    acc: float | int
    score: int
    combo: int
    grade: str
    mods: list[str]
    timestamp: datetime
    judgements: Judgements
    replay_id: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rank=data.get("rank"),
            score_id=data["sid"],
            user_id=data["uid"],
            username=data["username"],
            pp=data["pp"],
            acc=data["acc"],
            score=data["sc"],
            combo=data["cb"],
            grade=data["gr"],
            mods=data["mods"],
            timestamp=datetime.fromisoformat(data["at"].replace("Z", "+00:00")),
            judgements=Judgements.from_dict(data["judgments"]),
            replay_id=data["replayId"]
        )


@dataclass
class FirstPlaceScore:
    score_id: str
    mapset_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty_name: str
    acc: float | int
    pp: float | int
    score: int
    timestamp: datetime
    mods: list[str]
    combo: int
    grade: str
    judgements: Judgements
    tied_for_first: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            score_id=data["sid"],
            mapset_id=data["bid"],
            beatmap_title=data["bt"],
            beatmap_artist=data["ba"],
            difficulty_name=data["diff"],
            acc=data["acc"],
            pp=data["pp"],
            score=data["score"],
            timestamp=datetime.fromisoformat(data["at"].replace("Z", "+00:00")),
            mods=data["mods"],
            combo=data["cb"],
            grade=data["gr"],
            judgements=Judgements.from_dict(data["judgments"]),
            tied_for_first=data["isTiedFor1st"]
        )


@dataclass
class MostPlayedBeatmap:
    mapset_id: str
    beatmap_artist: str
    beatmap_title: str
    difficulty_name: str
    background_image_url: str
    play_count: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            mapset_id=data["mapsetId"],
            beatmap_artist=data["artist"],
            beatmap_title=data["title"],
            difficulty_name=data["difficultyName"],
            background_image_url=data["backgroundImageUrl"],
            play_count=data["playCount"]
        )


@dataclass
class Difficulty:
    difficulty_id: str
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
            difficulty_id=data["diffId"],
            difficulty_name=data["name"],
            star_rating=data["starRating"],
            star_rating_dt=data["starRatingNC"],
            star_rating_ht=data["starRatingHT"],
            od=data["overallDifficulty"],
            od_dt=data["overallDifficultyNC"],
            od_ht=data["overallDifficultyHT"],
            note_count=data["noteCount"],
            tap_count=data["tapCount"],
            catch_count=data["catchCount"],
            hold_count=data["holdCount"],
            typing_count=data["typingCount"],
            length=data["length"]
        )


@dataclass
class VersionHistory:
    type: str
    version: int
    timestamp: datetime | None
    patch_notes: str | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            type=data["type"],
            version=data["version"],
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
    version: int
    play_count: int
    favorite_count: int
    nomination_count: int
    version_history: list[VersionHistory]
    nominations: list[BeatmapNominator]
    difficulty_play_counts: dict
    uploaded_at: datetime
    ranked_date: datetime | None
    qualified_date: datetime | None
    nominated_at: datetime | None
    difficulties: list[Difficulty]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            mapset_id=data["mapsetId"],
            beatmap_title=data["songName"],
            beatmap_artist=data["artistName"],
            mapper=data["mapper"],
            mapper_id=data["mapperId"],
            bpm=data["bpm"],
            duration=data["duration"],
            offset=data["offset"],
            preview_time=data["previewTime"],
            status=data["status"],
            ranked=data["ranked"],
            description=data["description"],
            tags=data["tags"],
            language=data["language"],
            explicit=data["explicit"],
            has_video=data["hasVideo"],
            has_custom_hitsounds=data["hasCustomHitsounds"],
            audio_preview_url=data["audioPreviewUrl"],
            background_image_url=data["backgroundImageUrl"],
            background_urls=data["backgroundUrls"],
            rtm_url=data["rtmUrl"],
            version=data["version"],
            play_count=data["playCount"],
            favorite_count=data["favoriteCount"],
            nomination_count=data["nominationCount"],
            version_history=data["versionHistory"],
            nominations=[
                BeatmapNominator.from_dict(item)
                for item in data.get("nominations", [])
            ],
            difficulty_play_counts=data["difficultyPlayCounts"],
            uploaded_at=datetime.fromisoformat(data["uploadedAt"].replace("Z", "+00:00")),
            ranked_date=parse_timestamp(data.get("rankedDate")),
            qualified_date=parse_timestamp(data.get("qualifiedDate")),
            nominated_at=data.get("nominatedAt"),
            difficulties=data["difficulties"]
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
class BeatmapNominator:
    nominator_id: str
    nominator_username: str
    nominated_at: datetime | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nominator_id=data["nominatorId"],
            nominator_username=data["nominatorUsername"],
            nominated_at=parse_timestamp(data.get("nominatedAt")),
        )


@dataclass
class GlobalLeaderboard:
    rank: int
    user_id: str
    username: str
    pp: float | int
    acc: float | int
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
            rank=data["rank"],
            user_id=data["userId"],
            username=data["username"],
            pp=data["totalPP"],
            acc=data["accuracy"],
            play_count=data["playCount"],
            play_time=data["playTime"],
            ranked_score=data["rankedScore"],
            country=data["country"],
            profile_picture_url=data["profilePictureUrl"],
            rank_change=data["rankChange"],
            previous_rank=data["previousRank"]
        )


@dataclass
class CountryLeaderboard:
    rank: int
    country_code: str
    total_pp: int
    total_score: int
    total_play_count: int
    player_count: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rank=data["rank"],
            country_code=data["countryCode"],
            total_pp=data["totalPP"],
            total_score=data["totalScore"],
            total_play_count=data["totalPlayCount"],
            player_count=data["playerCount"]
        )


@dataclass
class TopPlaysLeaderboard:
    rank: int
    score_id: str
    mapset_id: str
    difficulty_id: str
    username: str
    beatmap_title: str
    beatmap_artist: str
    difficulty_name: str
    pp: float | int
    acc: float | int
    max_combo: int
    mods: list[str]
    played_at: datetime | None
    user_id: str
    country: str
    profile_picture_url: str
    judgements: Judgements

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rank=data["rank"],
            score_id=data["scoreId"],
            mapset_id=data["beatmapId"],
            difficulty_id=data["difficultyId"],
            username=data["username"],
            beatmap_title=data["beatmapTitle"],
            beatmap_artist=data["beatmapArtist"],
            difficulty_name=data["difficultyName"],
            pp=data["pp"],
            acc=data["accuracy"],
            max_combo=data["maxCombo"],
            mods=data["mods"],
            played_at=parse_timestamp(data["playedAt"]),
            user_id=data["userId"],
            country=data["country"],
            profile_picture_url=data["profilePictureUrl"],
            judgements=Judgements.from_dict(data["judgments"])
        )


@dataclass
class BeatmapDifficulty:
    difficulty_id: str
    name: str
    star_rating: float | int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            difficulty_id=data["id"],
            name=data["name"],
            star_rating=data["starRating"]
        )


@dataclass
class Judgements:
    perfect: int
    good: int
    ok: int
    miss: int
    caught: int | None
    catch_miss: int | None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            perfect=data["perfect"],
            good=data["good"],
            ok=data["ok"],
            miss=data["miss"],
            caught=data.get("caught"),
            catch_miss=data.get("catch_miss")
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
    liked: bool
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
            liked=data["liked"],
            timestamp=parse_timestamp(data.get("createdAt"))
        )


@dataclass
class UnplayedDifficulty:
    mapset_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty_name: str
    star_rating: float | int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            mapset_id=data["beatmapId"],
            beatmap_title=data["beatmapTitle"],
            beatmap_artist=data["beatmapArtist"],
            difficulty_name=data["difficultyName"],
            star_rating=data["starRating"]
        )


@dataclass
class UnplayedDifficulties:
    unplayed: list[UnplayedDifficulty]
    total_ranked: int
    total_played: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            unplayed=[
                UnplayedDifficulty.from_dict(item)
                for item in data["unplayed"]
            ],
            total_ranked=data["totalRanked"],
            total_played=data["totalPlayed"],
        )


@dataclass
class BestScore:
    mapset_id: str
    beatmap_title: str
    beatmap_artist: str
    difficulty_name: str
    difficulty_id: str
    score: int
    pp: float | int
    acc: float | int
    max_combo: int
    grade: str
    best_grade: str
    mods: list[str]
    played_at: datetime | None
    updated_at: datetime | None
    judgements: Judgements

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            mapset_id=data["beatmapId"],
            beatmap_title=data["beatmapTitle"],
            beatmap_artist=data["beatmapArtist"],
            difficulty_name=data["difficultyName"],
            difficulty_id=data["difficultyId"],
            score=data["score"],
            pp=data["pp"],
            acc=data["accuracy"],
            max_combo=data["maxCombo"],
            grade=data["grade"],
            best_grade=data["bestGrade"],
            mods=data["mods"],
            played_at=parse_timestamp(data["playedAt"]),
            updated_at=parse_timestamp(data["updatedAt"]),
            judgements=Judgements.from_dict(data["judgments"])
        )


@dataclass
class UserSearchResult:
    user_id: str
    username: str
    profile_picture: str
    total_pp: float | int
    global_rank: int
    country: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=data["userId"],
            username=data["username"],
            profile_picture=data["profilePicture"],
            total_pp=data["totalPP"],
            global_rank=data["globalRank"],
            country=data["country"]
        )


@dataclass
class Nominator:
    user_id: str
    username: str
    discord_id: int
    is_nominator: bool
    is_rank_manager: bool
    is_admin: bool
    banned: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=data["userId"],
            username=data["username"],
            discord_id=data["discordId"],
            is_nominator=data["isNominator"],
            is_rank_manager=data["isRankManager"],
            is_admin=data["isAdmin"],
            banned=data["banned"]
        )


@dataclass
class BeatmapScore:
    position: int
    score: Score

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            position=data["position"],
            score=Score.from_dict(data["score"])
        )
