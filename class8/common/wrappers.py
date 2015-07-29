import time

from django.core.cache import cache


def using_cache(func):
    def wrapper(*args, **kwargs):
        key = '{}_'.format(func.__name__).join([str(arg.pk) for arg in args])
        cache_val = cache.get(key)
        if cache_val:
            return cache_val

        print('No cache found for {}'.format(func.__name__))
        calc_val = func(*args, **kwargs)
        cache.set(key, calc_val, 180)
        return calc_val
    return wrapper


def retry(func):
    retries = [1, 2]

    def wrapper(*args, **kwargs):
        retry_count = kwargs.setdefault('retry_count', len(retries))
        retry_wait = retries[-retry_count]
        retry_count -= 1
        del kwargs['retry_count']
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if retry_count > -1:
                kwargs['retry_count'] = retry_count
                msg = 'Failure in {}, waiting {} seconds before retry'
                print(msg.format(func.__name__, retry_wait))
                time.sleep(retry_wait)
                return wrapper(*args, **kwargs)
            raise e
    return wrapper
