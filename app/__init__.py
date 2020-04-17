from flask import Flask
from flask_cors import CORS
import importlib
import os


def create_app():
    app = Flask(__name__)

    environ = {
        'dev': 'app.inc.Config.DevelopmentConfig',
        'prod': 'app.inc.Config.ProductionConfig'
    }

    conf = environ.get(os.environ.get('FLASK_CONF', default='dev'))
    app.config.from_object(conf)

    CORS(app)

    # Mapeando classe de configuração
    mod = importlib.import_module('.'.join(conf.split('.')[:-1]))
    
    # Pegando atributos da classe
    env = getattr(mod, conf.split('.')[-1:][0])

    # Registrando blueprint baseado na configuração dos modulos
    for module in env.MODULES:
        for version in range(1, env.VERSIONS + 1):
            try:
                package = importlib.import_module('app.views.v{}'.format(version))
                app.register_blueprint(
                    getattr(package, 'v{}_{}'.format(version, module)),
                    url_prefix='/v{}/{}'.format(version, module)
                )
            except Exception as e:
                print(str(e))

    return app
