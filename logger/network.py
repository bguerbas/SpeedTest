# Base imports
from __future__ import annotations
from typing import Any, Callable, Iterable, Mapping

# Project imports
from common.settings import SAMPLING_INTERVAL
from logger.base import PeriodicThread


class NetworkSpeedLogger(PeriodicThread):

    def __init__(self, logger_function: Callable, sampling_interval: int = SAMPLING_INTERVAL) -> None:
        """Overridden constructor."""
        super(NetworkSpeedLogger, self).__init__(logger_function, seconds_to_wait=sampling_interval)

    def start(self, args: Iterable[Any], kwargs: Mapping[str, Any] = None) -> None:
        return super(NetworkSpeedLogger, self).start(args=args, kwargs=kwargs)
