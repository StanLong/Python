# logging 模块
# 功能
    # 日志格式的规范
    # 操作的简化
    # 日志分级的管理

# logging 模块的使用
    # 普通配置型 简单但可定制化差
    # 对象配置型 复杂但可定制化强

# 普通配置型 简单但可定制化差
# 日志分级
# debug < info < warning < error < critical
# 默认输出 warning 以上的日志
# import logging
#
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(name)s-%(levelname)s-%(message)s", datefmt='%a, %d %b %Y %H:%M:%S') # 可以打印包含 DEBUG 级别的日志
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# logging.basicConfig函数各参数:
# filename: 指定日志文件名
# filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
# format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
#     %(levelno)s: 打印日志级别的数值
#     %(levelname)s: 打印日志级别名称
#     %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
#     %(filename)s: 打印当前执行程序名
#     %(funcName)s: 打印日志的当前函数
#     %(lineno)d: 打印日志的当前行号
#     %(asctime)s: 打印日志的时间
#     %(thread)d: 打印线程ID
#     %(threadName)s: 打印线程名称
#     %(process)d: 打印进程ID
#     %(message)s: 打印日志信息
# datefmt: 指定时间格式，同time.strftime()
# level: 设置日志级别，默认为logging.WARNING
# stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略


# 对象配置型 复杂但可定制化强
# 创建一个logger对象
# 创建一个文件管理操作符
# 创建一个屏幕管理操作符
# 创建一个日志输出格式
# logger 绑定 文件管理操作符
# logger 绑定 屏幕管理操作符

import logging
logger = logging.getLogger() # 创建一个logger对象
fh = logging.FileHandler('logger.log') # 创建一个文件管理操作符
sh = logging.StreamHandler() # 创建一个屏幕管理操作符
ft1 = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s') # 创建一个日志输出格式
ft2 = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s') # 创建一个日志输出格式

# logger 绑定 文件管理操作符
fh.setFormatter(ft2)
logger.addHandler(fh)
# logger 绑定 屏幕管理操作符
sh.setFormatter(ft2)
logger.addHandler(sh)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

