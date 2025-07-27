import pytest
import os

@pytest.fixture(scope="session", autouse=True)
def set_env_vars():
    os.environ['ENV'] = "True"
    os.environ['OWNER_ID'] = "123456789"
    os.environ['TOKEN'] = "8232910553:AAGw6Uo4mg3Zu0JqNnZlsRUwfI4rz0MVMYk"
    os.environ['MONGO_DB_URI'] = "mongodb://localhost:27017/"
    os.environ['API_ID'] = "123456"
    os.environ['API_HASH'] = "0123456789abcdef0123456789abcdef"
