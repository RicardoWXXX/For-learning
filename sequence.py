#数据结构：以某种方式（比如通过编号）组合起来的数据元素(数、字符乃至其他数据结构)集合
#序列(sequence)：序列中每个元素都有编号，即其位置或索引，其中第一个元素索引为0，第二个元素索引为1，以此类推
edward=["Edward",43]
john=["John",14]
database=[edward,john]
print(database)
print(edward[1])
#适用于所有序列的操作：索引，切片，相乘，成员资格检查，部分内置函数
#1.索引indexing
greeting='Hello'
print(greeting[0])
meizu='he llo'
print(meizu[2])
print(meizu[-1])#使用负数索引时，将从右(最后一个元素)开始往左数
print('hello'[2])#对于字符串字面量(以及其他序列字面量)，可以直接对其索引操作
forth=input('Year: ')[3]#如果调用函授返回一个序列，可以直接对其执行索引操作
print(forth)
#示例
months=['January','February','March','April','May','June','July','August','September','October','November','December']
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year=input('Year: ')
month=input('Month(1-12): ')
day=input('Day(1-31): ')
month_number=int(month)
day_number=int(day)
month_name=months[month_number-1]
ordinal=day+endings[day_number-1]
print(month_name+' '+ordinal+', '+year)
#1st--first，2nd--second，3rd--third，4th--fourth，5th--fifth，6th--sixth，7th-seventh，8th--eighth，9th--ninth，10th--tenth，11th--eleventh，12th--twelfth，13th--thirteenth，14th--fourteenth，15th--fifteenth，16th--sixteenth，17th--seventeenth，18th--eighteenth，19th--nineteenth，20th--twentieth，21st-twenty-first，22nd--twenty-second，23rd--twenty-third，24th，25th，26th，27th，28th，29th，30th，31st
#2.切片(slicing),访问特定范围内地元素
tag='<a href="http://www.python.org">python web site</a>'
print(tag[9:30])
print(tag[32:-4])#第一个索引是包含的第一个元素的编号，第二个索引是切面后余下的第一个元素的编号
number=[1,2,3,4,5,6,7,8,9,10]
number[3:6]
print(number[3:6])#即提供两个索引来指定切片的边界，第一个索引指定的元素包含在切片内，第二个索引指定的元素不包含在切片内
print(number[7:10])
print(number[-3:-1])
print(number[-3:0])#如果第一个索引指定的元素位于第二个索引指定的元素后面，结果为空序列
print(number[-3:])
print(number[:3])
print(number[:])#要复制整个序列，可以将两个索引都省略
#更大的步长
print(number[0:10:1])#步长为1
print(number[0:10:2])#步长为2
print(number[3:6:3])#步长为3
print(number[::3])
print(number[8:3:-1])#步长能为0，否则无法向前移动，但可以为复数，即从右向左提取元素
print(number[10:0:-1])
print(number[:5])
print(number[:5:-1])

print(number[-5:-1:-1])
print(number[-3:0:-1])#步长为正：第一个索引的元素位于第二个索引元素前面（从左到右提取元素）;补偿为负：第一个索引的元素位于第二个索引元素后面（从右往左提取元素）
#索引省略的，则表示按当前元素提取顺序，依次按步长提取到头,且到头的索引指定的元素不包含在切片中
#2.2.3序列相加
#可使用加法运算来拼接序列
print([1,2,3]+[3,4,5])
#一般而言，不能拼接不同类型的序列

#2.2.4乘法
print('Python'*4)
print([23]*3)#将序列余数x相乘时，将重复这个序列x次来创建一个新序列
 
 #None、空列表和初始化
 #空列表是使用不包含任何内容的两个方括号（[]）表示的
sequence=[None]*10#None表示什么都没有，将列表的长度初始化为10
print(sequence)
Sentence=input("Please input a sentence: ")
print('+'+'- '*18+'+')
print('|'+' '*36+'|')
print('|'+Sentence +'|')
print('|'+' '*36+'|')
print('+'+'- '*18+'+')

sentence=input("Sentence: ")
screen_width=80
text_width=len(sentence)
box_width=text_width+4
left_margin=(screen_width-box_width)//2
print()
print(' '*left_margin+'+'+'-'*(box_width-2)+'+')
print(' '*left_margin+'| '+' '*text_width+' |')
print(' '*left_margin+'| '+ sentence+' |')
print(' '*left_margin+'| '+' '*text_width+' |')
print(' '*left_margin+'+'+'-'*(box_width-2)+'+')
print()

#2.2.5成员资格
#要检车特定的值是否包含在序列中，可以使用运算符in；它检查是否满足指定的条件，并返回相应的值：满足时返回True，不满足时返回False。（这样的运算符称为布尔运算符，前述真值称为布尔值）
permissions='rw'
print('w'in permissions)
print('x' in permissions)
users=['mlh','foo','bar']
print(input('Enter your user name: ') in users)


database=[['albert','1234'],['dilbert','erer'],['smith','2345'],['jone','9523']]
username=input('User name: ')#只能由字母、数字和下划线构成，且不能以数字打头
pin=input('PIN code: ')
if [username,pin] in database: print('Access granted')

#长度、最小值和最大值
#内置函数len，min和max分别返回序列包含的元素个数，序列中最小和最大的值。
number=[100,34,678]
print(len(number))
print(max(number))
print(min(number))
print(max(2,4))
print(min(2,4,5,6))

