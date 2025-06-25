from datetime import datetime
import allure,os
import pytest
from utils.log import conf
from pages.add_jobtitle_method import AddJobTitlePage
from pages.base_public_method import BasePage
from pages.login_method import LoginPage
from utils.get_path import get_par_path
from utils.read_yaml import get_yaml_data


with allure.step('0.从数据文件中读取添加职称数据信息'):
    yaml_path = os.path.join(get_par_path(),"config/config.yaml")
    test_data = get_yaml_data(yaml_path)

class TestClass(object):
    # @allure.step("从配置文件中读取登录数据")
    # @pytest.fixture
    # def login_data(self):
    #     self.log = conf.logcon()
    #     self.log.info("read config.yaml")
    #     yaml_path = os.path.join(get_par_path(),"config/config.yaml")
    #     test_data = get_yaml_data(yaml_path)
    #     return test_data

    @allure.feature("登录功能")
    @allure.step("使用zxtzxt账号登录")
    def test_login(self,init_driver,login_data):
        self.log.info("login")
        init_driver.get(login_data["baseURL"]+"/symfony/web/index.php/auth/login")
        init_driver.maximize_window()
        init_driver.implicitly_wait(20)
        base_page = BasePage(init_driver)
        with allure.step("初始化登录页"):
            login_page = LoginPage(init_driver)
        with allure.step("输入用户名级密码后单击登录"):
            login_page.enter_username(login_data["username"])
            login_page.enter_password(login_data["password"])
            login_page.click_button()
        with allure.step("断言admin是否登录成功并截图"):
            assert "zxtzxt" in login_page.result_login_success()
            pic_path = os.path.join(get_par_path(),"shootpicture/")
            base_page.save_picture(pic_path+str(datetime.now())+'login.png')

    # @allure.step("0.这是初始化数据")
    # @pytest.fixture
    # def get_data(request):
    #     value = request.param
    #     return value



    @allure.feature("添加职称功能")
    @pytest.mark.parametrize("request_data",test_data,indirect=True)
    def test_2add_jobTitle(self,init_driver,request_data):
        jobTitle = request_data['jobTitle']
        jobDescription = request_data['description']
        note_text = request_data['note_text']
        base_page = BasePage(init_driver)
        addJobTitle_page = AddJobTitlePage(init_driver)
        with allure.step("1.进入职称页"):
            addJobTitle_page.click_movetoelement_job()
            addJobTitle_page.click_add_jobtitle()
        with allure.step("2.输入信息"):
            addJobTitle_page.enter_jobTitle(jobTitle)
            addJobTitle_page.enter_jobDescription(jobDescription)
            addJobTitle_page.enter_jobNote(note_text)
        with allure.step("3.上传文件"):
            data_path = os.path.join(get_par_path(),"datafile")
            addJobTitle_page.enter_jobTitle(data_path+"/20250623160911.jpg")
        with allure.step("4.提交保存"):
            addJobTitle_page.click_submit_job()
        with allure.step("5.断言添加成功并截图"):
            assert jobTitle in init_driver.page_source
            pic_path = os.path.join(get_par_path(),"shootpicture/")
            pic_name = pic_path+str(datetime.now())+'_addjob,png'
            base_page.save_picture(pic_name)
            allure.attach.file(pic_name,attachment_type=allure.attachment_type.PNG)