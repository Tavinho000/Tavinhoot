# recreate_db.py
from sqlalchemy import create_engine
from models import Base  # ou de onde você define seus modelos

engine = create_engine("sqlite:///db.sqlite3")
Base.metadata.create_all(engine)

print("Banco recriado com sucesso.")
