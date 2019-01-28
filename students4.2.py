"""
1 修复若干个Bug；
2 全面使用class做代码调试；
3 突出使用try except。
"""
import pymysql


class PrintInfo(object):
    """
    1 打印欢迎信息
    2 打印学生信息的标题
    """
    @staticmethod
    def greet():
        print("\n欢迎进入学生管理系统。")
        print("输入'1',添加学生信息。")
        print("输入'2',修改学生信息。")
        print("输入'3',查询学生信息。")
        print("输入'4',查询所有学生信息。")
        print("输入'5',删除学生信息。")
        print("输入'6',退出此程序。\n")

    @staticmethod
    def head_info():
        s_id = "ID"
        s_f_name = "First Name"
        s_l_name = "Last Name"
        s_sex = "Sex"
        s_age = "Age"
        s_subject = "Subject"
        print(s_id.ljust(5), s_f_name.center(20),
              s_l_name.center(15), s_sex.center(5),
              s_age.center(5), s_subject.center(20))


class ChoiceMenu(object):
    """
    当输出结束或输入有误时,给出选择提示.
    """
    def __init__(self):
        self.c_menu = input('选择"1"退出程序;选择"2"返回前面操作;选择其它返回主页面:')

    def choice_m(self):
        # 选择"1"退出程序;
        if self.c_menu == "1":
            print("\n您已经选择退出程序了,再见.\n")
            exit()

        # 选择"2"返回前面操作;
        elif self.c_menu == "2":
            return 2

        # 选择其它返回主页面:
        else:
            return 3


class CheckInput(object):
    """
    1 检查输入的内容是否为数字;
    2 检查输入的内容是否符合长度要求;
    3 检查输入的内容是否为性别.
    """
    # 输入的数字为5位
    sid_len_num = 5

    def __init__(self, val):
        self.val = val

    # 检查输入的内容是否为数字;
    def check_digit(self):
        if not self.val.isdigit():
            print("您输入的不对,请输入数字.\n")
            # 如果不匹配数字,则返回1,便于做条件判断.
            return 1

    # 检查输入的年龄;
    def check_age(self):
        if not (int(self.val) >= 1 <= 110):
            print("您输入的年龄不符合要求,年龄范围是1到110之间.")
            return 1

    # 检查输入的内容是否符合长度,以及第一位数字必须不能小于1开头;
    def check_len(self):
        # 检查输入的是否为5为数字,以及第一位是否为小于一.
        if len(self.val) != CheckInput.sid_len_num or int(self.val[0]) < 1:
            print("必须输入%d位长度,并且第一个数字必须大于等于1.\n" % CheckInput.sid_len_num)
            return 1

    # 检查输入的内容是否为性别.
    def check_sex(self):
        if not (self.val == "Male" or self.val == "Female"):
            print('请输入"Male"或"Female".\n')
            return 1


class InputPrompt(object):
    """
    提示输入的内容.
    """

    @staticmethod
    def id_input():
        s_id = input("请输入您要操作的学生ID:")
        return s_id

    @staticmethod
    def f_name_input():
        f_name = input("请输入您要操作的学生名字:")
        return f_name.title()

    @staticmethod
    def l_name_input():
        l_name = input("请输入您要操作的学生姓:")
        return l_name.title()

    @staticmethod
    def sex_input():
        sex = input("请输入您要操作的学生性别:")
        return sex.title()

    @staticmethod
    def age_input():
        age = input("请输入您要操作的学生年龄:")
        return age

    @staticmethod
    def subject_input():
        subject = input("请输入你要操作的学生科目:")
        return subject.title()


