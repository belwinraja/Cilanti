import redis

class redisServer:

    """docstring for [object Object]."""
    def __init__(self):
        self.POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

    def getVariable(self, name):
        my_server = redis.Redis(connection_pool=self.POOL)
        return my_server.get(name)

    def setVariable(self, name, value):
        my_server = redis.Redis(connection_pool=self.POOL)
        my_server.set(name, value)

    def keyFound(self, name):
        my_server = redis.Redis(connection_pool=self.POOL)
        return my_server.keys(name)
