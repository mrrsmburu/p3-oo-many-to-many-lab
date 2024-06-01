 
class Book:
    _all_books = []

    def __init__(self, title):
        self.title = title
        Book._all_books.append(self)
    
    @classmethod
    def all_books(cls):
        return cls._all_books


class Author:
    _all_authors = []

    def __init__(self, name):
        self.name = name
        Author._all_authors.append(self)

    @classmethod
    def all_authors(cls):
        return cls._all_authors

    def contracts(self):
        return [contract for contract in Contract._all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book instance")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    _all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author instance")
        if not isinstance(book, Book):
            raise Exception("Invalid book instance")
        if not isinstance(royalties, (int, float)) or royalties < 0:
            raise Exception("Invalid royalties value")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract._all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls._all_contracts if contract.date == date]

    @classmethod
    def all_contracts(cls):
        return cls._all_contracts

