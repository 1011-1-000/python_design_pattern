import abc

from utils import load_yml


class Chart(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def display(self):
        pass


class Histogram(Chart):

    def __init__(self):
        print('init histogram')

    def display(self):
        print('display histogram')


class Pie(Chart):

    def __init__(self):
        print('init pie')

    def display(self):
        print('display pie')


class Line(Chart):

    def __init__(self):
        print('init line')

    def display(self):
        print('display line')


class ChartFactory():

    @staticmethod
    def get_chart(chart_type):
        if chart_type == 'histogram':
            chart = Histogram()
        elif chart_type == 'pie':
            chart = Pie()
        elif chart_type == 'line':
            chart = Line()
        else:
            raise Exception('unsupported chart type')

        return chart


def test_simple_factory():
    simple_factory = load_yml('factory_pattern/config.yml')['simple_factory']
    chart = ChartFactory.get_chart(configuration['chart_type'])
    chart.display()
