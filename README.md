
  ## 1. 当我们在README.md写好内容时，发现它缩到一起了，怎么办呢？
     直接在要换行的语句最后打上2个空格。

  ## 2. GitHub上README.md排版样式教程
  https://blog.csdn.net/u012067966/article/details/50736647 
```  
#一级标题  
##二级标题  
###三级标题  
####四级标题  
#####五级标题  
######六级标题  
    注意井号#和标题名称要并排写作一行。 
    实际上，前文所述的大标题和中标题是分别和一级标题和二级标题对应的。即大标题大小和一级标题相同，中标题大小和二级标题相同。  
    普通文本：直接输入的文字就是普通文本。需要注意的是要换行的时候不能直接通过回车来换行，需要使用<br>(或者<br/>)。也就是html里面的标签。事实上，markdown支持一些html标签，你可以试试。当然如果你完全使用html来写的话，就丧失意义了，毕竟markdown并非专门做前端的，然而仅实现一般效果的话，它会比html写起来要简洁得多得多啦。  
```

**这个是粗体**<br>
*这个是斜体* <br>
***这个是粗体加斜体***<br>

  ## 3. GIT 第二问 Pycharm上传projects 到github 并创建 repository：  
   https://blog.csdn.net/olfisher/article/details/53790432  
     
  ## 4. 如何在Github中删除已有仓库或文件：
   https://blog.csdn.net/weixin_42152081/article/details/80635777  

  ## 5. github 添加密钥实现无密码操作
   https://blog.csdn.net/wanglei_storage/article/details/53258804

   ### （1）生成ssh密钥对
       当然上传之前肯定要自己先生成ssh key了。  
       windows的用户可以下载xshell之类的工具来生成；  
       linux就直接输命令:ssh-keygen -t rsa    #一直回车下去，不输入密码!  
   ### （2）查看公钥  
       密钥对生成完成后存放于当前用户 ~/.ssh 目录中，查看 id_rsa.pub  
          
  ## 6. 如何在README.md文件中添加图片？
   第一步：首先，向github 上传所需的图片；    
   第二部：打开README文件，写入图片的格式为：    
   ![Image text](图片的URL) --必须给出图片路径才可以显示（支持图片格式png和jpg） 
   ![Image text]这个标识不可缺少，不然就显示文字了。Image text：指的是如果图片不存在了，要显示的文字说明。

   ![image](https://github.com/liuliu408/image/blob/master/image1.png)
 
 

|列1的内容1|列2的内容1|
|列1的内容2|列2的内容2|

