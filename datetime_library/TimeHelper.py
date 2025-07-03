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

    def convert_utc_to_local_date(self, utc_date_str: str, tz_key: str = "utc", fmt: str = "%Y-%m-%d"):
        """
        Convert UTC date string (6 or 8 chars) to local date string in given timezone.
        Accepts:
         - 6 char date string: yyMMdd
         - 8 char date string: yyyyMMdd
        Time part assumed 00:00:00 UTC if missing.

        :param utc_date_str: e.g. '250703' or '20250703'
        :param tz_key: timezone key from TIMEZONE_MAP
        :param fmt: output format string, default '%Y-%m-%d'
        :return: formatted local date string
        """

        tz_name = self.TIMEZONE_MAP.get(tz_key.lower())
        if not tz_name:
            raise ValueError(f"Unsupported timezone key: {tz_key}")

        tz = pytz.timezone(tz_name)

        # Detect format based on length
        if len(utc_date_str) == 6:
            dt_format = "%y%m%d"
        elif len(utc_date_str) == 8:
            dt_format = "%Y%m%d"
        else:
            raise ValueError(f"Invalid date string length: {utc_date_str}")

        # Parse date (no time part, assume midnight UTC)
        utc_dt = datetime.strptime(utc_date_str, dt_format)
        utc_dt = datetime(utc_dt.year, utc_dt.month, utc_dt.day, 0, 0, 0, tzinfo=pytz.utc)

        # Convert to local timezone
        local_dt = utc_dt.astimezone(tz)

        return local_dt.strftime(fmt)
