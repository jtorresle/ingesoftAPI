from sqlalchemy import MetaData, create_engine

engine = create_engine("mysql+pymysql://root:957846Oso@localhost:3306/ingesoft",connect_args={"autocommit" : True})

meta = MetaData()

conn = engine.connect()

