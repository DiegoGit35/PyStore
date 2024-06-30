from fastapi                import FastAPI

from models                 import *
from routes.user            import user_router
from routes.account         import account_router
from routes.carts           import cart_router
from routes.categories      import category_router
from routes.product         import product_router
from database.connection    import engine, SQLModel


app = FastAPI()


app.include_router(user_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(category_router)
app.include_router(account_router)



SQLModel.metadata.create_all(engine)
