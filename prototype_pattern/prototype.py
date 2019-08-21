import copy


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, person):
        if self.name == person.name and self.age == person.age:
            return True
        else:
            return False


def test_prototype():

    p1 = Person('Leo', 32)
    p2 = copy.deepcopy(p1)
    assert p1 == p2
    assert id(p1) != d(p2)
