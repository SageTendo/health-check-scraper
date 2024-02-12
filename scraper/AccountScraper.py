import logging

import requests
from robobrowser import RoboBrowser

from exceptions.ExceptionHandler import AuthException
from scraper.HealthStatusScraper import HealthStatusScraper
from scraper.const import BASE_URL, LOGIN_URL


class AccountScraper:

    def __init__(self, user_session: requests.Session = None):
        self.__client = RoboBrowser(session=user_session, history=True, parser='html.parser')
        self.__client.open(BASE_URL)

        logging.debug(f'BASE <{BASE_URL}> : RESPONSE <{self.__client.url}>')
        self.logged_in = (self.__client.response.url != LOGIN_URL)

    def __get_login_form(self):
        self.__form = self.__client.get_form(id='login_form')

    def login(self, phone: str):
        if not phone:
            raise AuthException("ERROR: Phone number not provided")

        self.__get_login_form()
        self.__form['msisdn'] = phone
        self.__client.session.headers['Referer'] = BASE_URL
        self.__client.submit_form(self.__form)

    def verify_login(self, otp: str):
        if not otp:
            raise AuthException("ERROR: OTP not provided")

        if self.__client.response.history:
            if self.__client.response.history[0].status_code == 302:
                self.__get_login_form()  # Fetch the new login form
                self.__form['otp'] = otp
                self.__client.submit_form(self.__form)
                logging.debug(f'RESPONSES : {self.__client.response.history}')

                if self.__client.response.history:
                    if self.__client.response.history[0].status_code == 302:
                        self.logged_in = True
                        logging.debug(
                            f'STATUS CODE: {self.__client.response.history[0].status_code} -- LOGGED IN SUCCESSFULLY')
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
        return self.__client.session

    def close_session(self):
        self.__client.session.close()

    def generate_health_check(self, healthcheck_status: str):
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
        return str(self.__client.response.content)
