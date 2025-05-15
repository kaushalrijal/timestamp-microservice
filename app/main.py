from datetime import datetime, timezone

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.routes import router as api_router
from app.config import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/now")
def get_current_timestamp():
    now_utc = datetime.now(timezone.utc)
    unix_time = int(now_utc.timestamp())
    utc_time = now_utc.isoformat()

    return {"utc": utc_time, "unix": unix_time}


app.include_router(api_router, prefix="/api")
