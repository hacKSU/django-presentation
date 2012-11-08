#Introduction to Django

##Installing Django

###Mac/Unix
1. Download [Django-1.4.2.tar.gz](https://www.djangoproject.com/download/1.4.2/tarball/)
2. Run the following commands in terminal:

```
tar xzvf Django-1.4.2.tar.gz
cd Django-1.4.2
sudo python setup.py install
```

###PC
1. Download and install Python 2.7 if you dont have it. (http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi)
2. Download Django (https://github.com/django/django/zipball/master)
3. Copy django folder into C:\Python27\Lib\site-packages\
4. Right click on “My Computer” and select Properties.
5. Go to Advanced, then Environment Variables at the bottom.
6. Edit “Path” and at the end add the following:

```
;C:\Python27;C\Python27\scripts;C:\Python27\Lib\site-packages\django\bin
```


#####Test to find out if it was a great success!
In cmd (you can find this program from the start menu), type

```
python
```

and press enter. The python shell should appear. Enter

```
import django
```

and then

```
django.get_version()
```

This should return

```
1.6
```

YAY

Note: exit() will get you out of the shell
