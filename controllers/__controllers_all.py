from controllers.auth_controller import user, token
from models.identity.role_dto import role
from controllers.hotel_controller import hotel
from controllers.city_controller import city

''' Add Namespace on screen for startup. '''
namespaces = [
    user,
    role,
    token,
    hotel,
    city
]