class DbMysql(object):
    db = pymysql.connect(host="192.168.0.100", user="bruce", passwd="lqb@126.COM", db="python3", charset='utf8')

    # 使用静态方法，添加ID时，检查输入的ID是否存在数据库
    @staticmethod
    def check_id_exist(s_id):
        # 使用cursor()方法获取操作游标
        cursor = DbMysql.db.cursor()
        # SQL 查询语句
        sql = "select * from students where id = %s" % s_id
        try:
            # 在每次运行sql之前，ping一次，如果连接断开就重连
            DbMysql.db.ping(reconnect=True)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                # 如果输入的ID已存在,返回1值.
                print("\n您输入的Id:%s已存在,请更换.\n" % s_id)
                DbMysql.db.close()
                return 1
        except Exception as ex:
            # 发生错误时回滚
            print("\n数据库操作出现异常,请联系系统管理员.异常代码为:\n%s" % ex)
            DbMysql.db.rollback()
        DbMysql.db.close()

    # 使用静态方法，修改、删除、查找ID时，是否存在数据库
    @staticmethod
    def check_id_not_exist(s_id):
        # 使用cursor()方法获取操作游标
        cursor = DbMysql.db.cursor()
        # SQL 查询语句
        sql = "select * from students where id = %s" % s_id
        try:
            # 在每次运行sql之前，ping一次，如果连接断开就重连
            DbMysql.db.ping(reconnect=True)
            cursor.execute(sql)
            result = cursor.fetchone()
            if not result:
                # 如果输入的ID不存在,返回1值.
                print("\n您输入的Id:%s不存在,请更换.\n" % s_id)
                DbMysql.db.close()
                return 1
        except Exception as ex:
            # 发生错误时回滚
            print("\n数据库操作出现异常,请联系系统管理员.异常代码为:\n%s" % ex)
            DbMysql.db.rollback()
        DbMysql.db.close()

    @staticmethod
    def s_add(s_id, f_name, l_name, sex, age, subject):
        # 使用cursor()方法获取操作游标
        cursor = DbMysql.db.cursor()
        # SQL 插入语句
        sql = "insert into students(id, first_name, last_name, sex, age, subject) \
        values (%s, %s, %s, %s, %s, %s)"

        """
        下面这种配置方法不行,出现报错:
        sql = "insert into students(id, first_name, last_name, sex, age, subject) \
        values (%s, %s, %s, %s, %s, %s)" % (s_id, f_name, l_name, sex, age, subject)
        报如下错误:
        (1054, "Unknown column 'XX' in 'field list'")
        """

        params = [s_id, f_name, l_name, sex, age, subject]
        try:
            # 在每次运行sql之前，ping一次，如果连接断开就重连。
            DbMysql.db.ping(reconnect=True)
            cursor.execute(sql, params)
            DbMysql.db.commit()
            print("\n学生ID:%s,添加成功.\n" % s_id)
        except Exception as ex:
            # 发生错误时回滚
            print("数据库操作出现异常,请联系系统管理员.异常代码为:\n%s" % ex)
            DbMysql.db.rollback()
        DbMysql.db.close()

    @staticmethod
    def s_modify(s_id, f_name, l_name, sex, age, subject):
        # 使用cursor()方法获取操作游标
        cursor = DbMysql.db.cursor()
        # SQL 更新语句
        sql = "update students set first_name = %s, last_name = %s, sex = %s, age = %s, subject = %s where id = %s"
        params = [f_name, l_name, sex, age, subject, s_id]
        try:
            # 在每次运行sql之前，ping一次，如果连接断开就重连
            DbMysql.db.ping(reconnect=True)
            cursor.execute(sql, params)
            DbMysql.db.commit()
            print("\n学生ID:%s,修改成功.\n" % s_id)
        except Exception as ex:
            print("您的操作有误,错误信息如下:\n%s" % ex)
        DbMysql.db.close()

    @staticmethod
    def s_search(s_id):
        # 使用cursor()方法获取操作游标
        cursor = DbMysql.db.cursor()
        # SQL 查询语句
        sql = "select * from students where id = %s" % s_id
        try:
            # 在每次运行sql之前，ping一次，如果连接断开就重连
            DbMysql.db.ping(reconnect=True)
            cursor.execute(sql)
            results = cursor.fetchone()
            print(str(results[0]).ljust(5), results[1].center(20),
                  results[2].center(15), results[3].center(5),
                  str(results[4]).center(5), results[5].center(20))
        except Exception as ex:
            # 发生错误时回滚
            print("数据库操作出现异常,请联系系统管理员.异常代码为:\n%s" % ex)
            DbMysql.db.rollback()
        DbMysql.db.close()

    @staticmethod
    def search_all():
        # 使用cursor()方法获取操作游标
        cursor = DbMysql.db.cursor()
        # SQL 查询语句
        sql = "select * from students"
        try:
            # 在每次运行sql之前，ping一次，如果连接断开就重连
            DbMysql.db.ping(reconnect=True)
            cursor.execute(sql)
            results = cursor.fetchall()
            if results:
                for result in results:
                    print(str(result[0]).ljust(5), result[1].center(20),
                          result[2].center(15), result[3].center(5),
                          str(result[4]).center(5), result[5].center(20))
            else:
                print("\n当前数据库为空。\n")

        except Exception as ex:
            # 发生错误
            print("数据库操作出现异常,请联系系统管理员.异常代码为:\n%s" % ex)
        DbMysql.db.close()

    @staticmethod
    def s_del(s_id):
        # 使用cursor()方法获取操作游标
        cursor = DbMysql.db.cursor()
        # SQL 删除语句
        sql = "delete from students where id = %s" % s_id
        try:
            DbMysql.db.ping(reconnect=True)
            cursor.execute(sql)
            DbMysql.db.commit()
            print("\n学生ID:%s,删除成功.\n" % s_id)
        except Exception as ex:
            # 发生错误时回滚
            print("数据库操作出现异常,请联系系统管理员.异常代码为:\n%s" % ex)
            DbMysql.db.rollback()
            DbMysql.db_close()

    @staticmethod
    def db_close():
        DbMysql.db.close()


