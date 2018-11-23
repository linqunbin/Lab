#学生管理系统1.0版本，数据存储在列表的字典里。

students_info = []
#开始程序后，主程序的欢迎界面。
def greet_welcome ():
    print ("\n欢迎进入学生管理系统。")
    print ("输入'1',添加学生信息。")
    print ("输入'2',修改学生信息。")
    print ("输入'3',删除学生信息。")
    print ("输入'4',查询学生信息。")
    print ("输入'5',查询所有学生信息。")
    print ("输入'6',退出此程序。")

#打印学生信息
def print_student_info ():
    print("%s\t%s\t%s\t%s\t%s" % ("ID", "姓名", "性别", "年龄", "专业"))

#添加学生信息,press 1。
def add_students ():
    '''学生信息包括ID、姓名、性别、专业。'''
    add_id = input ("\n请输入您要添加的学生ID：")
    if students_info:
        for stu_info in students_info:
            '''检查新增加的ID,是否和现有的ID有冲突。'''
            if stu_info["ID"] == add_id:
                print ("您输入的学生ID，已存在，请换一个。\n")
                return
    '''如果上面检查没有冲突，添加到students字典里。'''
    add_name = input ("请输入您要添加的学生姓名：")
    add_sex = input ("请输入您要添加的学生性别：")
    add_age = input ("请输入您要添加的学生年龄：")
    add_subject = input ("请输入你要添加的学生专业:")
    students = {}
    students["ID"] = add_id
    students["name"] = add_name
    students["sex"] = add_sex
    students["age"] = add_age
    students["subject"] = add_subject
    students_info.append(students)
    print ("添加成功.\n")

#修改学生信息,press 2
def modify_students ():
    '''只能修改学生的姓名、性别、专业，学生ID无法修改。'''
    print ("\n只能修改学生的姓名、性别、专业，学生ID无法修改。")
    modify_id = input("请输入您要修改学生的ID:")
    for mod_info in students_info:
        if mod_info["ID"] == modify_id:
            '''如果上面检查没有冲突，添加到students字典里。'''
            mod_info["name"] = input("请输入您要修改的学生姓名：")
            mod_info["sex"] = input("请输入您要修改的学生性别：")
            mod_info["age"] = input("请输入您要修改的学生年龄：")
            mod_info["subject"] = input("请输入你要修改的学生专业:")
            print ("您已成功完成修改。\n")
            return
    print ("您输入的ID不存在，请检查。\n")

#根据学生ID,删除相关信息,press 3
def del_student ():
    del_id = input("\n请输入您要删除的学生ID:")
    #检查到匹配的用户ID,直接把列表里的对应字典删除了.
    for del_stu in range(len(students_info)):
        #找到列表对应的字典索引,然后删除该索引.
        if students_info[del_stu]["ID"] == del_id:
            del students_info[del_stu]
            print ("学生ID%s,删除成功.\n" %del_id)
            return
    print ("您输入的ID不存在，请检查。\n")

#根据学生ID查找学生信息,press 4
def search_student ():
    sear_id = input("\n请输入您要查找的学生ID:")
    for sear_info in students_info:
        if sear_info["ID"] == sear_id:
            '''打印学生头部信息'''
            print_student_info()
            print ("%s\t%s\t%s\t%s\t%s\n"
                   %(sear_info["ID"], sear_info["name"],
                     sear_info["sex"], sear_info["age"],
                     sear_info["subject"]))
            return
    print ("您输入的ID不存在，请检查。\n")

#查询所有的学生信息,press 5
def search_all_students ():
    print_student_info()    #打印学生头部信息
    for sear_all in students_info:
        print ("%s\t%s\t%s\t%s\t%s"
               %(sear_all["ID"], sear_all["name"],
                 sear_all["sex"], sear_all["age"],
                 sear_all["subject"]))
    print ("--" * 20)

#程序主程序
def main_students ():
    try:
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
    except BaseException:
        print ("\n\n您的操作不正确,操作失败.\n\n")

main_students()