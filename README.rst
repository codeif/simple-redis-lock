A simple redis lock.
=========================

Installation
---------------

.. code-block:: sh

    pip install simple-redis-lock


Usage
-------

.. code-block:: py

    from simple_redis_lock import get_simple_lock
    import your_redis_client

    with get_imple_lock(your_redis_client, 'my_lock_name', ex=30) as lock:
        if lock:
            print('get the lock, and do something, finish release the lock')
        else:
            print('do not get lock, return')
