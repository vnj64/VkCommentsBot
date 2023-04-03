from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TOKEN")

host = os.getenv("DATABASE_HOST")
password = os.getenv("DATABASE_PASSWORD")
user = os.getenv("DATABASE_USER")
name = os.getenv("DATABASE_NAME")
port = os.getenv("DATABASE_PORT")
