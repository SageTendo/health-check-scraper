from datetime import datetime

debug = False


def DEBUG(msg):
    """
    TODO: docstring
    :param msg:
    """
    print(f'{datetime.utcnow()} ::\n \t \t {msg}')
