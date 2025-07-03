# libs/TimeHelper.py
from datetime import datetime
import pytz

class TimeHelper:
    def get_chicago_time(self, fmt="%Y-%m-%d %H:%M:%S"):
        tz = pytz.timezone("America/Chicago")
        now = datetime.now(tz)
        return now.strftime(fmt)
