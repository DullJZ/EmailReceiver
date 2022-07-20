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


def save_mails(mail):
    pattern = re.compile(r'<.*?>')
    name = validate_name(str(mail.get('date'))) + '_' + validate_name(mail.get('subject')) + '.eml'
    if pattern.search(mail.get('to')):
        receiver = pattern.search(mail.get('to')).group()[1:-1]
    else:
        receiver = mail.get('to')
    if not os.path.exists('./emails/' + receiver):
        os.makedirs('./emails/' + receiver)
    zmail.save(mail, target_path='./emails/' + receiver,
               name=name, overwrite=True)


def validate_name(name):  # 验证文件名是否合法
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_name = re.sub(rstr, ".", name)  # 替换为.
    return new_name

# 登录POP3服务器
account, password, pop3_server, ssl, port = get_account_info()
server = zmail.server(account, password, pop_host=pop3_server, pop_ssl=ssl, pop_port=port)

# 检测是否登录成功
if server.pop_able():
    print('POP3 登录成功')

    # 判断已检索的ID
    if os.path.exists('./id_now.txt'):
        with open('./id_now.txt', 'r') as f:
            id_now = int(f.readline())
    else:
        id_now = 1
        with open('./id_now.txt', 'w') as f:
            f.write(str(id_now))
    # 最新ID
    id_latest = server.stat()[0]

else:
    raise Exception('POP3 配置错误')

# 循环监听邮件
while True:
    if id_now <= id_latest:
        mail = server.get_mail(id_now)

        if mail is not None:
            print('收到一封邮件')
            save_mails(mail)
            # 保存当前ID
            with open('./id_now.txt', 'w') as f:
                f.write(str(id_now))
            id_now += 1

    # 更新最新ID
    id_latest = server.stat()[0]
    time.sleep(1)
