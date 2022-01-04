# configparser 模块
# configparser 加载setting文件
# setting文件格式
    # [] 中括号里的内容称为小结 section
    # key=value 成为 option

import configparser
config = configparser.ConfigParser()
config.read('setting')
print(config.sections())
# ['path']
print(config['path']['user_info'])
# F:\sys\abc