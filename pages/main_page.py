from core.data_sets import Urls
from core.selectors import TopPanelSel


class MainPage:
    def open_mainpage(self, sb):
        sb.open(Urls.BITBUCKET)
        sb.wait_for_element_visible(TopPanelSel.LOGIN_BTN)
