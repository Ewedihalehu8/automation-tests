import os
import shutil
import sys

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.get_path import get_par_path
from utils.log import conf
from utils.read_yaml import get_yaml_data

# 检查关键模块是否能被导入
try:
    from utils.get_path import get_par_path
    print("Successfully imported get_par_path")
except Exception as e:
    print(f"Failed to import get_par_path: {e}")

sys.path.append('../..')


@allure.step("从配置文件中读取登录数据")
@pytest.fixture
def login_data():
    log = conf.logcon()
    log.info("read config.yaml")
    yaml_path = os.path.join(get_par_path(), "config/config.yaml")
    # test_data = get_yaml_data(yaml_path)
    return get_yaml_data(yaml_path)


@allure.step("0.这是初始化数据")
@pytest.fixture
def request_data(request):
    # value  =request.param
    return request.param

@allure.feature('打开浏览器')
@pytest.fixture(scope='session',autouse=True)
def init_driver(request):
    log = conf.logcon()
    log.info('setup_class')
    # service = Service(get_par_path())
    service = Service(executable_path='chromedriver')
    driver = webdriver.Chrome(service=service)
    # driver_path = os.path.join(get_par_path(),"driver/chromedriver")
    # driver = webdriver.Chrome(executable_path=driver_path)

    def close_browser():
        driver.quit()

    request.addfinalizer(close_browser)
    return driver


# 测试报告清除
@pytest.fixture(scope="session", autouse=True)
def cleanup():
    # 测试前清除旧结果
    if os.path.exists("allure-result"):
        shutil.rmtree("allure-result")
    yield
    # 测试后生成报告
    os.system("allure generate allure-result -o allure-report --clean")