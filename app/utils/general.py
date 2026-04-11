from config import settings

import logging
from pytz import timezone
from typing import Union, Optional, Any
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def time_now(strftime: str = None, location: str = 'Europe/Moscow') -> Union[datetime, str]:
    date = datetime.now(timezone(location))
    if strftime is None:
        return date
    return date.strftime(strftime)
