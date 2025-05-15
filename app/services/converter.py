from datetime import datetime, timezone


def utc_to_unix(utc_str: str) -> int:
    dt = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
    return int(dt.timestamp())


def unix_to_utc(unix_ts: int) -> str:
    dt = datetime.fromtimestamp(unix_ts, tz=timezone.utc)
    return dt.isoformat()
