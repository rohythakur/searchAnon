from app import app

print "Running server boss"

DEBUG = True
PORT = 5000
HOST = '127.0.0.1'


app.run(debug=DEBUG, host=HOST, port=PORT)