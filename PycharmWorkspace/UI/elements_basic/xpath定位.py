"""
======================
Author: 柠檬班-小简
Time: 2020/8/14 20:14
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
//*[@id="course-header"]/div/h1
//*[@id="third-nav"]/a[3]
//a[text()="话题"]
//*[@id="number-attend"]/div[2]/div[3]/i[1]


绝对定位：/开头    父节点/子节点
   绝对路径：从根目录开始，一直到当前的目录。
   绝对定位：从根结点开始，一直到当前的结点。结点顺序/结点位置
   
相对定位：//开头//
    相对路径：相对参照物。// 相对于前面节点。如果//在开头，那就是相对整个html
    定位原则：
        1、不依靠节点顺序和节点位置
        2、只要能够找得到匹配特征的元素就可以。
     
定位辅助工具：
 F12 -> elments -> Ctrl+F   
相对定位表达式：
    1、//标签名[@属性名=值]
    2、//标签名[text()=值]
    3、//标签名[contains(@属性名,值)]   //标签名[contains(text(),值)]
    4、*  标签名或者属性名都可以用*,表示匹配所有  //*[contains(@*,"TopicDiscuss")]
    
    当单一属性，无法唯一定位到元素
    组合条件
    逻辑：and or
    //标签名[text()=值 and @属性名=值 and contains(@属性名,值)]
    //标签名[text()=值 or @属性名=值 or contains(@属性名,值)]
    
    仅靠元素本身的特征，已经无法唯一定位。 
    层级：
    //祖先节点//要找的节点
    //div[@id="u1"]//a[@name="tj_login"]
    
    轴定位:
    元素的兄弟姐妹、父母
    轴运算：
    ancestor：祖先结点 包括父
    parent:父结点   
    preceding-sibling: 当前元素节点标签之前的所有兄弟结点
    following-sibling：当前元素节点标签之后的所有兄弟结点
    
    
    preceding: 当前元素节点标签之前的所有结点。（html页面先后顺序）
    following: 当前元素节点标签之后的所有结点。（html页面先后顺序）
    

    使用语法：
    已知的元素/轴名称::标签名称[@属性=值]
    例：//span[text()="考勤"]/parent::a
       //span[text()="考勤"]/ancestor::a
       //li[text()="发布作业"]/preceding-sibling::*
       //p[@title="030011"]/following-sibling::p[@class="name"]
       
       //span[text()="考勤"]/ancestor::a/following-sibling::p//div
    
    //dd[@data-val="张芝波"]/following-sibling::dd[contains(@class,"batscore")]/span
    较多的应用场景：
    页面显示为一个表格样式的数据列。需要通过组合来定位元素
    


    
    
    
 
 
//a[text()="话题"]   
//a[contains(@href,"TopicDiscuss")]

"""
