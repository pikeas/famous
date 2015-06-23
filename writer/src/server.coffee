{json} = require 'body-parser'
express = require 'express'
Redis = require 'ioredis'


PORT = process.env.NODE_PORT or 5001
QUEUE_KEY = process.env.QUEUE_KEY or 'famous'


app = express()
db = new Redis(host: process.env.DB_HOST)


app.use json()


app.post '/write', (req, res) ->
    if not req.body.text?
        return res.status(400).send('No text present!')

    db.lpush(QUEUE_KEY, req.body.text)
    .then (status) ->
        console.log status
        return res.sendStatus(200)
    .catch (err) ->
        console.log err
        return res.sendStatus(500)


app.listen(PORT)
