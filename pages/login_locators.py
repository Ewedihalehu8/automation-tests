from selenium.webdriver.common.by import By


class LoginPageLocations(object):
    username_text = (By.NAME, 'username')
    password_text = (By.NAME, 'password')
    login_button = (By.XPATH, '//button[@type="submit"]')

class MainPageLocations(object):
    user_img = (By.CLASS_NAME, "oxd-userdropdown-img")
    user_name = (By.CLASS_NAME, "oxd-userdropdown-name")
    menu_viewJobTitleList = (By.CLASS_NAME, "oxd-topbar-body-nav-tab-item")