from dependency_injection.services import UserServiceImpl
from dependency_injection.interface import UserService


class DependencyContainer:
    def __init__(self):
        self.services = {}

    def get_user_service(self) -> UserService:
        if "user_service" not in self.services:
            self.services["user_service"] = UserServiceImpl()
        return self.services["user_service"]

dependency_container = DependencyContainer()
