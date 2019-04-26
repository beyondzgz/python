#coding=utf-8
import os
import sys

if os.getuid()==0:
    pass
else:
    print('当前用户不是root用户')
    sys.exit(1)
version = raw_input('请输入python版本(2.7/3.7)')
if version == '2.7':
    url='https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz'
elif version == '3.7':
    url='https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz'
else:
    print('请输入正确的版本(2.7/3.7)')
    sys.exit(1)
cmd = 'wget '+url
ret = os.system(cmd)
if ret != 0:
    print('下载失败')
    sys.exit(1)

if version == '2.7':
    package = 'Python-2.7.16.tgz'
else:
    package = 'Python-3.7.3.tgz'
cmd = 'tar -xvf '+package
ret = os.system(cmd)
if ret != 0:
    os.system('rm -rf '+package)
    print('解压失败')
    sys.exit(1)

cmd = 'cd '+package+' && ./configure --prefix=/usr/local/pythonx && make && make install'
ret = os.system(cmd)
if ret != 0:
    print('编译源码失败')
    sys.exit(1)