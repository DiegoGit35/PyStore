from sqlmodel import SQLModel, create_engine


sqlite_filename = "store.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

engine = create_engine(sqlite_url, echo=True)

def get_session():
   with Session(engine_url) as session:
       yield session

# SQLModel.metadata.create_engine(engine)