#!/usr/bin/env python3
from arisutils import env

from app import app


HOST = env('HOST', '0.0.0.0')
PORT = env('PORT', 5000)


app.run(host=HOST, port=PORT)
