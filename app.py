import flask
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db: SQLAlchemy = SQLAlchemy()
migrate = Migrate()


def page_not_found(e=None):
    return render_template("404.html"), 404


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    import models

    from views import main

    app.register_blueprint(main.bp)

    app.register_error_handler(404, page_not_found)

    @app.route("/")
    def main():
        return render_template("main.html")

    @app.route("/s/<url>")
    def redirect_url(url):
        target = models.Uri.query.get(url)
        if target:
            return flask.redirect("https://" + target.target_url)
        else:
            return page_not_found(), 404

    return app
