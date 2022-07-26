

from repository import UserRepository

class UserUOW:

    def __init__(self, session_factory):
        self.session = session_factory
        self.user = UserRepository(session_factory)

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
