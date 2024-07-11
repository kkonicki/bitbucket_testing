from parameterized import parameterized
from seleniumbase import BaseCase

from core.data_sets import LoginData
from pages.login_form import LoginForm
from pages.main_page import MainPage
from pages.src_page import SrcPage
from pages.workspace_page import WorkspacePage

from time import time


class BitbucketE2E(BaseCase):
    def setUp(self, **kwargs) -> None:
        super(BitbucketE2E, self).setUp()

    @parameterized.expand([["test_project", f"test_repo_{time()}"]])
    def test_e2e_actions(self, project_name, repo_name):
        MainPage().open_mainpage(self)
        LoginForm().open_login_form(self)
        LoginForm().insert_creds(self, creds=LoginData.USER1)
        LoginForm().click_login(self)
        LoginForm().assert_user_logged_in(self)
        WorkspacePage().open_projects(self)
        WorkspacePage().assert_project_exists(self, project_name)
        WorkspacePage().open_given_project(self, project_name)
        WorkspacePage().create_repository(
            self, project_name=project_name, repo_name=repo_name
        )
        WorkspacePage().assert_repository_exists(self, repo_name=repo_name)
        SrcPage().add_file(self, "README.md", "readme placeholder")
        LoginForm().log_out(self)
