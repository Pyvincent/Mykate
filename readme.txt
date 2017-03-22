用来测试test.py
uwsgi --http :8001 --wsgi-file test.py


运行配置文件

 uwsgi --ini myweb_uwsgi.ini


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
