from arisutils import env
from flask import Flask, make_response
from redis import Redis

DEBUG = env('FLASK_DEBUG', False)
DB = Redis(host=env('DB_HOST'))
QUEUE_KEY = env('QUEUE_KEY', 'famous')

app = Flask(__name__)
app.config.update(
    DEBUG=DEBUG,
)


@app.route('/read')
def read():
    item = DB.rpop(QUEUE_KEY)
    if item is None:
        return make_response('Error: no data available for read. Please try again later!', 400)
    return item
