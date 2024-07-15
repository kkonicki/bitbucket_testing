class BranchesSel:
    CREATE_BRANCH = '//span[text()="Create branch"]'


class CreateRepositorySel:
    CREATE_REPO_BTN = '//button[text()="Create repository"]'
    NAME_IB = 'input[name="name"]'
    REPOSITORY_NAME_IB = '//span[text()="Add repositories"]'
    PROJECT_IB = '//span[text()="Select project"]'
    PROJECT = lambda name: f'//span[text()="{name}"]'
    INCLUDE_README_DD = '//div[@id="s2id_id_readme_type"]'
    OPTION_NO = '//div[text()="No"]'


class LoginFormSel:
    CONTINUE_BTN = 'button[id="login-submit"]'
    USERNAME = '//input[@id="username"]'
    PASSWORD = '//input[@id="password"]'
    LOGIN_BTN = 'button[id="login-submit"]'


class ProjectsSel:
    PROJECT = lambda name: f'//a[text()="{name}"]'
    ADD_REPO_BTN = '//span[text()="Add repositories"]'


class TopPanelSel:
    LOGIN_BTN = 'a[data-label="Log in"][class="imkt-navbar__link-list-link"]'
    PROFILE_BTN = '//button[@data-testid="profile-button"]'
    PROJECTS = '//span[text()="Projects"]'
    CREATE_BTN = '//span[text()="Create"]'
    REPOSITORY_BTN = '//span[text()="Repository"]'
    LOGOUT_BTN = '//span[text()="Log out"]'


class RepositoriesSel:
    REPO_A = lambda name: f'//div/h1[text()="{name}"]'


class SourceTabSel:
    REPO_HEADER = lambda repo_name: f'//h1[text()="{repo_name}"]'
    THREE_DOTS = '//span[@aria-label="Repository actions"]'
    ADD_FILE = '//span[text()="Add file"]'
    FILE_NAME_IB = '//input[@id="filename"]'
    CODE_IB = '//span[@role="presentation"]'
    COMMIT_BTN = '//button[text()="Commit"]'
    COMMIT_PANEL_BTN = '//div[@class="dialog-button-panel"]/button[text()="Commit"]'
