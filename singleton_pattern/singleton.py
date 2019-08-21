import threading
import time


class GeneralSingleton:

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            time.sleep(1)
            cls.instance = super().__new__(cls)
        return cls.instance


class EagerSingletion():

    class _EagerSingletion():

        def __init__(self):
            print('init')

    instance = _EagerSingletion()

    @staticmethod
    def get_instance():
        return EagerSingletion.instance


class LazySingleton():
    instance = None
    lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        cls.lock.acquire()
        try:
            if cls.instance:
                return cls.instance
            cls.instance = super().__new__(cls)
            return cls.instance
        finally:
            cls.lock.release()


class LazySingletonMeta(type):

    instance = None
    lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        cls.lock.acquire()
        try:
            if cls.instance:
                return cls.instance
            cls.instance = super().__call__(*args, **kwargs)
            return cls.instance
        finally:
            cls.lock.release()


class EagerSingletonMeta(type):

    class _EagerSingleton():

        def __init__(self):
            print('eager init')

    instance = _EagerSingleton()

    def __call__(cls, *args, **kwargs):
        return cls.instance


class Singleton(metaclass=EagerSingletonMeta):
    pass

# 类似可写装饰器模式


def get_singleton_instance():
    print(id(Singleton()))


def test_singletion_threading():
    for x in range(100):
        t = threading.Thread(target=get_singleton_instance)
        t.start()
