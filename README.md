2020数据库实验大作业 Pymysql + tkinter（图形化界面） + pickle（本地存储账号密码）

# 操作说明
## 1.可打开"添加用户.py"创建学生的账号密码和老师的账号密码。也可直接使用测试的数据。
（测试学生1账号：2018300356 密码：2018300356
      学生2账号：2018300357 密码：2018300357
      教师登录账号：teacher 密码：teacher）
## 2.打开”本地连接.py“或“GaussDB连接.py”运行。

# 数据库设计
## 需求分析
### 1.通过账号，密码登录系统。
### 2.区分学生与教师的权限。
### 3.学生只可以查看自己的学籍信息，查询自己的成绩。
### 4.教师可以查看全部学籍，成绩信息；输入新的学籍信息，成绩；修改已有学籍信息中‘所在学院‘列和成绩；删除已有学籍，成绩信息。

## 数据流图

![image](https://user-images.githubusercontent.com/74084385/200895489-d21052da-31df-4499-a911-d704bce4f641.png)

## 数据字典
### 1.数据处理条目

![image](https://user-images.githubusercontent.com/74084385/200894216-953f72cf-32c0-4c03-9f9b-233e3d15e162.png)

### 2.数据存储条目

![image](https://user-images.githubusercontent.com/74084385/200894431-0927bf3b-082f-43b6-8c05-ec19ad754e6e.png)

## E-R图

![image](https://user-images.githubusercontent.com/74084385/200895268-30d467f7-e67f-4d74-8223-b5dea5cb56b2.png)

## 关系模式设计
学籍信息s(学号sno,姓名sname,性别gender,出生年月birth,学院college)(主键：sno)
课程信息c(课程号cno,课程名cname,学分credit)(主键：cno)
成绩信息sc(学号sno,课程号cno,成绩grade)(外键：sno,cno)
