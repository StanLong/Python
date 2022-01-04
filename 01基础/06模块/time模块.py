import time

# print(time.time()) # 时间戳
# print(time.strftime('%Y-%m-%d %H:%M:%S')) # 格式化时间戳
# print(time.strftime('%c')) # 外国人的时间格式

# 结构化时间
# time_obj = time.localtime()
# print(time_obj)
# time.struct_time(tm_year=2021, tm_mon=3, tm_mday=3, tm_hour=19, tm_min=45, tm_sec=24, tm_wday=2, tm_yday=62, tm_isdst=0)
# print(time_obj.tm_year)
# print(time_obj.tm_mon)
# print(time_obj.tm_mday)
# print(time_obj.tm_wday)
# print(time_obj.tm_yday)

# 时间戳格式转换
# 时间戳格式转换成年月日格式
# time_obj = time.localtime(1614772265)
# print(time_obj)
# format_time = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
# print(format_time)

# 年月日格式转时间戳
# 2021-03-03 19:51:05
# struct_time = time.strptime('2021-03-03 19:51:05', '%Y-%m-%d %H:%M:%S')
# print(time.mktime(struct_time))

# 注意 time.strptime 和 time.strftime 参数不一样

# 计算本月一号的时间戳
# 方式一
# struct_time = time.localtime()
# struct_time = time.strptime('%s-%s-1' %(struct_time.tm_year, struct_time.tm_mon), '%Y-%m-%d')
# print(time.mktime(struct_time))

# 方式二
# time_f = time.strftime('%Y-%m-01')
# struct_time = time.strptime(time_f, '%Y-%m-%d')
# print(time.mktime(struct_time))

# python 时间戳格式转换
# format_string --------(strptime)> struct_time
# struct_time --------(strftime)> format_string
# struct_time --------(mktime)> timestamp
# timestamp --------------(localtime gmtime)> struct_time
