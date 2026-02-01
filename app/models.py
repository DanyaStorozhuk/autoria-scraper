from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    title = Column(String)
    price_usd = Column(Integer)
    odometer = Column(Integer)
    username = Column(String)
    phone_number = Column(String)
    image_url = Column(String)
    images_count = Column(Integer)
    car_number = Column(String)
    car_vin = Column(String)
    datetime_found = Column(DateTime)
