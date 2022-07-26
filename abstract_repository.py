


import abc

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_by_id(self, id):
        pass

    @abc.abstractmethod
    def create(self, item):
        pass

    @abc.abstractmethod
    def update(self, item):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass