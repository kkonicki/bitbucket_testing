from core.selectors import (
    TopPanelSel,
    ProjectsSel,
    CreateRepositorySel,
    RepositoriesSel,
)


class WorkspacePage:

    def create_repository(
        self, sb, project_name: str, repo_name: str, include_readme=False
    ):
        sb.click(TopPanelSel.CREATE_BTN)
        sb.click(TopPanelSel.REPOSITORY_BTN)
        self.select_project(sb, project_name=project_name)
        if not include_readme:
            sb.click(CreateRepositorySel.INCLUDE_README_DD)
            sb.click(CreateRepositorySel.OPTION_NO)
        sb.update_text(selector=CreateRepositorySel.NAME_IB, text=repo_name)
        sb.click(CreateRepositorySel.CREATE_REPO_BTN)
        sb.wait_for_element_not_visible(CreateRepositorySel.CREATE_REPO_BTN)

    def open_projects(self, sb):
        sb.click(TopPanelSel.PROJECTS)

    def open_given_project(self, sb, project_name: str):
        sb.click(ProjectsSel.PROJECT(project_name))
        sb.wait_for_element_visible(ProjectsSel.ADD_REPO_BTN)

    def select_project(self, sb, project_name: str):
        sb.click(CreateRepositorySel.PROJECT_IB)
        sb.update_text(selector=CreateRepositorySel.NAME_IB, text=project_name)
        sb.click(CreateRepositorySel.PROJECT(project_name))

    def assert_project_exists(self, sb, project_name: str):
        sb.wait_for_element_visible(ProjectsSel.PROJECT(project_name))

    def assert_repository_exists(self, sb, repo_name: str):
        sb.wait_for_element_visible(RepositoriesSel.REPO_A(repo_name))
