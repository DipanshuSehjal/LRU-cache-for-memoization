from collections import namedtuple, OrderedDict
import functools, urllib.request, urllib.error

def lru_cache(maxsize=128):
    def decorator(func): # store global
        cache = OrderedDict()  # to preserve the order of insertion in dict
        hits, misses = 0, 0

        @functools.wraps(func)
        def inner(*args, **kwargs):
            def cache_info():
                info = namedtuple('CacheInfo', ['hits', 'misses', 'maxsize', 'currsize'])
                return info(hits, misses, maxsize, len(cache))
            inner.cache_info = cache_info
            for arg in list(args)+list(kwargs.values()): # update cache list
                if arg not in cache.keys():
                    x = func(*args, **kwargs)
                    if isinstance(maxsize, int):
                        if len(cache) < maxsize:  # Queue
                            cache.update({arg: x})    # add new element
                        else:                   # cache is full # FIFO
                            cache.popitem(last=False) # remove arg at first location(least arg)
                            cache.update({arg: x}) # add new value to cache
                    else:
                        cache.update({arg: x})  # add new element
                    nonlocal misses
                    misses += 1
                    return cache[arg]
                else:                       # arg is in cache. Make it recent call in cache
                    tmp=cache[arg]          # take value for that arg
                    cache.pop(arg)          # delete that arg
                    cache.update({arg:tmp}) # add at latest/recent position(end of queue)
                    nonlocal hits
                    hits += 1
                    return cache[arg]
        return inner
    return decorator

@lru_cache()
def get_pep(num):
     resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
     try:
         with urllib.request.urlopen(resource) as s:
             return s.read()
     except urllib.error.HTTPError:
         return 'Not Found'