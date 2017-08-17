from redis import Redis
from time import sleep

redis = Redis()


k1 = 'k1'
k2 = 'k2'

v1 = 'v1'
v2 = 'v2'

redis.set(k1,v1)
redis.set(k2,v2)
redis.expire(k1, 5)
redis.expire(k2, 10)

# del get

sleep(3)

print(redis.keys('k*'))

sleep(2)

print(redis.keys('k*'))

sleep(1)

print(redis.keys('k*'))