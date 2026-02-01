from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv('DB_URL', 'postgresql://postgres:password@db:5432/autoria_db')
SCRAPE_TIME = os.getenv('SCRAPE_TIME', '12:00')
DUMP_TIME = os.getenv('DUMP_TIME', '12:00')
START_URL = os.getenv('START_URL', 'https://auto.ria.com/uk/search/?categories.main.id=1&')