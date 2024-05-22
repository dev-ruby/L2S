from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .db import get_db_session
from .models import Url
from .utils import generate_new_hash

app = FastAPI(docs_url=None, redoc_url=None)

origins = ["http://localhost:3000", "https://l2s.kro.kr", "http://l2s.kro.kr"]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)


class UrlForm(BaseModel):
    custom_link: str
    original_link: str


@app.get("/{url}")
def redirect(url: str, db: Session = Depends(get_db_session)):
    target = db.query(Url).get(url)
    if target:
        return RedirectResponse(target.target_url)
    else:
        return RedirectResponse("https://l2s.kro.kr")


@app.post("/api/create")
def main(
    url_form: UrlForm,
    db: Session = Depends(get_db_session),
):
    new_url = url_form.custom_link
    original_url = url_form.original_link

    code = 1

    new_url = new_url.replace(" ", "")

    if new_url:
        if db.query(Url).get(new_url):
            new_url = None
            code = 2
        elif len(new_url) > 20 or "/" in new_url or "api" in new_url:
            new_url = None
            code = 3
    else:
        new_url = generate_new_hash(original_url, db)

    if code == 1:
        db.add(Url(shorted_url=new_url, target_url=original_url))
        db.commit()

    return {"code": code, "new_url": new_url}
