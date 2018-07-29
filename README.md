
  ## 1. 当我们在README.md写好内容时，发现它缩到一起了，不是我们想要的格式，怎么办呢？  
     直接在要换行的语句最后打上2个空格。

  # 2. GIT 第二问 Pycharm上传projects 到github 并创建 repository：  
     https://blog.csdn.net/olfisher/article/details/53790432  
     
  # 3. 如何在Github中删除已有仓库或文件：
     https://blog.csdn.net/weixin_42152081/article/details/80635777  

  # 4. github 添加密钥实现无密码操作
   https://blog.csdn.net/wanglei_storage/article/details/53258804

   ## （1）生成ssh密钥对
       当然上传之前肯定要自己先生成ssh key了。  
       windows的用户可以下载xshell之类的工具来生成；  
       linux就直接输命令:ssh-keygen -t rsa    #一直回车下去，不输入密码!  
   ## （2）查看公钥  
       密钥对生成完成后存放于当前用户 ~/.ssh 目录中，查看 id_rsa.pub  
          
  # 5. 如何在README.md文件中添加图片？
   第一步：首先，向github 上传所需的图片；    
   第二部：打开README文件，写入图片的格式为：    
  #  ![Image text](图片的URL) --必须给出图片路径才可以显示（支持图片格式png和jpg） 
  注：![Image text]这个标识不可缺少，不然就显示文字了。Image text：指的是如果图片不存在了，要显示的文字说明。

   ![image](https://github.com/liuliu408/image/blob/master/image1.png)
 
 



