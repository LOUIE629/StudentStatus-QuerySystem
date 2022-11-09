#author 罗宇辰
#version v1.0
import tkinter as tk
import tkinter.messagebox
import PIL.ImageTk as ImageTk
import PIL.Image as Image
import pickle
import pymysql

window=tk.Tk()
window.title('学生信息查询系统')
window.geometry('450x300')

#welcome image
im_welcome=Image.open('welcome.jpg')
image_welcome=ImageTk.PhotoImage(im_welcome)
im_student = Image.open('student.jpg')
image_student = ImageTk.PhotoImage(im_student)
im_bridge = Image.open('bridge.jpg')
image_bridge = ImageTk.PhotoImage(im_bridge)
tk.Label(window,image=image_student).pack(side='right')


def usr_student():
    #window.destroy()
    window_student=tk.Toplevel(window)
    window_student.geometry('450x300')
    window_student.title('学生登录窗口')

    #bakeground image
    tk.Label(window_student, justify=tk.LEFT, image=image_welcome, compound=tk.CENTER).pack()

    tk.Label(window_student, text='学号:').place(x=110, y=150)
    tk.Label(window_student, text='密码:').place(x=110, y=190)

    var_usr_name = tk.StringVar()
    var_usr_pwd = tk.StringVar()

    entry_usr_name = tk.Entry(window_student, textvariable=var_usr_name)
    entry_usr_name.place(x=160, y=150)

    entry_usr_pwd = tk.Entry(window_student, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=160, y=190)

    def usr_login():
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)

        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tk.messagebox.showinfo(message='欢迎同学登录系统')
                #window_student.destroy()
                #window_3 = tk.Tk()
                window_3 = tk.Toplevel(window_student)
                window_3.geometry('400x300')
                window_3.title('功能')
                tk.Label(window_3, justify=tk.LEFT, image=image_bridge, compound=tk.CENTER).pack()
                def student_id():
                    #window_3.destroy()
                    #window_id = tk.Tk()
                    window_id = tk.Toplevel(window_3)
                    window_id.geometry('800x500')
                    window_id.title('个人信息')
                    tk.Label(window_id, justify=tk.LEFT, image=image_bridge, compound=tk.CENTER).pack()
                    db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                    cursor = db.cursor()

                    sql_sanme = '''select SNAME from s where SNO=%s '''
                    cursor.execute(sql_sanme, (usr_name))
                    result_sname = cursor.fetchall()

                    sql_ssex = '''select SSEX from s where SNO=%s '''
                    cursor.execute(sql_ssex, (usr_name))
                    result_ssex = cursor.fetchall()

                    sql_sbirth = '''select SBIRTH from s where SNO=%s '''
                    cursor.execute(sql_sbirth, (usr_name))
                    result_sbirth = cursor.fetchall()

                    sql_sdept = '''select SDEPT from s where SNO=%s '''
                    cursor.execute(sql_sdept, (usr_name))
                    result_sdept = cursor.fetchall()

                    cursor.close()
                    db.close()

                    tk.Label(window_id, text='个人信息', font=('Arial', 25), fg='blue').place(x=300, y=30)
                    tk.Label(window_id, text='学号', font=('Arial', 12), width=10, height=2, relief="sunken").place(x=100,
                                                                                                                  y=100)
                    tk.Label(window_id, text='姓名', font=('Arial', 12), width=10, height=2, relief="sunken").place(x=100,
                                                                                                                  y=150)
                    tk.Label(window_id, text='性别', font=('Arial', 12), width=10, height=2, relief="sunken").place(x=100,
                                                                                                                  y=200)
                    tk.Label(window_id, text='出生年月', font=('Arial', 12), width=10, height=2, relief="sunken").place(
                        x=100, y=250)
                    tk.Label(window_id, text='学院', font=('Arial', 12), width=10, height=2, relief="sunken").place(x=100,
                                                                                                                  y=300)

                    tk.Label(window_id, text=usr_name, font=('Arial', 12), width=40, height=2, relief="sunken").place(
                        x=200, y=100)
                    tk.Label(window_id, text=result_sname[0][0], font=('Arial', 12), width=40, height=2,
                             relief="sunken").place(x=200, y=150)
                    tk.Label(window_id, text=result_ssex[0][0], font=('Arial', 12), width=40, height=2,
                             relief="sunken").place(x=200, y=200)
                    tk.Label(window_id, text=result_sbirth[0][0], font=('Arial', 12), width=40, height=2,
                             relief="sunken").place(x=200, y=250)
                    tk.Label(window_id, text=result_sdept[0][0], font=('Arial', 12), width=40, height=2,
                             relief="sunken").place(x=200, y=300)

                def student_select():
                    #window_3.destroy()
                    #window_select = tk.Tk()
                    window_select = tk.Toplevel(window_3)
                    window_select.geometry('800x500')
                    window_select.title('成绩查询')
                    cno_in = tk.StringVar()
                    tk.Label(window_select, text='成绩查询', font=('Arial', 25), fg='blue').place(x=300, y=30)
                    tk.Label(window_select, text='课程号', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=150)
                    entry_usr_cno=tk.Entry(window_select, textvariable=cno_in)
                    entry_usr_cno.place(x=200, y=150)
                    tk.Label(window_select, text='课程名称', font=('Arial', 12), width=10, height=2,
                             relief="sunken").place(x=100, y=250)
                    tk.Label(window_select, text='成绩', font=('Arial', 12), width=10, height=2,
                             relief="sunken").place(x=100, y=300)

                    def select():
                        try:
                            usr_cno = cno_in.get()
                            db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                            cursor = db.cursor()

                            sql_grade = '''select grade from sc where sno=%s and cno=%s'''
                            cursor.execute(sql_grade, (usr_name, usr_cno))
                            result_grade = cursor.fetchall()

                            sql_cname = '''select cname from c where cno=%s  '''
                            cursor.execute(sql_cname, (usr_cno))
                            result_cname = cursor.fetchall()
                            cursor.close()
                            db.close()

                            tk.Entry(window_select, textvariable=cno_in, width=50).place(x=200, y=150)
                            tk.Label(window_select, text=result_cname[0][0], font=('Arial', 12), width=40, height=2,
                                     relief="sunken").place(x=200, y=250)
                            tk.Label(window_select, text=result_grade[0][0], font=('Arial', 12), width=40, height=2,
                                     relief="sunken").place(x=200, y=300)
                        except:
                            tk.messagebox.showerror(title='Error',message='没有该科成绩')

                    '''
                    def fanhui():
                        window_select.destroy()
                        window_3 = tk.Tk()
                        window_3.geometry('400x300')
                        window_3.title('功能')
                        tk.Button(window_3, text='个人信息', command=student_id, font=('Arial', 15)).place(x=50, y=100)
                        tk.Button(window_3, text='成绩查询', command=student_select, font=('Arial', 15)).place(x=200, y=100)
                    '''

                    tk.Button(window_select, text='查询', command=select, font=('Arial', 12)).place(x=600, y=150)
                    #tk.Button(window_select, text='返回上级界面', command=fanhui, font=('Arial', 12)).place(x=300, y=300)

                tk.Button(window_3, text='个人信息', command=student_id, font=('Arial', 15)).place(x=50, y=100)
                tk.Button(window_3, text='成绩查询', command=student_select, font=('Arial', 15)).place(x=200, y=100)


            else:
                tk.messagebox.showerror(title='Error',message='密码错误，请重试')
        else:
            tk.messagebox.showerror(title='Error',message='不存在该账号')

    tk.Button(window_student, text='登录', command=usr_login).place(x=200, y=250)

