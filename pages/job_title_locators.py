from selenium.webdriver.common.by import By


class JobTitleLocators(object):
    # 管理员页面
    admin_page = (By.XPATH,'//span[contains(@class,"oxd-text oxd-text--span oxd-main-menu-item--name")]')
    # 工作下拉框
    work_list =  (By.XPATH,"//li[@class='oxd-topbar-body-nav-tab --parent']")
    # 进入职称页面
    jobTitle_page = (By,"//ul[contains(@class,'oxd-dropdown-menu')]//a[text()='职称']")
    # 添加职级按钮
    jobTitle_addButton = (By.XPATH, "//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary')]")
    # 职称输入框
    jobTitle_name = (By.XPATH,"//div//input[@class='oxd-input oxd-input--active']")
    # 职称描述
    jobTitle_description = (By.XPATH,"//div//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
    # 文件上传
    jobTitle_file_upload = (By.XPATH,"//div//div[@class='oxd-file-button']")
    # 备注
    jobTitle_note = (By.XPATH,"//div//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
    # 提交按钮
    jobTitle_sumit = (By.XPATH,"//button[contains(@class,'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]")
    buttonAdd = (By.XPATH,"")
