# 装饰器模式关注于在一个对象上动态的添加方法，然而代理模式关注于控制对对象的访问。换句话 说，用代理模式，
# 代理类（proxy class）可以对它的客户隐藏一个对象的具体信息。因此，当使用代理模式的时候，我们常常在一
# 个代理类中创建一个对象的实例。并且，当我们使用装饰器模 式的时候，我们通常的做法是将原始对象作为一个参
# 数传给装饰者的构造器。
import abc


class Validator:

    def __init__(self):
        print('init validator')

    def validate(self):
        print('validate')


class Logger:

    def __init__(self):
        print('init logger')

    def log(self):
        print('log the call function')


class SearchEngine:

    def __init__(self):
        print('init the SearchEngine')

    @abc.abstractmethod
    def search(self):
        pass


class RealSearchEngine(SearchEngine):

    def __init__(self):
        print('init the RealSearchEngine')

    def search(self):
        print('do the search in the real engine')


class SearchProxy(SearchEngine):

    def __init__(self):
        print('init the SearchProxy')
        self.validator = Validator()
        self.logger = Logger()
        self.real_search_engine = RealSearchEngine()

    def search(self):
        self.validator.validate()
        self.real_search_engine.search()
        self.logger.log()


def test_proxy():

    search_engine = SearchProxy()
    search_engine.search()
