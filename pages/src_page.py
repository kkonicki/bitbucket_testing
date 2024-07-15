from core.selectors import SourceTabSel


class SrcPage:
    def click_three_dots(self, sb):
        sb.click(SourceTabSel.THREE_DOTS)

    def add_file(self, sb, filename: str, text: str):
        self.click_three_dots(sb)
        sb.click(SourceTabSel.ADD_FILE)
        sb.update_text(SourceTabSel.FILE_NAME_IB, filename)

        sb.click(SourceTabSel.CODE_IB)
        sb.click("//div[@class='CodeMirror-scroll']")
        sb.execute_script(
            """
        var editor = document.querySelector('.CodeMirror').CodeMirror;
        editor.setValue(arguments[0]);
        """,
            text,
        )

        sb.click(SourceTabSel.COMMIT_BTN)
        sb.click(SourceTabSel.COMMIT_PANEL_BTN)
        sb.wait_for_element_visible(SourceTabSel.THREE_DOTS)
