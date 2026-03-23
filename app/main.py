from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="PV Direktvermarktung Beratung")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/impressum", response_class=HTMLResponse)
async def impressum(request: Request):
    return templates.TemplateResponse("impressum.html", {"request": request})


@app.get("/datenschutz", response_class=HTMLResponse)
async def datenschutz(request: Request):
    return templates.TemplateResponse("datenschutz.html", {"request": request})


@app.get("/danke", response_class=HTMLResponse)
async def danke(request: Request):
    return templates.TemplateResponse("danke.html", {"request": request})


@app.post("/kontakt", response_class=HTMLResponse)
async def kontakt(
    request: Request,
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    nachricht: Annotated[str, Form()] = "",
):
    logger.info(
        "Neue Kontaktanfrage",
        extra={"name": name, "email": email},
    )
    # TODO: send email notification
    return RedirectResponse(url="/danke", status_code=303)
