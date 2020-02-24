from flask import Flask
from tasks import make_celery
flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(flask_app)

@flask_app.route('/')
@celery.task()
def add_together(a, b):
    return a + b

if __name__ == '__main__':
    flask_app.run()