from flask import Flask
from redis import Redis

app = Flask(__name__)
r = Redis(host='redis', port=6379)

@app.route('/inc')
def inc():
    r.incr('counter')
    return 'Counter incremented by 1'

@app.route('/dec')
def dec():
    r.decr('counter')
    return f'Counter decremented by 1'

@app.route('/queries')
def queries():
    counter = str(r.get('counter'), 'utf-8')
    return f"Actual counter value is equal: {counter}." 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
