# stacks 书库
本来想做个每个人存书籍的地方，后来越做越感觉像存储库了

### 项目内容
stacks这个网站，从外到里讲吧
花生壳进行的外网访问，树莓派布置的网站，nginx+uwsgi做的服务器，flask架构，mysql做的数据库

#### 花生壳
花生壳用的免费的，每个月一个G流量，带宽是1M，所以上传不是太快
这个选择我当时用了cpolar，但是后端就是很玄的东西，你觉得是正确的东西，结果不对，当时可能因为装了一些东西，也可能对cpolar做了一些设置，所以内部的cpolar总是连不上外网
为这个事还和cpolar的客服聊了很久，人家也给了很多方法，还是不行
这就使用了花生壳，因为花生壳可以用，就没去整cpolar了

#### 树莓派
很烦，我找个合适的系统就找了很久  
因为一开始使用过centos7虚拟机，还行，就先尝试了centos7，结果国内源对centos7+aarch64不太友好，很多库都下不成，就放弃了  
后来知道archlinux是"邪教"，我想看看我有没有入魔的潜质，就装了，结果装个系统就要从自己分区开始，这里自己找资料完成都很开心，装好后不能远程登录，就走了  
接着是使用树莓派官方系统，这个感觉底层是ubuntu，以为使用的是apt下载，这个好像也是有些库下载不了，就算了  
现在使用的是ubuntu系统，这个用的还行，什么库都有，因为工作原因还使用了机器学习tensorflow方面的库，也还行  
如果使用了上述系统的，可以去看看学习笔记的repo-issues，上面有笔记  
![image](https://github.com/keyfall/stacks/assets/21198605/9b4ccc3b-d033-44e7-8fb3-32e4bcf8e2c9)  


#### nginx+uwsgi
当时用这个是因为有次面试时，有人问我你项目用的什么服务器，我竟然说了flask，然后人家说那是框架..  
后来项目就使用了这个挺火的nginx+uwsgi吧，因为一搜就很多  
nginx做了转发，uwsgi启服务  
这里有个bug，就是flask里有的函数使用redirect做转发，但是到nginx会找不到，这个bug我没解决，所以就没有转发了，全都是直接跳转的html  
如果直接使用flask或者uwsgi启服务，不要nginx，就可以转发  


#### flask
flask-login：用户权限  
flask_sqlalchemy:数据库交互  
后台除了flask以外的大概这些，我觉得还是做个视频讲讲每个功能或者页面怎么用比较好，这几天整一个  

### 项目总结
做这个主要是因为想当做一个书籍聚集点，让每个人不用为搜书发愁，每次找书，要么是很少资源，要么是要加公众号的，好烦
这里每个人都可以分享书，如果没有，希望从别的地方得到书后上传上来，让其他人不在去费心费力的寻找  

B站账号:keyfall
git账号:https://github.com/keyfall/

  