def usr_teacher():
    #window.destroy()
    #window_teacher = tk.Tk()
    window_teacher=tk.Toplevel(window)
    window_teacher.geometry('450x300')
    window_teacher.title('教师登录窗口')
    tk.Label(window_teacher, justify=tk.LEFT, image=image_welcome, compound=tk.CENTER).pack()
    tk.Label(window_teacher, text='教职工号:').place(x=90, y=150)
    tk.Label(window_teacher, text='密码:').place(x=110, y=190)

    var_usr_name = tk.StringVar()
    var_usr_pwd = tk.StringVar()

    entry_usr_name = tk.Entry(window_teacher, textvariable=var_usr_name)
    entry_usr_name.place(x=160, y=150)

    entry_usr_pwd = tk.Entry(window_teacher, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=160, y=190)

    def usr_login():
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        with open('teacher_info.pickle', 'rb') as usr_file:
            teacher_info = pickle.load(usr_file)

        if usr_name in teacher_info:
            if usr_pwd == teacher_info[usr_name]:
                tk.messagebox.showinfo(message='欢迎老师登录系统')
                #window_teacher.destroy()
                #window_3 = tk.Tk()
                window_3=tk.Toplevel(window_teacher)
                window_3.geometry('400x300')
                window_3.title('功能')

                def teacher_idselect():
                    #window_3.destroy()
                    #window_id = tk.Tk()
                    window_id=tk.Toplevel(window_3)
                    window_id.geometry('800x500')
                    window_id.title('学生信息查询')
                    var_student_sno=tk.StringVar()
                    tk.Label(window_id, text='学生信息', font=('Arial', 25), fg='blue').place(x=300, y=30)
                    tk.Label(window_id, text='学号', font=('Arial', 12), width=10, height=2, relief="sunken").place(x=100,
                                                                                                                  y=100)
                    tk.Label(window_id, text='姓名', font=('Arial', 12), width=10, height=2, relief="sunken").place(x=100,
                                                                                                                  y=150)
                    tk.Label(window_id, text='性别', font=('Arial', 12), width=10, height=2, relief="sunken").place(x=100,
                                                                                                                  y=200)
                    tk.Label(window_id, text='出生年月', font=('Arial', 12), width=10, height=2, relief="sunken").place(
                        x=100, y=250)
                    tk.Label(window_id, text='学院', font=('Arial', 12), width=10, height=2, relief="sunken").place(x=100,
                                                                                                                  y=300)

                    tk.Entry(window_id, textvariable=var_student_sno, width=50).place(x=200, y=100)

                    def select():
                        student_sno = var_student_sno.get()
                        db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                        cursor = db.cursor()
                        sql_sanme = '''select SNAME from s where SNO=%s '''
                        cursor.execute(sql_sanme, (student_sno))
                        result_sname = cursor.fetchall()

                        sql_ssex = '''select SSEX from s where SNO=%s '''
                        cursor.execute(sql_ssex, (student_sno))
                        result_ssex = cursor.fetchall()

                        sql_sbirth = '''select SBIRTH from s where SNO=%s '''
                        cursor.execute(sql_sbirth, (student_sno))
                        result_sbirth = cursor.fetchall()

                        sql_sdept = '''select SDEPT from s where SNO=%s '''
                        cursor.execute(sql_sdept, (student_sno))
                        result_sdept = cursor.fetchall()

                        tk.Label(window_id, text=result_sname[0][0], font=('Arial', 12), width=40, height=2,
                                 relief="sunken").place(x=200, y=150)
                        tk.Label(window_id, text=result_ssex[0][0], font=('Arial', 12), width=40, height=2,
                                 relief="sunken").place(x=200, y=200)
                        tk.Label(window_id, text=result_sbirth[0][0], font=('Arial', 12), width=40, height=2,
                                 relief="sunken").place(x=200, y=250)
                        tk.Label(window_id, text=result_sdept[0][0], font=('Arial', 12), width=40, height=2,
                                 relief="sunken").place(x=200, y=300)

                        cursor.close()
                        db.close()
                    tk.Button(window_id, text='查询', command=select, font=('Arial', 12)).place(x=600, y=100)
                def teacher_gradeselect():
                    #window_3.destroy()
                    #window_select = tk.Tk()
                    window_select=tk.Toplevel(window_3)
                    window_select.geometry('800x500')
                    window_select.title('学生成绩查询')
                    var_student_sno = tk.StringVar()
                    var_student_cno = tk.StringVar()
                    tk.Label(window_select, text='学生成绩查询', font=('Arial', 25), fg='blue').place(x=300, y=30)
                    tk.Label(window_select, text='学号', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=150)
                    tk.Label(window_select, text='课程号', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=200)
                    tk.Entry(window_select, textvariable=var_student_sno, width=50).place(x=200, y=150)
                    tk.Entry(window_select, textvariable=var_student_cno, width=50).place(x=200, y=200)
                    tk.Label(window_select, text='课程名称', font=('Arial', 12), width=10, height=2,
                             relief="sunken").place(x=100, y=250)
                    tk.Label(window_select, text='成绩', font=('Arial', 12), width=10, height=2,
                             relief="sunken").place(x=100, y=300)
                    def select():
                        try:
                            student_sno = var_student_sno.get()
                            student_cno = var_student_cno.get()
                            db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                            cursor = db.cursor()

                            sql_grade = '''select grade from sc where sno=%s and cno=%s'''
                            cursor.execute(sql_grade, (student_sno, student_cno))
                            result_grade = cursor.fetchall()

                            sql_cname = '''select cname from c where cno=%s  '''
                            cursor.execute(sql_cname, (student_cno))
                            result_cname = cursor.fetchall()
                            cursor.close()
                            db.close()

                            tk.Label(window_select, text=result_cname[0][0], font=('Arial', 12), width=40, height=2,
                                     relief="sunken").place(x=200, y=250)
                            tk.Label(window_select, text=result_grade[0][0], font=('Arial', 12), width=40, height=2,
                                     relief="sunken").place(x=200, y=300)
                        except:
                            tk.Label(window_select, font=('Arial', 12), width=40, height=2,
                                     relief="sunken").place(x=200, y=300)
                            tk.messagebox.showerror(title='ERROR',message='没有该门成绩')
                    tk.Button(window_select, text='查询', command=select, font=('Arial', 12)).place(x=600, y=200)

                def teacher_gradeupdate():
                    #window_3.destroy()
                    #window_select = tk.Tk()
                    window_select = tk.Toplevel(window_3)
                    window_select.geometry('800x500')
                    window_select.title('学生成绩修改')
                    var_student_sno = tk.StringVar()
                    var_student_cno = tk.StringVar()
                    var_student_grade = tk.StringVar()
                    tk.Label(window_select, text='学生成绩修改', font=('Arial', 25), fg='blue').place(x=300, y=30)
                    tk.Label(window_select, text='学号', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=100)
                    tk.Label(window_select, text='课程号', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=200)
                    tk.Label(window_select, text='成绩', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=300)
                    tk.Entry(window_select, textvariable=var_student_sno, width=50).place(x=200, y=100)
                    tk.Entry(window_select, textvariable=var_student_cno, width=50).place(x=200, y=200)
                    tk.Entry(window_select, textvariable=var_student_grade, width=50).place(x=200, y=300)
                    def update():
                        try:
                            student_sno = var_student_sno.get()
                            student_cno = var_student_cno.get()
                            student_grade = var_student_grade.get()
                            db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                            cursor = db.cursor()

                            sql_update = '''update sc set grade=%s where sno=%s and cno=%s'''
                            cursor.execute(sql_update, (student_grade, student_sno, student_cno))

                            db.commit()
                            cursor.close()
                            db.close()
                            if student_grade==0 or student_cno==0 or student_sno==0:
                                tk.messagebox.showerror(message='修改成绩失败')
                            else:
                                tk.messagebox.showinfo(message='修改成绩成功')
                        except:
                            tk.messagebox.showerror(title='ERROR',message='修改成绩失败')

                    def insert():
                        try:
                            student_sno = var_student_sno.get()
                            student_cno = var_student_cno.get()
                            student_grade = var_student_grade.get()
                            db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                            cursor = db.cursor()

                            sql_insert = '''insert into sc values(%s,%s,%s)'''
                            cursor.execute(sql_insert, (student_sno, student_cno, student_grade))

                            db.commit()
                            cursor.close()
                            db.close()
                            tk.messagebox.showinfo(message='插入成功')

                        except:
                            tk.messagebox.showerror(title='ERROR',message='插入失败')

                    def delete():
                        student_sno = var_student_sno.get()
                        student_cno = var_student_cno.get()
                        student_grade = var_student_grade.get()
                        db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                        cursor = db.cursor()

                        sql_delete = '''delete from sc where sno=%s and cno=%s '''
                        cursor.execute(sql_delete, (student_sno, student_cno))

                        db.commit()
                        cursor.close()
                        db.close()
                        tk.messagebox.showinfo(message='删除成功')



                    tk.Button(window_select, text='更新', command=update, font=('Arial', 12)).place(x=200, y=400)
                    tk.Button(window_select, text='插入', command=insert, font=('Arial', 12)).place(x=350, y=400)
                    tk.Button(window_select, text='删除', command=delete, font=('Arial', 12)).place(x=500, y=400)

                def teacher_idupdate():
                    #window_3.destroy()
                    #window_select = tk.Tk()
                    window_select = tk.Toplevel(window_3)
                    window_select.geometry('800x700')
                    window_select.title('学籍信息修改')
                    var_student_sno = tk.StringVar()
                    var_student_name = tk.StringVar()
                    var_student_gender = tk.StringVar()
                    var_student_birth = tk.StringVar()
                    var_student_college = tk.StringVar()
                    tk.Label(window_select, text='学籍信息修改', font=('Arial', 25), fg='blue').place(x=300, y=30)
                    tk.Label(window_select, text='学号', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=100)
                    tk.Label(window_select, text='姓名', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=200)
                    tk.Label(window_select, text='性别', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=300)
                    tk.Label(window_select, text='出生年月', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=400)
                    tk.Label(window_select, text='所在院系', font=('Arial', 12), width=10,
                             relief="sunken").place(x=100, y=500)
                    tk.Entry(window_select, textvariable=var_student_sno, width=50).place(x=200, y=100)
                    tk.Entry(window_select, textvariable=var_student_name, width=50).place(x=200, y=200)
                    tk.Entry(window_select, textvariable=var_student_gender, width=50).place(x=200, y=300)
                    tk.Entry(window_select, textvariable=var_student_birth, width=50).place(x=200, y=400)
                    tk.Entry(window_select, textvariable=var_student_college, width=50).place(x=200, y=500)

                    def update():
                        tk.Label(window_select, width=50,
                                 relief="sunken").place(x=200, y=200)
                        tk.Label(window_select, width=50,
                                 relief="sunken").place(x=200, y=300)
                        tk.Label(window_select, width=50,
                                 relief="sunken").place(x=200, y=400)

                        student_sno = var_student_sno.get()
                        student_college = var_student_college.get()

                        db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                        cursor = db.cursor()

                        sql_update = '''update s set sdept=%s where sno=%s '''
                        cursor.execute(sql_update, (student_college, student_sno))

                        db.commit()
                        cursor.close()
                        db.close()
                        tk.messagebox.showinfo(title='提示', message='修改成功')

                    def insert():
                        try:
                            student_sno = var_student_sno.get()
                            student_name = var_student_name.get()
                            student_gender = var_student_gender.get()
                            student_birth = var_student_birth.get()
                            student_college = var_student_college.get()
                            db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                            cursor = db.cursor()

                            sql_insert = '''insert into s values(%s,%s,%s,%s,%s)'''
                            cursor.execute(sql_insert,
                                           (student_sno, student_name, student_gender, student_birth, student_college))

                            db.commit()
                            cursor.close()
                            db.close()

                            tk.messagebox.showinfo(message='插入成功')
                        except:
                            tk.messagebox.showerror(message='插入失败')

                    def delete():
                        student_sno = var_student_sno.get()

                        db = pymysql.connect("localhost", "root", "louie0629021x", "student")
                        cursor = db.cursor()

                        sql_delete = '''delete from s where sno=%s  '''
                        cursor.execute(sql_delete, (student_sno))

                        db.commit()
                        cursor.close()
                        db.close()
                        tk.messagebox.showinfo(title='提示',message='删除成功')


                    tk.Button(window_select, text='更新', command=update, font=('Arial', 12)).place(x=200, y=600)
                    tk.Button(window_select, text='插入', command=insert, font=('Arial', 12)).place(x=350, y=600)
                    tk.Button(window_select, text='删除', command=delete, font=('Arial', 12)).place(x=500, y=600)

                tk.Button(window_3, text='学籍信息查询', command=teacher_idselect, font=('Arial', 15)).place(x=130, y=50)
                tk.Button(window_3, text='学生成绩查询', command=teacher_gradeselect, font=('Arial', 15)).place(x=130, y=100)
                tk.Button(window_3, text='学籍信息修改', command=teacher_idupdate, font=('Arial', 15)).place(x=130, y=150)
                tk.Button(window_3, text='学生成绩修改', command=teacher_gradeupdate, font=('Arial', 15)).place(x=130, y=200)

            else:
                tk.messagebox.showerror(title='Error',message='密码错误，请重试')
        else:
            tk.messagebox.showerror(title='Error',message='不存在该账号')

    btn_login = tk.Button(window_teacher, text='登录', command=usr_login)
    btn_login.place(x=200, y=250)

btn_student=tk.Button(window,text='学生入口',command=usr_student)
btn_student.place(x=100,y=200)
btn_teacher=tk.Button(window,text='教师入口',command=usr_teacher)
btn_teacher.place(x=280,y=200)
window.mainloop()
