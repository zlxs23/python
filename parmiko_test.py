# _*_coding:utf-8_*_

# 测试使用 paramiko 来驱动登录使用 linux 远程服务器

import paramiko


host = '...'
user = '...'
passwd = '...'

port = 22

if __name__ == '__main__':
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, user, passwd)
    stdin, stdout, sterr = client.exec_command('free')
    print(stdout.read())
    client.close()
