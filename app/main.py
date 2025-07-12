from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from app.database import SessionLocal
from app.routes import products, categories, orders, banks, auth

app = FastAPI()

@app.get('/')
def home():
    return {"Message" : "Halo Bang Imat...."}

@app.get("/connection")
def check_db_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))  # ← pakai text()
        return {"status": "success", "message": "Connected to Supabase DB"}
    except SQLAlchemyError as e:
        return {"status": "fail", "error": str(e)}
    finally:
        db.close()

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(banks.router) 