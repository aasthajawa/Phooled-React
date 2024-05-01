class GameStates:
    IDLE = "idle"
    GAME_PROPOSAL = "game_proposal"
    GAME_SETTINGS = "game_settings"
    SET_UP_QF_DISTRIBUTE_CARDS = "set_up_qf_distribute_cards"
    SET_UP_QF_READY_UP = "set_up_qf_ready_up"
    QUICK_FIRE = "qf"
    QF_TEAR_DOWN = "qf_tear_down"
    SET_UP_AR = "set_up_ar"
    ARSENAL_ROUND = "ar"
    AR_TEAR_DOWN = "ar_tear_down"
    SET_UP_FR = "set_up_fr"
    FR_INIT = "fr_init"
    FR_CLASSIFY_INIT = "fr_classify_init"
    FR_CLASSIFY = "fr_classify"
    FR_CLASSIFY_TEAR_DOWN = "fr_classify_tear_down"
    FR_CLASSIFY_RESULT = "fr_classify_result"
    FR_WILD = "fr_wild"
    FR_INIT_ATTR = "fr_init_attr"
    FR_ATTR_SOLO = "fr_attr_solo"
    FR_ATTR_GROUP = "fr_attr_group"
    FR_ATTR_TEAR_DOWN = "fr_attr_tear_down"
    FR_ATTR_RESULT = "fr_attr_result"
    FR_RESULT = "fr_result"
    FINISH = "finish"
    ABANDON = "abandon"
    ALL = "__all__"


class Misc:
    WEBSOCKET_DOCKER_URL = "ws://nginx:80/ws/phish-game/"
    WEBSOCKET_LOCAL_URL = "ws://127.0.0.1:8000/ws/phish-game/"
    WEBSOCKET_DEV_URL = (
        "wss://206-12-97-82.cloud.computecanada.ca/ws/phish-game/"
    )
    CARD_PLAYER_SERVER = 0
    VAR_WWW_PATH = "/var/www/Phishducation"
    VAR_WWW_PATH_LOWER = "/var/www/phishducation"
    PYTHON_PATH_SERVER = "/var/www/phishducation/env/bin/python"
    PYTHON_PATH_LOCAL = "python"
    CARDS_DISTRIBUTE_ABOVE_LIMIT = 5


class Err:
    SUCCESS = 0
    GO_TO_ABANDON = -4
    RESTORE_STATE = -5


class TimerRet:
    VALID = 1
    SUCCESS = 0
    INVALID = -1
    EMPTY = -2
    ABSENT = -3


DEFAULT_TIMERS = {
    GameStates.FR_CLASSIFY: 30,  # TODO: change this temporary constant value
    # TODO: change this temporary constant value
    GameStates.FR_CLASSIFY_INIT: 30,
    GameStates.FR_CLASSIFY_RESULT: 10,
    # TODO: change this temporary constant value
    GameStates.FR_INIT_ATTR: 30,
    GameStates.FR_ATTR_SOLO: 30,
    GameStates.FR_ATTR_GROUP: 30,
    GameStates.FR_ATTR_RESULT: 10,
    GameStates.ABANDON: 60,
    GameStates.ALL: 60 * 60 * 2,
}
