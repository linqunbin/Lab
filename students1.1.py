# 数据存储在列表里,来做学生管理系统.
"""
优化了添加学生时,如果添加的Id冲突时,跳到主程序.
目前修改为,当检测到有冲突的Id时,直接循环提示再输入要添加新的Id.
"""
# 学生信息,保存在下面列表里.
students_lists = []

# 开始程序后，主程序的欢迎界面。
def greet_welcome():
    print("\n欢迎进入学生管理系统。")
    print("输入'1',添加学生信息。")
    print("输入'2',修改学生信息。")
    print("输入'3',删除学生信息。")
    print("输入'4',查询学生信息。")
    print("输入'5',查询所有学生信息。")
    print("输入'6',退出此程序。")


# 打印学生头部信息
def print_student_head():
    students_id = "Id"
    students_name = "Name"
    students_age = "Age"
    students_sex = "Sex"
    students_subject = "Subject"
    print(students_id.ljust(5), students_name.center(35),
          students_age.ljust(10), students_sex.ljust(5),
          students_subject.center(35))


# 添加学生信息时,输入的Id临时存放这个列表里.
student_id = []

# 添加学员信息,定义检查冲突的函数.
def add_check():
    flag = 0
    while flag < 3:
        t_id = input("请输入您要添加的Id:")
        if students_lists:  # 如果students_lists列表不为空,那么If语句则为True.
            for student_list in students_lists:
                if student_list["Id"] == t_id:
                    print("您要添加的Id:%s已存在,请更换一个Id." % t_id)  # 当Id冲突时,提示Id已存在.
                    break  # 如果检查到输入Id有冲突,直接跳过下面的else语句执行,再次进入while循环要求输入添加的Id.
            else:  # 如果输入的Id,检测发现没有冲突,那么执行如下代码.
                student_id[0] = t_id  # 将t_id的变量值,放到索引0里.
                flag = 4  # 中断while循环.

        else:  # 如果上面的if语句不匹配,也就是students_lists为None的时,执行如下代码.
            student_id.append(t_id)  # 如果t_id的变量,与现有Id不冲突,则放到这个列表里.
            flag = 4  # 中断while循环.

def add_student():
    # students_dict = {} 如果将字典放在这个位置,会导致添加完用户,按2循环添加时,
    # 新增加用户会覆盖students_lists的原来用户,不知为何.

    while True:
        students_dict = {}  # 临时存放添加学生的信息
        add_check()
        a_name = input("请输入您要添加学生的名字:")
        a_age = input("请输入您要添加学生的年龄:")
        a_sex = input("请输入您要添加学生的性别:")
        a_subject = input("请输入您要添加学生的学科:")
        students_dict["Id"] = student_id[0]  # 取变量的第一个索引,实际上也只会有一个索引.
        students_dict["Name"] = a_name
        students_dict["Age"] = a_age
        students_dict["Sex"] = a_sex
        students_dict["Subject"] = a_subject
        students_lists.append(students_dict)
        print("学员信息添加成功.")
        choice = input('按"1"返回主页面;按"2"继续添加,按其它任意键,退出程序:')
        if choice == "1":  # 返回主程序
            return
        elif choice == "2":
            continue
        else:  # 退出程序
            exit("您已近选择退出程序,再见.")

def modify_student():
    while True:
        m_id = input("请输入您要修改的Id:")
        if students_lists:
            for update_student in students_lists:
                if update_student["Id"] == m_id:
                    print("您要修改的学员Id:%s信息如下:\n" % m_id)
                    print_student_head()
                    print(update_student["Id"].ljust(5), update_student["Name"].center(35),
                          update_student["Age"].ljust(10), update_student["Sex"].ljust(5),
                          update_student["Subject"].center(35), "\n")
                    choice1 = input('按"1"返回主页面,按"2"继续修改,按其它任意键,退出程序:')
                    if choice1 == "1":  # 返回主页面
                        return
                    elif choice1 == "2":  # 继续修改
                        m_name = input("请输入您要修改学生的名字:")
                        m_age = input("请输入您要修改学生的年龄:")
                        m_sex = input("请输入您要修改学生的性别:")
                        m_subject = input("请输入您要修改学生的学科:")
                        update_student["Name"] = m_name
                        update_student["Age"] = m_age
                        update_student["Sex"] = m_sex
                        update_student["Subject"] = m_subject
                        print("Id:%s信息修改成功.\n" % m_id)
                        break  # 修改成功后,跳出For循环.
                    else:  # 退出程序
                        exit("您已近选择退出程序,再见.")
            else:
                print("您输入的Id:%s不存在,请检查并重新输入:" % m_id)
                continue  # 重新循环,提示输入修改的Id.

            # 修改成功后,提示是否返回主页面或者继续修改,或者退出程序.
            choice2 = input('按"1"返回主页面,按"2"继续修改,按其它任意键,退出程序:')
            if choice2 == "1":
                return
            elif choice2 == "2":
                continue
            else:
                exit("您已近选择退出程序,再见.")
        else:
            print("目前数据库是空的,请有数据后在修改.")
            choice2 = input('按"1"返回主页面,按"2"继续修改,按其它任意键,退出程序:')
            if choice2 == "1":
                return
            elif choice2 == "2":
                continue
            else:
                exit("您已近选择退出程序,再见.")

def del_student():
    while True:
        del_stu = input("请输入您要删除的学生Id:")
        for del_number in range(len(students_lists)):
            if students_lists[del_number]["Id"] == del_stu:
                del students_lists[del_number]
                print("学生Id:%s已删除." % del_stu)
                break
        else:
            print("您输入的Id:%s不存在,请检查." % del_stu)

        choice = input('按"1"返回主页面;按"2"继续删除,按其它任意键,退出程序:')
        if choice == "1":  # 返回主程序
            return
        elif choice == "2":
            continue
        else:  # 退出程序
            exit("您已近选择退出程序,再见.")

def search_student ():
    while True:
        search_s = input("请输入您要搜索学生的Id:")
        for s_student in students_lists:
            if s_student["Id"] == search_s:
                print("您要查询的学员Id:%s信息如下:" % search_s)
                print_student_head()
                print(s_student["Id"].ljust(5), s_student["Name"].center(35),
                      s_student["Age"].ljust(10), s_student['Sex'].ljust(5),
                      s_student["Subject"].center(35))
                break
        else:
            print("您输入的Id:%s不存在,请检查." % search_s)

        choice = input('按"1"返回主页面;按"2"继续搜索,按其它任意键,退出程序:')
        if choice == "1":  # 返回主程序
            return
        elif choice == "2":
            continue
        else:  # 退出程序
            exit("您已近选择退出程序,再见.")

def search_all_student():
    print_student_head()
    for sear_all_s in students_lists:
        print(sear_all_s["Id"].ljust(5), sear_all_s["Name"].center(35),
              sear_all_s["Age"].ljust(10), sear_all_s['Sex'].ljust(5),
              sear_all_s["Subject"].center(35))
    return

while True:
    greet_welcome()
    press = input("请输入您的选择:")
    if press == "1":
        add_student()

    elif press == "2":
        modify_student()

    elif press == "3":
        del_student()

    elif press == "4":
        search_student()

    elif press == "5":
        search_all_student()

    else:
        exit("您已近选择退出程序,再见.")