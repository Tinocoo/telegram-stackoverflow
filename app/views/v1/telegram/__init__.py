from flask.blueprints import Blueprint


v1_telegram = Blueprint('v1_telegram', __name__)

from .controllers import *

v1_telegram.add_url_rule('/msg', view_func=ManagerTelegram.as_view('ManagerTelegram'))
v1_telegram.add_url_rule('/webhook', view_func=ManagerWebhook.as_view('ManagerWebhook'))
