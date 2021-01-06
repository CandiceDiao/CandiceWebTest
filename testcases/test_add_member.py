from page.main_page import MainPage


class TestAddMember():

    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):

        #1.点击添加成员，跳转到添加成员页面2.填写成员信息3.点击保存
        #4.断言是否添加成功
        assert "维恩" in self.main.goto_add_member().add_member().get_member()

    def test_add_member_fail(self):
        assert "维恩2" not in self.main.goto_add_member().add_member_fail().get_member()

    def teardown(self):
        self.main.quit()

