from sqlmodel import SQLModel, create_engine, Session


sqlite_filename = "store.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

engine = create_engine(sqlite_url, echo=True)

def get_session() -> Session:
   with Session(engine) as session:
       yield session

# SQLModel.metadata.create_engine(engine)