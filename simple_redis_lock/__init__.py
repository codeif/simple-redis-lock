from contextlib import contextmanager


@contextmanager
def get_simple_lock(redis_store, key, ex=None):
    lock = redis_store.set(key, '1', ex=ex, nx=True)
    try:
        yield lock
    finally:
        if lock:
            redis_store.delete(key)
