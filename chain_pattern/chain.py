import sys


class PurchaseRequest:

    def __init__(self, amount, thing):
        self.amount = amount
        self.thing = thing


class Approver:

    def __init__(self, name, approved_budget, successor=None):
        self.name = name
        self.approved_budget = approved_budget
        self.successor = successor

    def process_request(self, request):
        if request.amount <= self.approved_budget:
            print(f"{request.thing} is approved by {self.name}")
        else:
            self.successor.process_request(request)


def test_chain():
    purchase_request1 = PurchaseRequest(1000, '1')
    purchase_request2 = PurchaseRequest(100000, '2')
    purchase_request3 = PurchaseRequest(10000, '3')

    president = Approver('president', sys.maxsize)
    vice_president = Approver('vice_president', 11000, president)
    director = Approver('director', 1000, vice_president)

    director.process_request(purchase_request1)
    director.process_request(purchase_request2)
    director.process_request(purchase_request3)
