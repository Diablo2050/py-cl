from flask import Flask
from tasks import make_celery
flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='pyamqp://amr:admin@rabbitmq_min:5672/celery',
    CELERY_RESULT_BACKEND='redis://redis_min/0'
)
celery = make_celery(flask_app)

@flask_app.route('/')
@celery.task()
def add_together(a, b):
    return a + b

if __name__ == '__main__':
    flask_app.run()