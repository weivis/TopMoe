#该文件储存的是用于扩展的代码 可复制到工程内使用


#内容主分类表
class Main_category(db.Model):

    '''表名设置'''
    __tablename__ = 'main_category'

    id = db.Column(db.Integer, primary_key=True) #分类id
    name = db.Column(db.Text)       #分区名
    sort = db.Column(db.Integer)    #类目排序

    '''可在此处添加需要的字段'''
    
    def __init__(self, name=None, sort=None):
        self.name = name
        self.sort = sort
        self.update()  # 提交数据

    def update(self):
        db.session.add(self)
        db.session.commit()


#内容子分类表
class Sub_category(db.Model):

    '''表名设置'''
    __tablename__ = 'sub_category'

    id = db.Column(db.Integer, primary_key=True) #分类id
    name = db.Column(db.Text)       #分区名
    sort = db.Column(db.Integer)    #类目排序
    parentID = db.Column(db.Integer) #父级id

    '''可在此处添加需要的字段'''
    
    def __init__(self, name=None, sort=None, parentID=None):
        self.name = name
        self.sort = sort
        self.parentID = parentID
        self.update()  # 提交数据

    def update(self):
        db.session.add(self)
        db.session.commit()


#文章表
class Article(db.Model):

    '''表名设置'''
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True) #文章id
    sub_category = db.Column(db.Integer) #分类
    authorid = db.Column(db.Integer) #作者id
    title = db.Column(db.Text) #标题
    content = db.Column(db.Text) #内容
    status = db.Column(db.Integer) #状态
    upload_date = db.Column(db.String(100)) #发布时间

    '''可在此处添加需要的字段'''

    def __init__(self, sub_category = None, authorid = None, title = None, content = None, status = None, upload_date = None):
        self.sub_category = sub_category
        self.authorid = current_user.id #作者id
        self.title = title
        self.content = content
        self.status = status
        self.upload_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update()

    def update(self):
        db.session.add(self)
        db.session.commit()