class Students(object):
    """
    添加、修改、查看、删除都在这个类里。
    """
    def __init__(self):
        pass

    # 添加学生
    @staticmethod
    def add_students():
        while True:
            # 提示输入内容:
            s_id = InputPrompt.id_input()

            # input输入的ID,并做输入ID的检查。
            s_check_id = CheckInput(s_id)

            # 检查输入的是否为数字以及长度是否为5位,当输入的不符合检查条件情况下,执行if命令操作;
            if s_check_id.check_digit() == 1 or s_check_id.check_len() == 1:
                # 当输入有误时,给出选择提示.
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            # 检查输入的ID是否在数据库中已存在:
            if DbMysql.check_id_exist(s_id) == 1:
                # 当输入有误时,给出选择提示.
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            s_f_name = InputPrompt.f_name_input()
            s_l_name = InputPrompt.l_name_input()
            s_sex = InputPrompt.sex_input()
            s_check_sex = CheckInput(s_sex)
            # 检查输入的性别
            if s_check_sex.check_sex() == 1:
                # 当输入有误时,给出选择提示:
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            s_age = InputPrompt.age_input()
            s_check_age = CheckInput(s_age)
            # 检查输入的年龄是否为数字.
            if s_check_age.check_digit() == 1 or s_check_age.check_age() == 1:
                # 当输入有误时给出的选择提示:
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            s_subject = InputPrompt.subject_input()

            # 把输入信息提交给数据库
            DbMysql.s_add(s_id, s_f_name, s_l_name, s_sex, s_age, s_subject)

            # 学生信息添加完毕后,继续给出选择提示:
            c_menu = ChoiceMenu()
            if c_menu.choice_m() == 2:
                continue
            elif c_menu.choice_m() == 3:
                return

    # 修改学生
    @staticmethod
    def modify_students():
        while True:
            # 提示输入内容:
            s_id = InputPrompt.id_input()

            # input输入的ID,并做输入ID的检查。
            s_check_id = CheckInput(s_id)

            # 检查输入的是否为数字以及长度是否为5位,当输入的不符合检查条件情况下,执行if命令操作;
            if s_check_id.check_digit() == 1 or s_check_id.check_len() == 1:
                # 当输入有误时,给出选择提示.
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            # 检查输入的ID是否在数据库中已存在:
            if DbMysql.check_id_not_exist(s_id) == 1:
                # 当输入有误时,给出选择提示.
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            # 显示要修改学生的信息：
            PrintInfo.head_info()
            DbMysql.s_search(s_id)

            s_f_name = InputPrompt.f_name_input()
            s_l_name = InputPrompt.l_name_input()
            s_sex = InputPrompt.sex_input()
            s_check_sex = CheckInput(s_sex)
            # 检查输入的性别
            if s_check_sex.check_sex() == 1:
                # 当输入有误时,给出选择提示:
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            s_age = InputPrompt.age_input()
            s_check_age = CheckInput(s_age)
            # 检查输入的年龄是否为数字.
            if s_check_age.check_digit() == 1 or s_check_age.check_age() == 1:
                # 当输入有误时给出的选择提示:
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            s_subject = InputPrompt.subject_input()

            DbMysql.s_modify(s_id, s_f_name, s_l_name, s_sex, s_age, s_subject)

            # 操作完成后，给出提示操作
            c_menu = ChoiceMenu()
            if c_menu.choice_m() == 2:
                continue
            elif c_menu.choice_m() == 3:
                return

    # 搜索单个学生
    @staticmethod
    def search_students():
        while True:
            # 提示输入内容:
            s_id = InputPrompt.id_input()

            # input输入的ID,并做输入ID的检查。
            s_check_id = CheckInput(s_id)

            # 检查输入的是否为数字以及长度是否为5位,当输入的不符合检查条件情况下,执行if命令操作;
            if s_check_id.check_digit() == 1 or s_check_id.check_len() == 1:
                # 当输入有误时,给出选择提示.
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            # 检查输入的ID是否在数据库中已存在:
            if DbMysql.check_id_not_exist(s_id) == 1:
                # 当输入有误时,给出选择提示.
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            # 显示要搜索学生的信息：
            PrintInfo.head_info()
            DbMysql.s_search(s_id)

            # 操作完成后，给出提示：
            c_menu = ChoiceMenu()
            if c_menu.choice_m() == 2:
                continue
            elif c_menu.choice_m() == 3:
                return

    # 搜索全部学生
    @staticmethod
    def search_all_students():
        while True:
            PrintInfo.head_info()
            DbMysql.search_all()
            # 显示完后，给出选择
            c_menu = ChoiceMenu()
            if c_menu.choice_m() == 2:
                continue
            elif c_menu.choice_m() == 3:
                return

    # 删除学生信息
    @staticmethod
    def del_students():
        while True:
            # 提示输入内容:
            s_id = InputPrompt.id_input()

            # input输入的ID,并做输入ID的检查。
            s_check_id = CheckInput(s_id)

            # 检查输入的是否为数字以及长度是否为5位,当输入的不符合检查条件情况下,执行if命令操作;
            if s_check_id.check_digit() == 1 or s_check_id.check_len() == 1:
                # 当输入有误时,给出选择提示.
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            # 检查输入的ID是否在数据库中已存在:
            if DbMysql.check_id_not_exist(s_id) == 1:
                # 当输入有误时,给出选择提示.
                c_menu = ChoiceMenu()
                if c_menu.choice_m() == 2:
                    continue
                elif c_menu.choice_m() == 3:
                    return

            # 显示要搜索学生的信息：
            PrintInfo.head_info()
            DbMysql.s_search(s_id)

            # 执行删除学生动作
            DbMysql.s_del(s_id)

            # 操作完成后，给出提示
            c_menu = ChoiceMenu()
            if c_menu.choice_m() == 2:
                continue
            elif c_menu.choice_m() == 3:
                return


class Main(object):
    """
    程序的主程序
    """
    def __init__(self):
        pass

    @staticmethod
    def menu():
        while True:
            PrintInfo.greet()
            press = input("\n请输入您的操作:")
            press = int(press)
            try:
                if press >= 1 <= 6:
                    if press == 1:
                        Students.add_students()
                    elif press == 2:
                        Students.modify_students()
                    elif press == 3:
                        Students.search_students()
                    elif press == 4:
                        Students.search_all_students()
                    elif press == 5:
                        Students.del_students()
                    elif press == 6:
                        exit()
                else:
                    print("\n您的输入有误，请输入1到6的选择\n")

            except Exception as ex:
                print("\n您的输入有误，请输入1到6的选择。错误代码如下：\n%s" % ex)


if __name__ == '__main__':
    try:
        Main.menu()
    except Exception as ex1:
        print("您已退出程序。")
