
class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.members.append(self)

class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        if royalties < 0 or royalties > 100:
            raise Exception("royalties must be between 0 and 100")
        
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.members.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.members if contract.date == date]

