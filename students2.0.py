"""学生管理系统2.0版本，将学生信息存在文件里。
学生文件存在student.json里面.
该版本还没想好怎么修改、删除Json文件里的数据.
"""
import os
import json

#用来保存学生信息的文件
filename = "students.json"

#判断文件是否存在,如果不存在，创建文件.
#如果没有此文件,搜索学生时会报错.
if not os.path.exists(filename) :
    file = open(filename, 'w')
    file.close()

#开始程序后，主程序的欢迎界面。
def greet_welcome():
    print("\n欢迎进入学生管理系统。")
    print("输入'1',添加学生信息。")
    print("输入'2',修改学生信息。")
    print("输入'3',删除学生信息。")
    print("输入'4',查询学生信息。")
    print("输入'5',查询所有学生信息。")
    print("输入'6',退出此程序。")

#打印学生信息
def print_student_head():
    students_id = "Id"
    students_name = "Name"
    students_sex = "Sex"
    students_age = "Age"
    students_subject = "Subject"
    print(students_id.ljust(5), students_name.center(35),
          students_sex.ljust(10), students_age.ljust(5),
          students_subject.center(35))

def print_student_info(students):
    students_id = "Id"
    students_name = "Name"
    students_sex = "Sex"
    students_age = "Age"
    students_subject = "Subject"
    print(students[students_id].ljust(5), students[students_name].center(35),
          students[students_sex].ljust(10), students[students_age].ljust(5),
          students[students_subject].center(35))

#添加学生信息,press 1。
def add_students():
    '''学生信息包括Id、姓名、性别、年龄、专业。'''
    add_id = input("\n请输入您要添加的学生Id：")
    #搜索输入的ID是否和现有的ID有冲突,如果有给出提示,并中断输入.
    with open(filename) as search_id:
        for check_id in search_id: #遍历文件,逐行读取.当文件中有多行时,貌似只能这样做.
            add_stu_info = json.loads(check_id)  #json.loads将字符串转换成字典。
            if add_id == add_stu_info["Id"]:
                print("您添加的学生Id:%s已被使用,请更换一个." %add_id)
                return

    #如果不存在ID冲突,添加新用户,并保存进文件里.
    with open(filename, "a+") as add_f:
        add_name = input("请输入您要添加的学生姓名：")
        add_sex = input("请输入您要添加的学生性别：")
        add_age = input("请输入您要添加的学生年龄：")
        add_subject = input("请输入你要添加的学生专业:")
        #用于临时保存用户输入的信息,输入信息收集完整后,写入到文件里.
        students = {}
        students["Id"] = add_id
        students["Name"] = add_name
        students["Sex"] = add_sex
        students["Age"] = add_age
        students["Subject"] = add_subject
        #通过json.dump将字典写入文件里.
        #貌似直接用add_f.write(),无法将字典(students)写入到文件里.
        json.dump(students, add_f)
        add_f.write("\n") #输入完信息后,换行.否则所有的学生信息都在一行,无法给后续的搜索使用.
        print("添加成功.\n")

#修改学生信息,press 2
"""
def modify_students ():
    '''只能修改学生的姓名、性别、专业，学生Id无法修改。'''
    print ("\n只能修改学生的姓名、性别、专业，学生Id无法修改。")
    modify_id = input("请输入您要修改学生的Id:")
    stu_dicts = []
    with open(filename) as read_fs:
        for read_f in read_fs:
            mod_f = json.loads(read_f)
            stu_dicts.append(mod_f))
    

            with open(filename, "a+") as modify_info:

                '''如果上面检查没有冲突，添加到students字典里。'''
                mod_info["Name"] = input("请输入您要修改的学生姓名：")
                mod_info["Sex"] = input("请输入您要修改的学生性别：")
                mod_info["Age"] = input("请输入您要修改的学生年龄：")
                mod_info["Subject"] = input("请输入你要修改的学生专业:")
                print("您已成功完成修改。\n")
                return
    print("您输入的Id:%s不存在，请检查。\n" %modify_id)


#根据学生ID,删除相关信息,press 3
def del_student ():
    del_id = input("\n请输入您要删除的学生Id:")
    #检查到匹配的用户ID,直接把列表里的对应字典删除了.
    with open(filename, "a+") as del_files:
        for del_stu in range(len(students_info)):
            #找到列表对应的字典索引,然后删除该索引.
            if students_info[del_stu]["Id"] == del_id:
                del students_info[del_stu]
                print ("学生Id%s,删除成功.\n" %del_id)
                return
    print ("您输入的Id:%s存在，请检查。\n" %del_id)
"""

#根据学生ID查找学生信息,press 4
def search_student ():
    sear_id = input("\n请输入您要查找的学生Id:")
    with open(filename) as student_id:
        for stu_id in student_id:  #遍历文件,逐行读取.当文件中有多行时,貌似只能这样做.
            s_id = json.loads(stu_id) #json.loads将字符串转换成字典。
            if sear_id == s_id["Id"]:
                '''打印学生信息'''
                print_student_head()
                print_student_info(s_id)
                return
    print("您输入的Id:%s不存在，请检查。\n" %sear_id)

#查询所有的学生信息,press 5
def search_all_students ():
    #打印学生头部信息
    print_student_head()
    with open(filename) as all_info:
        for sear_all in all_info: #遍历文件,逐行读取.当文件中有多行时,貌似只能这样做.
            all_students = json.loads(sear_all) #json.loads将字符串转换成字典。
            print_student_info(all_students)
    print("--" * 20)

#程序主程序
def main_students ():
    while True:
        greet_welcome()
        press = input("\n请输入您的选择：")
        if press == "1":
            add_students()
        elif press == "2":
            modify_students()
        elif press == "3":
            del_student()
        elif press == "4":
            search_student()
        elif press == "5":
            search_all_students()
        else:
            print("您已选择退出操作.")
            break

main_students()