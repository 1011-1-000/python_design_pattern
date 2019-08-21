import abc

from utils import load_yml, get_instance_of_attr


class BarFactory:

    def __init__(self):
        print('init bar factory')

    @staticmethod
    def get_chart(chart_type):
        if chart_type == 'basic_bar':
            chart = BasicBar()
        elif chart_type == 'group_bar':
            chart = GroupBar()
        else:
            raise Exception('unsupported bar chart type')
        return chart


class LineFactory:

    def __init__(self):
        print('init line factory')

    @staticmethod
    def get_chart(chart_type):
        if chart_type == 'basic_line':
            chart = BasicLine()
        elif chart_type == 'multiple_line':
            chart = MultipleLine()
        else:
            raise Exception('unsupported Line chart')
        return chart


class Chart():

    def __init__(self):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class BasicBar(Chart):

    def __init__(self):
        print('init basic bar')

    def display(self):
        print('display basic bar')


class GroupBar(Chart):

    def __init__(self):
        print('init group bar')

    def display(self):
        print('display group bar')


class BasicLine(Chart):

    def __init__(self):
        print('init basic line')

    def display(self):
        print('display basic line')


class MultipleLine(Chart):

    def __init__(self):
        print('init multiple line')

    def display(self):
        print('display multiple line')


def test_factory():
    config = load_yml('factory_pattern/config.yml')
    factory_pattern = config['factory_pattern']
    factory = get_instance_of_attr(factory_pattern['factory'])
    chart = factory.get_chart(factory_pattern['chart_type'])
    chart.display()
