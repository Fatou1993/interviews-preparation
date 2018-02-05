from collections import deque
class User:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.book = None
        self.book_reader = None

    def disconnect(self, user):
        self.book_reader.disconnect()
        self.book_reader = None

    def turnPage(self):
        self.book.turn_page()

class Book:
    def __init__(self, id, title):
        self.title = title
        self.id = id
        self.curr_page = 0

    def turn_page(self):
        self.curr_page+=1

class BookReader:
    def __init__(self):
        self.curr_user = None
        self.curr_book = None
        self.book_player = BookPlayer(self)

    def read_book(self, user, book):
        if not self.curr_user : #there is not a curr user
            self.curr_user = user
            self.curr_user.book_reader = self
            self.curr_user.book = self.book_player.read(book)
        else:
            print "Someone is already using the reader. Come back later"

    def disconnect(self):
        self.curr_user = None


class BookPlayer:
    def __init__(self, book_reader):
        self.book_reader = book_reader
        self.curr_book = None
        self.book_page = None

    def read(self, book):
        if book == self.curr_book :
            return self.curr_book
        else :
            curr_book = "search in database"
            self.curr_book = curr_book
        return self.curr_book



class UserManager:
    def __init__(self, users):
        self.users = users #set of users stocked using their id

    def addUser(self, user):
        self.users.add(user.id)

    def removeUser(self, user):
        return self.users.remove(user.id)
