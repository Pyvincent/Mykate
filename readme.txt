用来测试test.py
uwsgi --http :8001 --wsgi-file test.py


运行配置文件

 uwsgi --ini myweb_uwsgi.ini
 http://127.0.0.1:8099/


sudo apt-get install nginx  #安装
python3 -m pip install uwsgi 安装 uwsgi

 服务器在
 /etc/nginx/sites-available

/etc/init.d/nginx start  #启动
/etc/init.d/nginx stop  #关闭
/etc/init.d/nginx restart  #重启

新建一个服务器配置：
sudo vim /etc/nginx/sites-available/mykate.conf

激活网站：
sudo ln -s /etc/nginx/sites-available/mykate.conf /etc/nginx/sites-enabled/mykate.conf


测试配置语法问题
sudo service nginx configtest 或 /path/to/nginx -t


重启 nginx 服务器：
sudo service nginx reload 或 sudo service nginx restart 或 /path/to/nginx -s reload


/alidata/server/mysql/bin/mysqladmin -u root password '这里就是密码'

用root账号登录mysql

mysql -uroot -p
GRANT ALL PRIVILEGES ON *.* TO root IDENTIFIED BY "这里就是密码"

比如你想给某一个endpoint发送TCP请求
nc 192.168.0.11 8000 < data
就将data的内容发送到对端。
nc可以当做服务器，监听某个端口号
nc -l 8000 > received_data
把某一次请求的内容存储到received_data里。
上边只监听一次，如果多次可以加上-k参数

nc -lk 8000