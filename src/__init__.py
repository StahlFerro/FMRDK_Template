import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    # )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        if os.environ.get("FLASK_ENV") == "development":
            app.config.from_object("config.DevelopmentConfig")
        elif os.environ.get("FLASK_ENV") == "production":
            app.config.from_object("config.ProductionConfig")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    print(app.config)

    from flask_mongoengine import MongoEngine
    db = MongoEngine()
    from src.resource import api
    api.init_app(app)
    db.init_app(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app
