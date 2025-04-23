from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    # DB_URL = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    DB_URL = "mysql+mysqlconnector://root:root@localhost:3307/fastapi"
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    REDIS_BROKER = "redis://localhost:6379/0"

settings = Settings()
