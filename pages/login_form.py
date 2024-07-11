from core.data_sets import LoginData
from core.selectors import TopPanelSel, LoginFormSel


class LoginForm:
    def open_login_form(self, sb):
        sb.click(TopPanelSel.LOGIN_BTN)
        sb.wait_for_element_visible(LoginFormSel.CONTINUE_BTN)

    def insert_creds(self, sb, creds: LoginData):
        sb.update_text(selector=LoginFormSel.USERNAME, text=creds.value["login"])
        sb.click(LoginFormSel.CONTINUE_BTN)
        sb.update_text(selector=LoginFormSel.PASSWORD, text=creds.value["password"])

    def click_login(self, sb):
        sb.click(LoginFormSel.LOGIN_BTN)

    def assert_user_logged_in(self, sb):
        sb.wait_for_element_visible(TopPanelSel.PROFILE_BTN)

    def log_out(self, sb):
        sb.click(TopPanelSel.PROFILE_BTN)
        sb.click(TopPanelSel.LOGOUT_BTN)
        sb.wait_for_element_visible(LoginFormSel.CONTINUE_BTN)