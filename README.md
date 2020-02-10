## childmath
Python script used to generate child math problems with TKinter GUI. -- 这个python程序使用了TKinter GUI 包，可以产生儿童的数学题。

### How to use git command 

	1. 打开github，登陆自己的主页


	2. 点击Repositories 的New创建新的分支，把该填的填好


	3. 进入这new版本库的界面,点击这个Clone or download,然后复制这个链接（版本库名字是childmath）

	4. 进入linux操作系统，使用git clone命令将版本库lone下来。
         git clone https://github.com/elahw/childmath.git

	5. 接下来，进入childmath这个文件夹，之行git init操作

	6. 接下来是常规操作，git add ， git commit -m 
    
	7. 接下来是git push 操作，这时候可能会出现如下问题
        "error: The requested URL returned error: 403 Forbidden while accessing https://elahw@github.com/elahw/childmath.git/info/refs

        fatal: HTTP request failed"

        修正方法是，修改 .git/config :
        将  ：
        	#url = https://github.com/elahw/childmath.git
        改成：
	        url = https://elahw@github.com/elahw/childmath.git


    8. 这时候之行git push，可能会出现openSSH，这时候需要输入密码，密码是github的登录密码

