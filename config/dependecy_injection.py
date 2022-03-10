import inject
from data.interfaces.__interfaces_all import *
from data.repositories.__repositories_all import *

class DependencyInjection:
    @staticmethod
    def __ioc_config(binder):
        binder.bind(ICityRepository, CityRepository)

    @staticmethod
    def register_ioc():
        inject.configure(DependencyInjection.__ioc_config)