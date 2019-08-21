import abc
from utils import load_yml, get_instance_of_attr


class LegendFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_legend(legend_type):
        if legend_type == 'basic_legend':
            legend = BasicLegend()
        elif legend_type == 'group_legend':
            legend = GroupLegend()
        else:
            raise Exception('unsupported legend type')
        return legend


class AxisFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_axis(axis_type):
        if axis_type == 'x_axis':
            axis = xAxis()
        elif axis_type == 'yAxis':
            axis = yAxis()
        else:
            raise Exception('unsupported legend type')
        return axis


class Legend:

    def __init__(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass


class BasicLegend(Legend):

    def __init__(self):
        print('init basic legend')

    def draw(self):
        print('draw basic legend')


class GroupLegend(Legend):

    def __init__(self):
        print('init group legend')

    def draw(self):
        print('draw group legend')


class Axis:

    def __init__(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass


class xAxis(Axis):

    def __init__(self):
        pass

    def draw(self):
        print('draw xAxis')


class yAxis(Axis):

    def __init__(self):
        pass

    def draw(self):
        print('draw yAxis')


class BasicLine:

    def __init__(self):
        self.legend = BasicLegend()
        self.xAxis = xAxis()
        self.yAxis = yAxis()

    def draw_chart(self):
        self.legend.draw()
        self.xAxis.draw()
        self.yAxis.draw()


class GroupLegendLine:

    def __init__(self):
        self.legend = GroupLegend()
        self.xAxis = xAxis()
        self.yAxis = yAxis()

    def draw_chart(self):
        self.legend.draw()
        self.xAxis.draw()
        self.yAxis.draw()


def test_abstract_factory():

    config = load_yml('factory_pattern/config.yml')
    factory_pattern = config['abstract_factory']
    chart = get_instance_of_attr(factory_pattern['chart'])()
    chart.draw_chart()
