import logging

def record(filename):
    # 1.创建一个logger对象
    logger = logging.getLogger() #创建一个logger对象
    logger.setLevel(logging.INFO)

    # 2.创建一个屏幕管理操作符
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)

    # 3.创建一个文件管理操作符
    fh = logging.FileHandler(filename)
    fh.setLevel(logging.INFO)

    # 4.创建一个日志输出格式
    formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    #5.操作符绑定日志格式
    sh.setFormatter(formater)
    fh.setFormatter(formater)

    # 6.绑定文件和屏幕管理操作符
    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger