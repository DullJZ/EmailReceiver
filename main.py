import re
import zmail
import os
import time


def get_account_info():
    with open('account.txt', 'r') as f:
        account = f.readline().split('\n')[0]
        password = f.readline().split('\n')[0]
        pop3_server = f.readline().split('\n')[0]
        if f.readline().split('\n')[0] != '0':
            ssl = True
        else:
            ssl = False
        port = int(f.readline())
    return account, password, pop3_server, ssl, port


def save_mails(mails):
    pattern = re.compile(r'<.*?>')
    for mail in mails:
        name = str(mail.get('date')).replace(':', '.') + '_' + mail.get('subject').replace(':', '.') + '.eml'
        receiver = pattern.search(mail.get('to')).group()[1:-1]
        if not os.path.exists('./emails/'+receiver):
            os.makedirs('./emails/'+receiver)
        zmail.save(mail, target_path='./emails/' + receiver,
                   name=name, overwrite=True)


# 登录POP3服务器
account, password, pop3_server, ssl, port = get_account_info()
server = zmail.server(account, password, pop_host=pop3_server, pop_ssl=ssl, pop_port=port)

# 检测是否登录成功
if server.pop_able():
    print('POP3 登录成功')
    id_latest = server.stat()[0]
else:
    raise Exception('POP3 配置错误')

# 循环监听新邮件
while True:
    mail = server.get_latest()
    if mail is not None and mail.get('id') > id_latest:
        print('收到一封邮件')
        save_mails([mail])
        id_latest = mail.get('id')
    time.sleep(1)
