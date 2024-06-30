from sqlmodel import SQLModel, create_engine


sqlite_filename = "store.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

engine = create_engine(sqlite_url, echo=True)

# SQLModel.metadata.create_engine(engine)