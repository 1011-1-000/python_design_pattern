# 外观模式：为子系统中的一组接口提供一个统一的入口。外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
import abc
from utils import load_yml, get_instance_of_attr


class FileReader:

    def __init__(self, filename):
        print("init file reader")
        self.filename = filename

    def read(self):
        print(f"read the {self.filename}")


class FileCipher:

    def __init__(self, filename):
        print("init file cipher")
        self.filename = filename

    def encrypt(self):
        print(f"encrypt the {self.filename}")


class NewFileCipher():

    def __init__(self, filename):
        print("init file new file cipher")
        self.filename = filename

    def encrypt(self):
        print(f"encrypt the {self.filename}")


class FileWriter:

    def __init__(self, filename):
        print("init file writer")
        self.filename = filename

    def write(self):
        print(f"write the {self.filename}")


class Facade(metaclass=abc.ABCMeta):

    def encrypt(self):
        self.file_reader.read()
        self.file_cipher.encrypt()
        self.file_writer.write()


class FileFacade(Facade):

    def __init__(self, filename):
        print("init file facade")
        self.file_reader = FileReader(filename)
        self.file_writer = FileWriter(filename)
        self.file_cipher = FileCipher(filename)


class NewFileFacade(Facade):

    def __init__(self, filename):
        print("init file facade")
        self.file_reader = FileReader(filename)
        self.file_writer = FileWriter(filename)
        self.file_cipher = NewFileCipher(filename)


def test_facade():
    config = load_yml('facade_pattern/config.yml')
    facade_pattern = config['facade']
    facade = get_instance_of_attr(facade_pattern)('test_file')
    facade.encrypt()
