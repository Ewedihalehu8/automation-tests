from selenium.webdriver.support.wait import WebDriverWait
from pages.login_locators import LoginPageLocations
from pages.login_locators import MainPageLocations
from pages.base_public_method import BasePage
from selenium.webdriver.support import expected_conditions as EC
class LoginPage(BasePage):
    # 1.输入用户名
    def enter_username(self, username):
        # 智能等待加载这个元素，等待加载用户名文本框
        WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*LoginPageLocations.username_text))
        # 用户名元素定位，加*是将远足格式拆成两个参数
        element = self.driver.find_element(*LoginPageLocations.username_text)
        element.click()
        element.clear()
        element.send_keys(username)
    # 2.输入密码
    def enter_password(self, password):
        WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*LoginPageLocations.password_text))
        element = self.driver.find_element(*LoginPageLocations.password_text)
        element.clear()
        element.send_keys(password)
    # 3.单击登录
    def click_button(self):
        element_click = self.driver.find_element(*LoginPageLocations.login_button)
        element_click.click()
    # 4.返回要验证的文本，登录成功
    def result_login_success(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(*MainPageLocations.user_name))
        return self.driver.find_element(*MainPageLocations.user_name)
