# Base imports
from __future__ import annotations
from typing import (
    Any,
    Iterable,
    Callable,
    Mapping,
)
import logging

# Third-party imports
from threading import Timer


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(threadName)-9s] %(message)s',
)


class PeriodicThread:

    """A class to represent a person.

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.

    """

    def __init__(self, target_function: Callable, seconds_to_wait: int) -> None:
        """Constructor."""
        self._should_continue = False
        self.is_running = False
        self.seconds_to_wait = seconds_to_wait
        self.target_function = target_function
        self.thread: Timer

    def _handle_target(self, *args, **kwargs) -> None:
        try:
            self.is_running = True
            self.target_function(*args, **kwargs)
            self.is_running = False
            self._start_thread(args, kwargs)
        except Exception as exc:
            print(str(exc))

    def _start_thread(self, args: Iterable[Any] = None, kwargs: Mapping[str, Any] = None) -> None:
        if self._should_continue:           # Code could have been running when cancel was called.
            self.thread = Timer(self.seconds_to_wait, self._handle_target, args, kwargs)
            self.thread.start()

    def start(self, args: Iterable[Any], kwargs: Mapping[str, Any] = None) -> None:
        if not self._should_continue and not self.is_running:
            self._should_continue = True
            self._start_thread(args, kwargs)
        else:
            logging.debug("Thread already started or running, please wait if you're restarting.")

    def cancel(self) -> None:
        if self.thread is not None:
            self._should_continue = False   # Just in case thread is running and cancel fails.
            self.thread.cancel()
        else:
            logging.debug("Thread never started or failed to initialize.")
