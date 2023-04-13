import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(r'../.env')
load_dotenv(dotenv_path=env_path)
DATABASE_URL = os.environ.get("DATABASE_PATH")
