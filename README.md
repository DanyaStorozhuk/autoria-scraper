# 🏨 AutoRia Scraper

This project is an application for periodic scraping of the AutoRia platform (used cars).
The application runs daily, iterates through all pages with car listings, visits each individual car page, and stores the collected data in a PostgreSQL database without duplicates, which allows viewing only unique car listings.

---

## 🛠 Tech Stack

- Python 3.12  
- Selenium + webdriver-manager (scraping)  
- SQLAlchemy (database operations)  
- PostgreSQL  
- APScheduler (task scheduler)  
- python-dotenv (.env configuration)  
- Docker & Docker Compose (deployment)  
- pip (package manager)

## 🚀 Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/USERNAME/autoria-scraper.git
    cd autoria-scraper
    ```

2. **Set Up a Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    Install Dependencies:
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create and Configure .env File:**:

    ```bash
    - Create a .env file in the project
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=autoria

    DB_URL=postgresql://postgres:postgres@db:5432/autoria

    START_URL=https://auto.ria.com/uk/search/?categories.main.id=1&country.import.usa.not=-1&price.currency=1&abroad.not=0&custom.not=1&sort[0].add_date.order=desc&page=0&size=100
    SCRAPE_TIME=12:00
    DUMP_TIME=12:00
    ```

5. **Run with Docker**:

    ```bash
    docker compose up --build
    ```

6. **Local Run (testing)**:

    ```bash
    python app/main.py

    -- Start the scheduler (will wait for the scheduled time):

    python app/scheduler.py
    ```
7. **Verification**:
    ```bash
    docker compose exec db psql -U postgres -d autoria

    Inside psql:
    SELECT * FROM cars LIMIT 5;
    ```
8. **Stopping**:
    ```bash
    docker compose down
    ```

## 📌 Author
Danya Storozhuk
GitHub: https://github.com/DanyaStorozhuk