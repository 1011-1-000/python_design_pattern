#  在正式介绍桥接模式之前，我先跟大家谈谈两种常见文具的区别，它们是毛笔和蜡笔。假如我们需要大中小3种型号的画笔，
#  能够绘制12种不同的颜色，如果使用蜡笔，需要准备3×12 = 36支，但如果使用毛笔的话，只需要提供3种型号的毛笔，
#  外加12个颜料盒即可，涉及到的对象个数仅为 3 + 12 = 15，远小于36，却能实现与36支蜡笔同样的功能。如果增加一种新型号的画笔，
#  并且也需要具有12种颜色，对应的蜡笔需增加12支，而毛笔只需增加一支。为什么会这样呢？
#  通过分析我们可以得知：在蜡笔中，颜色和型号两个不同的变化维度（即两个不同的变化原因）融合在一起，
#  无论是对颜色进行扩展还是对型号进行扩展都势必会影响另一个维度；但在毛笔中，颜色和型号实现了分离，
#  增加新的颜色或者型号对另一方都没有任何影响。如果使用软件工程中的术语，我们可以认为在蜡笔中颜色和型号之间存在较强的耦合性，
#  而毛笔很好地将二者解耦，使用起来非常灵活，扩展也更为方便。
#  在软件开发中，我们也提供了一种设计模式来处理与画笔类似的具有多变化维度的情况

# 桥接模式用一种巧妙的方式处理多层继承存在的问题，用抽象关联取代了传统的多层继承，将类之间的静态继承关系转换为动态的对象组合关系，
# 使得系统更加灵活，并易于扩展，同时有效控制了系统中类的个数。桥接定义如下：

# 版权声明：本文为CSDN博主「Liuwei-Sunny」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/lovelion/article/details/7464183

import abc
from utils import load_yml, get_instance_of_attr


class Matrix:

    def __init__(self):
        print('Generate the pixel matrix')


class ImageImp(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def doPaint(self):
        pass


class LinuxImp(ImageImp):

    def doPaint(self, matrix):
        print('LinuxImp: doPaint')


class UnixImp(ImageImp):

    def doPaint(self, matrix):
        print('UnixImp: doPaint')


class WindowsImp(ImageImp):

    def doPaint(self, matrix):
        print('WindowsImp: doPaint')


class Image:

    def __init__(self):
        self.imp = None

    def setImageImp(self, imp):
        self.imp = imp

    @abc.abstractmethod
    def parseFile(self, filename):
        pass


class JPGImage(Image):

    def __init__(self):
        super(JPGImage, self).__init__()

    def parseFile(self, filename):
        matrix = Matrix()
        self.imp.doPaint(matrix)
        print('file has been painted with JPG format')


class PNGImage(Image):

    def __init__(self):
        super(PNGImage, self).__init__()

    def parseFile(self, filename):
        matrix = Matrix()
        self.imp.doPaint(matrix)
        print('file has been painted with PNG format')


class BMPImage(Image):

    def __init__(self):
        super(BMPImage, self).__init__()

    def parseFile(self, filename):
        matrix = Matrix()
        self.imp.doPaint(matrix)
        print('file has been painted with BMP format')


class GIFImage(Image):

    def __init__(self):
        super(GIFImage, self).__init__()

    def parseFile(self, filename):
        matrix = Matrix()
        self.imp.doPaint(matrix)
        print('file has been painted with GIF format')


def test_bridge():
    config = load_yml('bridge_pattern/config.yml')
    os = get_instance_of_attr(config['os'])()
    image = get_instance_of_attr(config['image'])()
    image.setImageImp(os)
    image.parseFile('leo.jpg')
