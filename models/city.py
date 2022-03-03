from config.context import sql


class CityModel(sql.Model):
    __tablename__ = 'city'

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(50))

    '''
    def __init__(self, city:str) -> None:
        self.name = city

    def to_dict(self):
        return self.__dict__
    '''
    