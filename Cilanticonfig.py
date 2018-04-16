#Thread Pool count
MAX_THREAD = 2
DONE = False
seed = ['https://www.stackoverflow.com', 'https://en.wikipedia.org/', 'https://www.quora.com',
            'https://www.reddit.com', 'https://www.cancer.com', 'http://www.who.int/en/', 'https://www.unicef.org/',
            'https://en.unesco.org/', 'http://www.un.org/en/index.html', 'https://www.tutorialspoint.com/index.html']

dbfile = 'data.sql'

def getSeed():
    return seed
