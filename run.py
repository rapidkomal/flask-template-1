import logging
import os

from flask import Flask

from app.v1.project import project


# def create_app():
app = Flask(__name__)

# Logger
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(
                        os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])
LOGGER = logging.getLogger()

app.config.update(
    FLASK_ENV=os.getenv('FLASK_ENV'),
    DEBUG=os.getenv('DEBUG'),
)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# Register blueprints
app.register_blueprint(project)

    # return app

if __name__ == '__main__':
    app.run()
