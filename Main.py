from request import Spider
from threading import Thread
import Cilanticonfig


'''Spider instance created here'''

spider = Spider.Spider()
while not spider.URLset.empty():
    if Cilanticonfig.DONE:
        break
    i=spider.URLset.get()
    spider.spi_request('get', i )
print("-----------------------------------------------------Done--------------------------------------------------")

for j in spider.URLhash:
    print(j)
