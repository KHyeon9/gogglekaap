import os
from dotenv import load_dotenv

load_dotenv()

db_env = os.environ.get('SQLALCHEMY_DATABASE_URI')
print(db_env)