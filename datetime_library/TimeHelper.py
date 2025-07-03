# libs/TimeHelper.py

from datetime import datetime
import pytz

class TimeHelper:
    TIMEZONE_MAP = {
        "chicago": "America/Chicago",
        "new_york": "America/New_York",
        "los_angeles": "America/Los_Angeles",
        "sydney": "Australia/Sydney",
        "utc": "UTC",
    }

    def get_local_date(self, tz_key: str = "utc"):
        tz_name = self.TIMEZONE_MAP.get(tz_key.lower())
        if not tz_name:
            raise ValueError(f"Unsupported timezone key: {tz_key}")

        tz = pytz.timezone(tz_name)
        now = datetime.now(tz)
        return now.strftime("%Y-%m-%d")
