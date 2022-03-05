import requests
from robobrowser import RoboBrowser
from logger.Logger import DEBUG
from scraper.HealthStatusScraper import HealthStatusScraper
from exceptions.ExceptionHandler import AuthException
from scraper.const import BASE_URL, LOGIN_URL


class AccountScraper:

    def __init__(self, user_session: requests.Session = None):
        """
        TODO: docstring
        :param user_session:
        """
        self.__client = RoboBrowser(session=user_session, history=True, parser='html.parser')
        self.__client.open(BASE_URL)

        DEBUG(f'BASE <{BASE_URL}> : RESPONSE <{self.__client.url}>')
        self.logged_in = (self.__client.response.url != LOGIN_URL)

    def __get_login_form(self):
        """
        TODO: docstring
        """
        self.__form = self.__client.get_form(id='login_form')

    def login(self, phone: str):
        """
        TODO: docstring
        :param phone:
        """
        if not phone:
            raise AuthException("ERROR: Phone number not provided")

        self.__get_login_form()
        self.__form['msisdn'] = phone
        self.__client.session.headers['Referer'] = BASE_URL
        self.__client.submit_form(self.__form)

    def verify_login(self, otp: str):
        """
        TODO: docstring
        :param otp:
        """
        if not otp:
            raise AuthException("ERROR: OTP not provided")

        if self.__client.response.history:
            if self.__client.response.history[0].status_code == 302:
                self.__get_login_form()  # Fetch the new login form
                self.__form['otp'] = otp
                self.__client.submit_form(self.__form)
                DEBUG(f'RESPONSES : {self.__client.response.history}')

                if self.__client.response.history:
                    if self.__client.response.history[0].status_code == 302:
                        self.logged_in = True
                        DEBUG(f'STATUS CODE: {self.__client.response.history[0].status_code} -- LOGGED IN SUCCESSFULLY')
                    else:
                        raise AuthException("ERROR: Something went wrong when trying to send the verification request")
                else:
                    raise AuthException("ERROR: Incorrect OTP provided")
            else:
                raise AuthException("ERROR: User not found")
        else:
            raise AuthException("ERROR: Something went wrong when trying to send a login request")

    def is_logged_in(self):
        return self.logged_in

    def get_session(self):
        """
        TODO: docstring
        :return:
        """
        return self.__client.session

    def close_session(self):
        """
        TODO: docstring
        """
        self.__client.session.close()

    def generate_health_check(self, healthcheck_status: str):
        """
        TODO: docstring
        :param healthcheck_status:
        :return:
        """
        if not self.logged_in:
            raise AuthException("ERROR: User not logged in")

        health_status = HealthStatusScraper(client=self.__client, status=healthcheck_status, redo=True)
        health_status.submit_form()

        receipt_type, status_div, receipt_div = health_status.get_receipt_div()
        return {
            'url': health_status,
            'status_div': status_div,
            'receipt_div': receipt_div,
            'receipt_type': receipt_type
        }

    def __str__(self):
        """
        TODO: docstring
        :return:
        """
        return str(self.__client.response.content)
