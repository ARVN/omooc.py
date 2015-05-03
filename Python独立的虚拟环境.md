# Python独立的虚拟环境

> pyenv是一个Python多版本管理工具，他设计精巧，通过巧妙的方法，可以使多版本的Python共存在一个操作系统能，简单的实现切换，或者更具项目使用不同的Python。

pyenv支持插件且和virtualenv完美结合，实现多版本，多环境的控制，不同项目，运行各自完全隔离的环境。



## 安装+使用步骤

以下是我练习Python+Django搭建blog的基础准备/备忘，其中Pyenv+Virtualenv 搭建开发环境的部分步骤

### 安装pyenv

Pyenv-Virtualenv  好用，并且作者很贴心 直接使用[pyenv-installer](https://github.com/yyuu/pyenv-installer)完成两者的安装，只需要在终端执行:

`curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash`

该一脚本并安装了插件[pyenv-virtualenv] 帮助我们整合使用virtualenv

### 使用

- pyenv可安装python列表


``` 
$ pyenv install -l                              2.2.1p85
Available versions:
  2.1.3
```

- 安装python3.4.3


``` 
#安装python 3.4.3

$ pyenv install 3.4.3                           2.2.1p85
Downloading Python-3.4.3.tgz...
-> https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz
Installing Python-3.4.3...
Installed Python-3.4.3 to /Users/ArvinYu/.pyenv/versions/3.4.3
```

- 使用命令创建3.4.3 的虚拟环境 （命名为my_blog)


``` 
$ pyenv virtualenv 3.4.3 my_blog
```

- 命令：`pyenv virtualenvs` 查看已有的虚拟环境


``` 
$ pyenv virtualenvs                             2.2.1p85
  my_blog (created from /Users/ArvinYu/.pyenv/versions/3.4.3)
```

- 系统当下安装着的python环境


``` 
$; pyenv versions                                2.2.1p85
* system (set by /Users/ArvinYu/.python-version)
  3.4.3
  anaconda-2.0.1
  my_blog
```

- 激活my_blog 项目 （基于python3.4.3的开发环境）
  
  ``` 
  ArvinYu at yandongdeMacBook-Pro in ~/.pyenv on master
  :$; pyenv activate my_blog                        2.2.1p85
  (my_blog)
  ```
  
  - 在其中安装django
    
  - ``` 
    ArvinYu at yandongdeMacBook-Pro in ~/.pyenv on master
    :$; pip install django                 (my_blog)  2.2.1p85
    You are using pip version 6.0.8, however version 6.1.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
    Collecting django
      Downloading Django-1.8.1-py2.py3-none-any.whl (6.2MB)
        100% |################################| 6.2MB 78kB/s
    Installing collected packages: django
    
    Successfully installed django-1.8.1
    (my_blog)
    ```
    
  
- 退出当前虚拟开发环境
  
  ``` 
  ArvinYu at yandongdeMacBook-Pro in ~/.pyenv on master
  :$; pyenv deactivate my_blog           (my_blog)  2.2.1p85
  ```
  




- 删除错误命名的开发环境
  
  ``` 
  ArvinYu at yandongdeMacBook-Pro in ~/.pyenv on master
  :$; rm -rf ~/.pyenv/versions/my_bolg/             2.2.1p85
  ```
  
  - 还可以使用命令 `pyenv uninstall`  my_bolg （my_bolg是我要删除的my-virtual-env）
    
    ​
    
  
- 使用Django创建 myblog项目
  
- ``` 
  ArvinYu at yandongdeMacBook-Pro in ~/.pyenv on master
  :$; django-admin.py startproject myblog
  (my_blog)
  
  :$; tree                               (my_blog)  2.2.1p85
  .
  |____manage.py
  |____myblog
  | |______init__.py
  | |____settings.py
  | |____urls.py
  | |____wsgi.py
  (my_blog)
  ```
  
  ​
  




