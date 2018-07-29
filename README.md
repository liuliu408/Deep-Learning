
github如何建仓库

Github如何删除repository(仓库)

github如何写文章

github如何上传文章



GIT 第二问 Pycharm上传projects 到github 并创建 repository： https://blog.csdn.net/olfisher/article/details/53790432

如何在Github中删除已有仓库或文件：https://blog.csdn.net/weixin_42152081/article/details/80635777


github 添加密钥实现无密码操作
   https://blog.csdn.net/wanglei_storage/article/details/53258804

一、生成ssh密钥对
    当然上传之前肯定要自己先生成ssh key了。
    windows的用户可以下载xshell之类的工具来生成；
    linux就直接输命令:ssh-keygen -t rsa    #一直回车下去，不输入密码!
二、查看公钥
    密钥对生成完成后存放于当前用户 ~/.ssh 目录中，查看 id_rsa.pub
    
 ![image](https://github.com/liuliu408/image/blob/master/image1.png)

1，向README文件中添加图片，用于展示程序效果或辅助说明！

  两步： 首先，向github 上传所需的图片；
 
 然后，打开README文件，写入图片的格式为：

    ![image](https://github.com/secondLieutenantCoder/TableAndCollection/blob/master/resut.png?raw=true)

    ![image](图片的URL)
