from datetime import datetime, timezone


def utc_to_both(utc_str: str) -> dict:
    try:
        dt = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
        unix_ts = int(dt.timestamp())
        return {"utc": dt.isoformat(), "unix": unix_ts}
    except ValueError:
        raise ValueError(
            "Invalid UTC datetime format. Use ISO format like 2024-05-15T12:00:00Z."
        )


def unix_to_both(unix_ts: int) -> dict:
    try:
        dt = datetime.fromtimestamp(unix_ts, tz=timezone.utc)
        return {"utc": dt.isoformat(), "unix": unix_ts}
    except (OverflowError, OSError, ValueError):
        raise ValueError("Invalid UNIX timestamp. Must be a valid number.")
