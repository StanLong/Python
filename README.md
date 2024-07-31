# Python
Python从入门到放弃



爬虫 http://kmoon.fun/2022/spider/#%E7%88%AC%E8%99%AB%E6%A6%82%E5%BF%B5



快代理  https://www.kuaidaili.com/free/



----

**Linux安装python3**

系统：Centos7,  要安装的python版本 Python-3.9.11.tgz

```shell
# 安装python前需要先补包
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
# 解压安装
tar -zxf Python-3.9.11.tgz
cd Python-3.9.11
# 编译安装
./configure --prefix=/usr/local/python3.9
make
make install
# 创建软链接
ln -s /usr/local/python3/bin/python3.9 /usr/bin/python3.9
ln -s /usr/local/python3/bin/python3.9 /usr/bin/python3.9

# 配置pip下载源
touch ~/.pip/pip.conf
cat > ~/.pip/pip.conf << EOF
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
EOF

```



