from requests import get, post
from multiprocessing import Pool
from links import Links
from hasher import Hasher
import Cilanticonfig
from database import Database
from Redis_cli import redis_cli
from queue import *

request_method = {
    'get': get,
    'post': post,
}


class Spider:

    def __init__(self):
        self.threadPool = Pool(Cilanticonfig.MAX_THREAD)
        self.threadPool.deamon=True
        self.URLset = Queue()
        [self.URLset.put(seed) for seed in Cilanticonfig.getSeed() ]
        self.URLhash = set([])
        self.database = Database.Database(Cilanticonfig.dbfile)
        self.redis= redis_cli.redisServer()

    def spi_request(self, method, *args, **kwargs):
        '''used to get the request pages async
        '''
        method = request_method[method]
        value=self.threadPool.apply(method, args=args, kwds=kwargs)
        self.spi_response(value)

    def spi_response(self, response):
        '''Response of the spi_request are handled here
        '''
        if 'text/html' in response.headers['Content-Type'] and response.status_code == 200:
            hash_val = Hasher.HashMD5(response.content)
            if self.redis.getVariable(hash_val) is None:
                if self.database.isConn():
                    self.database.saveData(hash=hash_val ,url=response.url ,content=response)
                self.redis.setVariable(hash_val, response.url)
                [self.URLset.put(link) for link in Links.parse_link(response)]

               #STORE CURRENT URL AND DATA HERE
               # Database.saveData(url,response.content,keyword)
