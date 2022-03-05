from exceptions.ExceptionHandler import AuthException
from logger.Logger import DEBUG


def verify_otp(otp: str):
    """
    TODO: docstring
    :param otp:
    """
    if len(otp) != 6:
        raise AuthException('ERROR: OTP must be 6 digits long')

    try:
        int(otp)
    except ValueError:
        raise AuthException("ERROR: Invalid OPT provided")


def verify_phone(phone: str):
    """
    TODO: docstring

    :param phone:
    """
    if len(phone) != 10:
        raise AuthException('ERROR: Phone number must be 10 digits long')

    try:
        int(phone)
    except ValueError:
        DEBUG(f'USER {phone} provided a phone number of an invalid length')
        raise AuthException("ERROR: Invalid phone number provided")
