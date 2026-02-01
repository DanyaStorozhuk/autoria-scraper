from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DB_URL
from .models import Base, Car
from datetime import datetime

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def insert_car(car_data):
    with Session() as session:
        exists = session.query(Car).filter((Car.car_vin == car_data['car_vin']) | (Car.url == car_data['url'])).first()
        if exists:
            return  
        
        car = Car(
            url=car_data['url'],
            title=car_data['title'],
            price_usd=car_data['price_usd'],
            odometer=car_data['odometer'],
            username=car_data['username'],
            phone_number=car_data['phone_number'],
            image_url=car_data['image_url'],
            images_count=car_data['images_count'],
            car_number=car_data['car_number'],
            car_vin=car_data['car_vin'],
            datetime_found=datetime.now()
        )
        session.add(car)
        session.commit()