from abc import ABC, abstractmethod


class apiClientBase(ABC):

    @abstractmethod
    def _cache(func, is_enabled):
        pass

    @abstractmethod
    def get(self, endpoint: str, **kwargs):
        pass

    @abstractmethod
    def post(self, endpoint: str, **kwargs):
        pass

    @abstractmethod
    def put(self, endpoint: str, **kwargs):
        pass

    @abstractmethod
    def patch(self, endpoint: str, **kwargs):
        pass

    @abstractmethod
    def get_cache(self, endpoint: str, **kwargs):
        pass

    @abstractmethod
    def set_cache(self, endpoint: str, result: str, **kwargs):
        pass
