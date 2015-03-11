from checkio_referee import RefereeRank
from checkio_referee import covercodes

import settings
import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "count_squares"
    ENV_COVERCODE = {
        "python_3": covercodes.py_unwrap_args,
        "python_2": covercodes.py_unwrap_args,
        "javascript": None
    }
