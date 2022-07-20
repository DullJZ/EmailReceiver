# EmailReceive
使用 EmailReceiver 接收邮件并用收件人加以区分

主要用途嘛，配合域名邮件转发做到临时邮箱的效果
## 使用方法
1. 安装
    ```bash
   git clone https://github.com/DullJZ/EmailReceiver
   pip install zmail
    ```
2. 配置

   创建`account.txt`文件，内容为：
   ```
   POP3邮箱，示例：xxxxx@hotmail.com
   POP3密码，示例：password
   POP3服务器地址，示例：outlook.office365.com
   是否使用SSL（是填1，否填0），示例：1
   POP3端口，示例：995
   ```
3. 使用
    ```bash
   cd EmailReceiver
   python main.py
    ```
## 鸣谢
1. [zmail](https://github.com/zhangyunhao116/zmail)
2. [PyCharm](https://www.jetbrains.com/pycharm/)
## 打赏
本项目完全免费且公开提供，如果你喜欢这个项目，请赏作者一杯咖啡！


<center class="half">
    <img src="./hongbaoma.jpg" alt="支付宝红包码" style="zoom: 25%;" /><img src="./zfb.jpg" alt="支付宝" style="zoom:25%;" />
</center>