import pytest
from time import time

from assertpy import assert_that

from tests.API.core import list_repos, create_repo, delete_repo


@pytest.fixture()
def username():
    yield "mendio_bb"


@pytest.fixture()
def username():
    yield f"test_repo_{int(time())}"


def test_list_repos():
    response = list_repos(username)
    assert response is not None and response.status_code == 200, response.text


def test_create_repo(username, repo_name):
    response = create_repo(username, repo_name)
    assert_that(response).is_not_none()
    assert_that(response.status_code).is_in([200, 201])
    repos = list_repos(username).json()
    assert_that(repos["values"]).does_contain(repo_name)


def test_delete_repo(username, repo_name):
    response = delete_repo(username, repo_name)
    assert response is not None and response.status_code == 204, response.text
    repos = list_repos(username).json()
    assert_that(repos["values"]).does_not_contain(repo_name)
