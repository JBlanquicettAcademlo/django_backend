


from abstract_repository import AbstractRepository

class UserRepository(AbstractRepository):

    def __init__(self, session) -> None:

        self.session = session

    def get_all(self):
        #session.query(User).all()
        return ['jorge', 'armando', 'pepito', 'juan']

    def get_by_id(self, id):
        ...

    def create(self, item):
        ...

    def update(self, item):
        ...

    def delete(self, id):
        ...