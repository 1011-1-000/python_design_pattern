import abc


class AbstractFile(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add(self, filename):
        pass

    @abc.abstractmethod
    def remove(self, filename):
        pass

    @abc.abstractmethod
    def getChild(self, i):
        pass

    @abc.abstractmethod
    def killVirus(self):
        pass


class ImageFile(AbstractFile):

    def __init__(self, filename):
        self.filename = filename

    def add(self, file):
        print('unsupported operation')

    def remove(self, file):
        print('unsupported operation')

    def getChild(self, i):
        print('unsupported operation')

    def killVirus(self):
        print(f'Kill virus on the {self.filename}')


class TextFile(AbstractFile):

    def __init__(self, filename):
        self.filename = filename

    def add(self, file):
        print('unsupported operation')

    def remove(self, file):
        print('unsupported operation')

    def getChild(self, i):
        print('unsupported operation')

    def killVirus(self):
        print(f'Kill virus on the {self.filename}')


class VideoFile(AbstractFile):

    def __init__(self, filename):
        self.filename = filename

    def add(self, file):
        print('unsupported operation')

    def remove(self, file):
        print('unsupported operation')

    def getChild(self, i):
        print('unsupported operation')

    def killVirus(self):
        print(f'Kill virus on the {self.filename}')


class Folder(AbstractFile):

    def __init__(self, filename):
        self.filename = filename
        self.filelist = []

    def add(self, file):
        self.filelist.append(file)

    def remove(self, file):
        self.filelist.remove(file)

    def getChild(self, i):
        return self.filelist[i]

    def killVirus(self):
        print(f'Kill virus on the {self.filename}')
        for i in range(len(self.filelist)):
            file = self.getChild(i)
            file.killVirus()


def test_composite():

    imageFile = ImageFile('image.png')
    videoFile = VideoFile('video.rm')
    textFile = TextFile('text.txt')

    imageFolder = Folder('imageFolder')
    videoFolder = Folder('videoFolder')
    textFolder = Folder('textFolder')

    imageFolder.add(imageFile)
    videoFolder.add(videoFile)
    textFolder.add(textFile)

    folder = Folder('myFolder')
    folder.add(imageFolder)
    folder.add(videoFolder)
    folder.add(textFolder)

    folder.killVirus()
