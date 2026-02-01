from apscheduler.schedulers.blocking import BlockingScheduler
from .main import scrape
from .config import SCRAPE_TIME, DUMP_TIME, DB_USER, DB_NAME, DB_HOST
import os
import subprocess
from datetime import datetime

def dump_db():
    now = datetime.now()
    dump_file = f"dumps/dump_{now.strftime('%Y%m%d_%H%M')}.sql"


    env = os.environ.copy()
    env["PGPASSWORD"] = os.getenv("DB_PASSWORD", "")
    
    subprocess.run([
        "pg_dump",
        "-h", DB_HOST,
        "-U", DB_USER,
        "-d", DB_NAME,
        "-F", "p",
        "-f", dump_file
    ], env=env, check=True) 

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    
    
    scrape_hour, scrape_min = map(int, SCRAPE_TIME.split(":"))
    dump_hour, dump_min = map(int, DUMP_TIME.split(":"))
    
    scheduler.add_job(scrape,   "cron", hour=scrape_hour, minute=scrape_min)
    scheduler.add_job(dump_db,  "cron", hour=dump_hour,  minute=dump_min)
    
    print(f"Заплановано скрапінг на {SCRAPE_TIME} щодня")
    print(f"Заплановано дамп на {DUMP_TIME} щодня")
    
    scheduler.start()