from flask import Flask

from app.views import ManagerTelegram, ManagerWebhook


def create_app():
    app = Flask(__name__)

    app.add_url_rule('/msg', view_func=ManagerTelegram.as_view('ManagerTelegram'))
    app.add_url_rule('/webhook', view_func=ManagerWebhook.as_view('ManagerWebhook'))
    return app
