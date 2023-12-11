from abc import ABC, abstractmethod


class UserService(ABC):
    @abstractmethod
    def create_user(self, user_data):
        pass
