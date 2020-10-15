import re
pattern1="cat"
pattern2="brid"
string="dog runs to cat"
print(re.search(pattern1,string))
print(re.search(pattern2,string))
ptn=r"r[au]n"
print(re.search(ptn,"dog runs to cat"))

string="""
dog runs to cat
I run to dog.
"""
print(re.search(r"^I",string))
print(re.search(r"^I",string,flags=re.M))
#re.M是re.MULTILINE 这个参数可以对每一行进行处理


# r"r[A-Z]n"
# r"r[a-z]n"
# r"r[0-9]n"
# r"r[0-9a-z]n"

# 按类型匹配
# 除了自己定义规则, 还有很多匹配的规则时提前就给你定义好了的. 下面有一些特殊的匹配类型给大家先总结一下, 然后再上一些例子.
# \d : 任何数字
# \D : 不是数字
# \s : 任何 white space, 如 [\t\n\r\f\v]
# \S : 不是 white space
# \w : 任何大小写字母, 数字和 “” [a-zA-Z0-9]
# \W : 不是 \w
# \b : 空白字符 (只在某个字的开头或结尾)
# \B : 空白字符 (不在某个字的开头或结尾)
# \\ : 匹配 \
# . : 匹配任何字符 (除了 \n)
# ^ : 匹配开头
# $ : 匹配结尾
# ? : 前面的字符可有可无

#重复匹配
# * : 重复零次或多次
# + : 重复一次或多次
# {n, m} : 重复 n 至 m 次
# {n} : 重复 n 次

# 举例
# # * : occur 0 or more times
# print(re.search(r"ab*", "a"))             # <_sre.SRE_Match object; span=(0, 1), match='a'>
# print(re.search(r"ab*", "abbbbb"))        # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>
#
# # + : occur 1 or more times
# print(re.search(r"ab+", "a"))             # None
# print(re.search(r"ab+", "abbbbb"))        # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>
#
# # {n, m} : occur n to m times
# print(re.search(r"ab{2,10}", "a"))        # None
# print(re.search(r"ab{2,10}", "abbbbb"))   # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

#找到内容的分组
match=re.search(r"(\d+),Date:(.+)","stu:4322321,Date:Jun/22/2019")
print(match.group())
print(match.group(1))
print(match.group(2))

#有时候组会很多，可以在括号开头写上 ?P<名字> 这样的形式给组定义个名字
match=re.search(r"(?P<stu>\d+),Date:(?P<date>.+)","stu:4322321,Date:Jun/22/2019")
print(match.group("stu"))
print(match.group("date"))


#findall
print(re.findall(r"r[ua]n","run ran ren"))
#这里的|是or的意思
print(re.findall(r"run|ran","run ran ren"))

#replace 匹配掉一些字符串
print(re.sub(r"r[au]ns","catches","dog runs to cat")) #dog catches to cat

#split 分割功能 ，产生一个列表保存所有单词
print(re.split(r"[,;\.]","a;b,c.d;e")) #['a', 'b', 'c', 'd', 'e']
