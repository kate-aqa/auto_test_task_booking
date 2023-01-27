import os


class Config:
    web_ui_wait_timeout = 10
    headless = False
    password = 'Test1213!'
    login = 'autotesttask@ukr.net'


def get_download_dir():
    download_dir = os.path.join(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                os.path.join("resources", "download"))
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir
