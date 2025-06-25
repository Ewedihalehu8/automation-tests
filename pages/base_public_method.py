class BasePage(object):
    # 初始化是在类加载时加载的方法，在浏览器打开的基础上初始化浏览器参数
    # 初始化打开浏览器
    def __init__(self, driver):
        self.driver = driver
    def save_picture(self,filepath):
        self.driver.save_screenshot(filepath)