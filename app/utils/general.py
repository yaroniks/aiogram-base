import os
from pytz import timezone
from config import settings
from typing import Union, Optional, Any
from datetime import datetime, timedelta


def log(text: Any) -> None:
    print(f'[{time_now("%Y-%m-%d %H:%M:%S")}] [INFO]: {text}', flush=True)


def time_now(strftime: str = None, location: str = 'Europe/Moscow') -> Union[datetime, str]:
    date = datetime.now(timezone(location))
    if strftime is None:
        return date
    return date.strftime(strftime)
