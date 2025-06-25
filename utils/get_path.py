import os


def get_par_path():
    root_path =os.path.abspath(os.path.dirname(__file__)).split('utils')[0]
    # 返回路径为根路径
    return root_path