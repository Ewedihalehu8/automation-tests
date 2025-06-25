from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.job_title_locators import JobTitleLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.base_public_method import BasePage


class AddJobTitlePage(BasePage):
    # 进入职称页面
    def click_movetoelement_job(self):
        self.driver.find_element(*JobTitleLocators.admin_page).click()
        self.driver.find_element(*JobTitleLocators.work_list).click()
        self.driver.find_element(*JobTitleLocators.jobTitle_page).click()
    # 点击添加职称按钮
    def click_add_jobtitle(self):
        element = self.driver.find_element(*JobTitleLocators.jobTitle_page)
        element.click()
    # 输入jobtitle
    def enter_jobTitle(self,jobTitle):
        # 智能等待加载职称名文本框
        WebDriverWait(self.driver,10).until(
            lambda driver:driver.find_element(*JobTitleLocators.jobTitle_name)
        )
        element = self.driver.find_element(*JobTitleLocators.jobTitle_name)
        element.click()
        element.clear()
        element.send_keys(jobTitle)
    # 输入description
    def enter_jobDescription(self,Description):
        WebDriverWait(self.driver,10).until(
            lambda driver:driver.find_element(*JobTitleLocators.jobTitle_description)
        )
        element = self.driver.find_element(*JobTitleLocators.jobTitle_description)
        element.send_keys(Description)
    # 上传文件
    def enter_jobfile_upload(self,filename):
        WebDriverWait(self.driver,10).until(
            lambda driver:driver.find_element(*JobTitleLocators.jobTitle_file_upload)
        )
        element = self.driver.find_element(*JobTitleLocators.jobTitle_file_upload)
        element.send_keys(filename)
    # 输入备注
    def enter_jobNote(self,jobNote):
        WebDriverWait(self.driver,10).until(
            lambda driver:driver.find_element(*JobTitleLocators.jobTitle_note)
        )
        element = self.driver.find_element(*JobTitleLocators.jobTitle_note)
        element.send_keys(jobNote)
    # 点击提交
    def click_submit_job(self):
       element_click = self.driver.find_element(*JobTitleLocators.jobTitle_sumit)
       element_click.click()

    # 返回要验证的文本
    def result_addjobtitle(self):
        elements = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border']")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(elements)
        )
        # 检查目标职级是否存在
        return len(elements) > 0