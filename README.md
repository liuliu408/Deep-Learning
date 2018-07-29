
 # Github上README.md编辑格式使用  
 （Markdown是一种可以使用普通文本编辑器编写的标记语言    
  https://blog.csdn.net/qcx321/article/details/53780672  
 -----------------------------------------------[liuqiang](https://sites.google.com/view/qiangliu/)------------------------
 
  ## 1. 当我们在README.md写好内容时，发现它缩到一起了，怎么办呢？
     直接在要换行的语句最后打上2个空格。

  ## 2. GitHub上README.md排版样式教程
  https://blog.csdn.net/u012067966/article/details/50736647 
  https://www.cnblogs.com/leechanx/archive/2013/03/25/3322616.html  
  https://www.cnblogs.com/shiy/p/6526868.html
```  
 #一级标题  
 ##二级标题  
 ###三级标题  
 ####四级标题  
 #####五级标题  
 ######六级标题  
 注意井号#和标题名称要并排写作一行。 
 实际上，前文所述的大标题和中标题是分别和一级标题和二级标题对应的。即大标题大小和一级标题相同，中标题大小和二级标题相同。 
 
 普通文本：直接输入的文字就是普通文本。需要注意的是要换行的时候不能直接通过回车来换行，需要使用<br>(或者<br/>)。也就是html里面的标签。
 事实上，markdown支持一些html标签，你可以试试。
 当然如果你完全使用html来写的话，就丧失意义了，毕竟markdown并非专门做前端的，然而仅实现一般效果的话，它会比html写起来要简洁得多得多啦。  

**这个是粗体**<br>
*这个是斜体* <br>
***这个是粗体加斜体***<br> 

换行：使用标签<br>
单行文本：前面使用两个Tab
多行文本:每行行首加两个Tab
部分文字高亮：使用``包围，这个符号不是单引号，而是Tab上方，数字1左边那个按键的符号
、在键盘的ESC键下。 
```
<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=#0099ff size=12 face="黑体">黑体</font>
<font color=#00ffff size=3>null</font>
<font color=gray size=5>gray</font>
     
  ## 3. 如何在README.md文件中添加图片？
   第一步：首先，向github 上传所需的图片；    
   第二部：打开README文件，写入图片的格式为：   
   ```
   ![Image text](图片的URL) 
   ![Image text]这个标识不可缺少，不然就显示文字了。Image text：指的是如果图片不存在了，要显示的文字说明。
    图片的URL：给出图片路径（支持图片格式png和jpg）
    如：![image](https://github.com/liuliu408/image/blob/master/image1.png) 
   ```
   ![image](https://github.com/liuliu408/image/blob/master/image2.png)
   ![image](https://github.com/liuliu408/image/blob/master/image3.png)
   
   ##  4. 显示图片方法2
   ```
   <img src="https://upload-images.jianshu.io/upload_images/64542-b2610724831ceb28.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700" ；export=download width="720" /> 
  
  上面的网址是指定网页的上的图片地址复制过来：https://upload-images.jianshu.io/upload_images/64542-b2610724831ceb28.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700
   ```
   <img src="https://upload-images.jianshu.io/upload_images/64542-b2610724831ceb28.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700" /> 
