from datetime import datetime
from typing import Optional

import random

from flask import Blueprint, request, render_template, redirect, url_for

import utils
from app import db
from utils import get_hash
from models import Uri

bp = Blueprint("main", __name__, url_prefix="/")


def is_exist_url(new_url: str):
    return bool(Uri.query.get(new_url))


def create_hash_url(data: str) -> str:
    _hash = get_hash(data)
    if is_exist_url(_hash):
        return create_hash_url(_hash)
    else:
        return _hash


def commit_url(original_url: str, new_url: str) -> None:
    uri = Uri(
        shorted_url=new_url,
        target_url=original_url
        .replace("https://", "", 1)
        .replace("http://", "", 1),
        create_date=datetime.now(),
    )

    db.session.add(uri)
    db.session.commit()


def create_new_url(original_url: str, new_url: Optional[str] = None):
    if new_url:
        if len(new_url) <= 20:
            if not is_exist_url(new_url):
                commit_url(original_url, new_url)
                return render_template("create_success.html", new_url=new_url)
            else:
                return redirect("/")
        else:
            return redirect("/")
    else:
        new_url = create_hash_url("".join(random.sample(original_url, len(original_url)-1)))
        commit_url(original_url, new_url)
        return render_template("create_success.html", new_url=new_url)


@bp.route("/create", methods=["POST"])
def create():
    return create_new_url(request.form["origin_url"], request.form["new_url"])
