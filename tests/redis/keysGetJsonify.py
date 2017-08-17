from redis import Redis 
from flask import jsonify,Flask

app = Flask(__name__)

redis = Redis()


k1 = 'k1'
k2 = 'k2'

v1 = 'v1'
v2 = 'v2'

redis.set(k1,v1)
redis.set(k2,v2) 
klist = redis.keys('k*') 

vlist = [redis.get(k).decode('utf-8') for k in klist]
# decode binary to a str object before jsonify 

@app.route('/')
def index():
	return jsonify({'product':vlist}) 


app.run(debug=True)