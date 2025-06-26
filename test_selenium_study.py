import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get("http://localhost/orangehrm-5.7/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("zxtzxt")
driver.find_element(By.NAME, "password").send_keys("Zxt295470@")
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
time.sleep(2)
try:
    user_avatar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-img"))
    )
    assert user_avatar.is_displayed(), "登录失败：用户头像未显示"
except Exception as e:
    assert False, f"登录失败"
    username_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
    )
    print(f"登录用户: {username_element.text}")
time.sleep(2)

driver.find_element(By.XPATH,'//span[contains(@class,"oxd-text oxd-text--span oxd-main-menu-item--name")]').click()
try:
    work_button = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH,"//li[@class='oxd-topbar-body-nav-tab --parent']"))
    )
    work_button.click()
    job_level = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH,"//ul[contains(@class,'oxd-dropdown-menu')]//a[text()='职称']"))
    )
    job_level.click()
    add_level = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH,"//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary')]"))
    )
    add_level.click()
except Exception as e:
    print(f"操作过程中发生错误：{e}")


time.sleep(2)
driver.close()


