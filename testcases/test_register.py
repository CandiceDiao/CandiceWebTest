from page.main_page import MainPage


class TestRegister:

    def setup(self):
        self.main = MainPage()

    def test_register(self):
        assert self.main.go_to_register().register()

