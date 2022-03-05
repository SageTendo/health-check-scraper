from robobrowser import RoboBrowser
from exceptions.ExceptionHandler import DIVException, HealthCheckException
from logger.Logger import DEBUG
from scraper.const import STATUS, RECEIPT_URL


class HealthStatusScraper:
    __handled = False
    __redo = False
    __fetched = False

    def __init__(self, client: RoboBrowser, status: str, redo: bool):
        """
        TODO: docstring
        :param client:
        :param redo:
        """
        self.__client = client
        self.__status = status

        DEBUG(f'RESPONSE: <{self.__client.response.url}>')

        if redo and self.__client.response.url == RECEIPT_URL:
            self.__form = self.__client.get_form(action='/')
            self.__form['redo'] = 'true'
            self.__client.submit_form(self.__form)
            self.__redo = True

    def __get_login_form(self):
        """
        TODO: docstring
        """
        self.__form = self.__client.get_form('login_form')

    def __handle_form(self):
        """
        TODO: docstring
        """
        if self.__status not in STATUS.keys():
            raise HealthCheckException('ERROR: Invalid healthcheck status provided')

        selected_status = STATUS[self.__status]
        for key in selected_status:
            if key in self.__form.keys():
                self.__form[key] = selected_status[key]
        # TODO: PERSONALISE VACCINE UPTAKE
        self.__form['vaccine_uptake'] = 'FULLY'
        self.__handled = True

    def submit_form(self):
        """
        TODO: docstring
        """
        self.__get_login_form()
        if not self.__redo:
            self.__form['healthcheck-terms'] = 'on'
        self.__handle_form()
        self.__client.submit_form(self.__form)
        self.__fetched = True

    def get_receipt_div(self):
        """
        TODO: docstring
        :return:
        """
        if self.__fetched:
            status_div = self.__client.find('ul', class_='receipts-results-message-list')
            try:
                receipt_div = self.__client.find('div', class_='receipts-results receipts-results--low')
                if not receipt_div:
                    raise DIVException('Receipt DIV not found')
                return 'green', status_div, receipt_div
            except DIVException as error:
                print(repr(error))

            try:
                receipt_div = self.__client.find("div", class_='receipts-results receipts-results--mid')
                if not receipt_div:
                    raise DIVException('Receipt DIV not found')
                return 'orange', status_div, receipt_div
            except DIVException as error:
                print(repr(error))

            try:
                receipt_div = self.__client.find('div', class_='receipts-results receipts-results--high')
                if not receipt_div:
                    raise DIVException('Receipt DIV not found')
                return 'red', status_div, receipt_div
            except DIVException as error:
                print(repr(error))

    def __repr__(self):
        """
        TODO: docstring
        :return:
        """
        return self.__client.response.url