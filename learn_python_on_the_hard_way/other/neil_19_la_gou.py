#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 04
"""

# 题目：
# 你是一名体育老师，在某次课距离下课还有五分钟时，你决定搞一个游戏。此时有100名学生在上课。游戏的规则是：
# 1. 你首先说出三个不同的特殊数，要求必须是个位数，比如3、5、7。
# 2. 让所有学生拍成一队，然后按顺序报数。
# 3. 学生报数时，如果所报数字是第一个特殊数（3）的倍数，那么不能说该数字，而要说Fizz；如果所报数字是第二个特殊数（5）的
# 倍数，那么要说Buzz；如果所报数字是第三个特殊数（7）的倍数，那么要说Whizz。
# 4. 学生报数时，如果所报数字同时是两个特殊数的倍数情况下，也要特殊处理，比如第一个特殊数和第二个特殊数的倍数，那么不能
# 说该数字，而是要说FizzBuzz, 以此类推。如果同时是三个特殊数的倍数，那么要说FizzBuzzWhizz。
# 5. 学生报数时，如果所报数字包含了第一个特殊数，那么也不能说该数字，而是要说相应的单词，比如本例中第一个特殊数是3，那么
# 要报13的同学应该说Fizz。如果数字中包含了第一个特殊数，那么忽略规则3和规则4，比如要报35的同学只报Fizz，不报BuzzWhizz。
#
# 现在，我们需要你完成一个程序来模拟这个游戏，它首先接受3个特殊数，然后输出100名学生应该报数的数或单词。比如，
#
# 输入
# 3,5,7
# 输出（片段）
#
# 1
# 2
# Fizz



# list中的1到9 属性由int 转换成 str
def list_str():
    list_ = []
    for i in range(1, 10):
        i = str(i)
        list_.append(i)
    return list_

# 输出个位数，范围在1～9
def input_():
    print u"请输入一个自然数，数值范围在1～9。"
    num_ = raw_input(">")
    while num_ not in list_str():
        print u"输入值不符合条件，请重新输入一个自然数，数值范围在1～9。"
        num_ = raw_input(">")
    return num_

# 输出三个数互不相等
def diff():
    a = input_()
    b = input_()
    while a == b:
        print (u"该个位数已存在,已存在->"), a
        b = input_()
    c = input_()
    while c == a or c == b:
        print (u"该个位数已存在,已存在->"), a, (u"和"), b
        c = input_()
    print u"输入阶段已完成。"
    return int(a), int(b), int(c)

# 输入阶段，完成
# 进入，报数阶段

# 将int转换成str，再拆成list
def int_to_list(number_):
    list_ = []
    for i in str(number_):
        list_.append(i)
    return list_

# 报数
def number_off():
    # 获取三个特殊值
    a, b, c = diff()

    # 从1～100开始报数
    for number_ in range(1, 101):

        # 将int转换成str，再拆成list
        number_str = int_to_list(number_)

        # 第一个特殊数在数字中，排除其他规律，输出”Fizz“
        if str(a) in number_str:
            print "Fizz"

        else:
            # 条件1：被第1个特殊数整除
            message_1 = "Fizz" if number_ % a == 0 else ""
            # 条件2; 被第2个特殊数整除
            message_2 = "Buzz" if number_ % b == 0 else ""
            # 条件3： 被第3个特殊数整除
            message_3 = "Whizz" if number_ % c == 0 else ""
            # 条件4： 都不能被3个特殊数整除
            message_4 = str(number_) if (number_ % a != 0 and number_ % b != 0 and number_ % c != 0) else ""
            message = message_1 + message_2 + message_3 + message_4
            print message

if __name__ == "__main__":
    print u"一共需要输入三个自然数，数值范围在1～9。"
    number_off()
    print u"报数完毕，谢谢。"









