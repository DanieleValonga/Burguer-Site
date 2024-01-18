import pytest
from app import app as my_server

@pytest.fixture()
def app():
    my_server.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield my_server

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
