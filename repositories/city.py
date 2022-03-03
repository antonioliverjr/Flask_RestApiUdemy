from models.city import CityModel


class CityRepository(CityModel):
    @classmethod
    def list(cls):
        return cls.query.all()
    
    def list_id(self):
        pass
    
    def create(self, **Kwargs):
        pass

    def uptade(self):
        pass

    def delete(self):
        pass

    @classmethod
    def search(cls, city:str):
        return cls.query.filter_by(name=city).first()