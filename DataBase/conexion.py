from sqlalchemy import create_engine

DATABSE_URL = 'sqlite:///./test.db' # ejemplo de conexion al SQLite

engine = create_engine(DATABSE_URL)
