import sys
from logbook import Logger, StreamHandler,FileHandler


class conf():
    @staticmethod
    def logcon():
        log = Logger('HRM系统测试自动化日志')
        StreamHandler(sys.stdout).push_application()
        FileHandler("/Users/ewedihalehu/PycharmProjects/orangeHRM/log/pytest_log.log").push_application()
        return log