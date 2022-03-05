import io
from html2image import Html2Image

from scraper.const import IMAGE_DIMENSIONS
from settings import user_receipts_path, images_path, css_path


class ImageProcessor:
    def __init__(self):
        """
        TODO: docstring
        """
        self.h2i = Html2Image(output_path=user_receipts_path)

    @staticmethod
    def __generate_html(status_div: str, receipt_div: str):
        """
        TODO: docstring
        :param status_div:
        :param receipt_div:
        :return:
        """
        # noinspection SpellCheckingInspection
        html = f"""
        <!DOCTYPE html>
        <html>
            <head>
            <link rel="stylesheet" href="{css_path}/style.css">
            <link rel="stylesheet" href="{css_path}/style2.css">
            </head>
            <body>
                <div class="content-receipts">
                    <div class="content-receipts__block">
                        <div class="content-receipts__logo">
                            <a class="logo-list__anchor" href="http://higherhealth.ac.za/">
                              <img class="header-brand__logo" src="{images_path}/header.png" alt="Higherhealth Logo">
                            </a>
                        </div>
                        {status_div}
                </div>
                <img class="lifebouy-ad" src="{images_path}/header-logo.png" alt="Eu, HWSETA, Lifebuoy logos" role="img">
                {receipt_div}
                </div>
            </body>
        </html>"""
        return html

    def generate_image(self, user_id: int, status_div: str, receipt_div: str, receipt_type: str):
        """
        TODO: docstring
        :param user_id:
        :param status_div:
        :param receipt_div:
        :param receipt_type:
        """
        filename = f'{user_id}.jpg'
        html = self.__generate_html(status_div, receipt_div)
        size = IMAGE_DIMENSIONS[receipt_type]
        self.h2i.screenshot(html_str=html, save_as=filename, size=size)

    @staticmethod
    def open_image(user_id: int):
        """
        TODO: docstring
        :param user_id:
        :return:
        """
        file = f'{user_receipts_path}/{user_id}.jpg'
        with open(file, 'rb') as f:
            f = io.BytesIO(f.read())
            return f
