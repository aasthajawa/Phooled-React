from pathlib import Path
import shortuuid

from .models import User

from game import const

def get_user_name(user_id):
    return User.objects.filter(user_id=user_id).first().username

def var_www_path_exists():
    if not Path(const.Misc.VAR_WWW_PATH_LOWER).exists():
        if not Path(const.Misc.VAR_WWW_PATH).exists():
            return False
    return True

def is_current_instance_server():
    return var_www_path_exists()

def get_instance_websocket_url():
    if is_current_instance_server():
        return const.Misc.WEBSOCKET_DEV_URL
    return const.Misc.WEBSOCKET_DOCKER_URL

def get_instance_python_path():
    if is_current_instance_server():
        return const.Misc.PYTHON_PATH_SERVER
    return const.Misc.PYTHON_PATH_LOCAL

def generate_uuid(length = 10):
    return shortuuid.uuid()[:length]
