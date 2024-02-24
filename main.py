from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.users import user_router
from routes.events import event_router
import uvicorn
from database.connection import conn

app = FastAPI()

# enroll router
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# app 실행 시 conn 사용하여 디비 생성
@app.on_event("startup")
def on_startup():
    conn()

app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
