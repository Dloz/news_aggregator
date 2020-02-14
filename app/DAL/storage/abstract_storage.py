from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @abstractmethod
    def store(self, model):
        pass

    @abstractmethod
    def store_many(self, models):
        pass

    @abstractmethod
    def pagination(self, page, col_name):
        pass
