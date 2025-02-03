#Python使用加号(+)来合并字符串，这种方法称为拼接。通过拼接，可使用存储在变量中的信息来创建完整消息
first_name="wjx"
last_name="Ricardo"
full_name=first_name+" "+last_name
print("hello, "+full_name.title()+"!")
#空白泛指任何非打印字符，如空格，制表符(\t)和换行符(\n)等
#删除字符串末尾的空白用函数rstrip()；删除字符串开头的空白用函数lstrip()；同时删除字符串两端的空白用函数strip()
#要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中
saying=" how dare you! "
print(saying.rstrip())
print(saying.lstrip())
print(saying.strip())
print(full_name.capitalize())#将字符串的第一个字符转换为大写
print(full_name.lower())#转换字符串中所有大写字符为小写
print(full_name.title())#所有单词都是以大写开始，其余字母均为小写
print(full_name.upper())#转换字符串中的小写字母为大写
message='"A person who never made a mistake never tried anything new."'
famous_person="Albert Einstein"
print(famous_person+" once said, "+message)
#长字符串
#使用三引号，这让解释器能够识别表示字符串开始和结束位置的引号，因此字符串本身可以包含单引号和双引号，且无需使用反斜杠对换行符进行转义(单引号和双引号则必须要使用反斜杠进行转义)
print('''This is a very long string. It continues 
here. And it's not over yet. "hello world!"
Still here = This is a very long string. It continues \nhere. And it's not over yet. "hello world!"\nStill here''')
print("Hello \ world")
print("Hello \
world")
#常规字符串也可以在编辑代码的时候跨越多行，只要在行尾加上反斜杠，编译代码时反斜杠和换行符将忽略
print("This is a very long string. It continues \
here. And it's not over yet. hello world! \
Still here")
print\
    ("hello world")
print(1+3+4\
    +4)
#原始字符串，用前缀r表示。原始字符串不会对反斜杠做特殊处理，而是让字符串包含的每个字符都保持原样。
#原始字符串不能以单个反斜杠结尾(非要以反斜杠结尾，则可以通过拼接字符串实现)
print(r'Hello \n world')
print('Hello \n world')
print(r'C\:desktop\python''\\')
print('hello \ world\\')
#函数str()，将非字符串值表示为字符串
age=23
birthday="Happy "+str(age)+"rd birthday to you!"
print(birthday)

print("hello git")