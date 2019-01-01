from contextlib import contextmanager


@contextmanager
def simple_lock(redis_store, key, ex=None):
    lock = redis_store.set(key, '1', ex=ex, nx=True)
    yield lock
    if lock:
        redis_store.delete(key)
