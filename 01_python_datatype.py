'''
import keyword
print(keyword.kwlist)
'''
#예를 들어서, False, True 등의 철자를 확인할 수 있다. 어떤 키워드가 있는지 확인해본 것.

#변수의 생성과 삭제
#변수 입력할 때, 밀크타입?은 데이터의 타입을 명시하지 않는 것. 스트롱?타입은 데이터의 타입을 명시해야 한다. C가 스트롱타입.
#내가 변수를 가지고 있는 게 아니라, 메모리 어딘가에 저장된 값을 가르키는 주소를 가지게 되는 것.
my_var = 100
print(my_var)

'''
del my_var
print(my_var)
'''


#파이썬의 데이터 타입
#파이썬의 built-in data type (이미 정의되어 있는 데이터 타입)
# Numeric(숫자형. 정수 실수 구별 안 함), Sequence(리스트 같은 거), Text Sequence (문자열), Set, Mapping, Bool

#Numeric Type

# int(정수), float(실수), complex(복소수)
# a = 100
# b = 3.141592
# c = 1 + 2j
# print(type(a))
# print(type(b))
# print(type(c))

# d = 0o34 #8진수로 34. int
# e = 0xAB #16진수. int

my_result = 3 / 4
print(my_result)
#기본적으로 모든 컴퓨터 언어에서는 같은 타입끼리만 연산한다.
#그래서 지금 정수랑 정수를 계산했으니까 답을 정수가 따라간다.
#반면, 파이썬에서는 그대로 계산한다. 다른 언어에서는 0이 나올 것.

my_result = 10 % 3   #나머지
print(my_result)

my_result = 10 // 3   #몫
print(my_result)


#Text Sequence Type (str)

#문자는 한글자, 문자열은 두글자 이상으로 구성
#문자를 표현할 때 다른 언어는, ''
#문자열을 표현할 때 다른 언어는, ""
#근데 파이썬은 문자라는 게 없다. 그냥 다 문자열이다. 그래서 구분없이 그냥 사용한다.

a = 'hello'
b = "k"
c = 'Python'
print(a, b, c)

#문자열 연산
first = 'haha'
second = 'hoho'
print(first + second)
print(first + str(10))
print(first * 3)
#indexing
my_var = 'hello'
print(my_var[-3])
#slicing
print(my_var[0:3])
my_var = '이것은소리없는아우성!!'
print(my_var[0:5])

#in , not in 연산자
myStr = 'This is a sample Text'
print('sample' in myStr)      #True가 문자열로 출력된다.
print('Sample' not in myStr)

#formatting
myStr = '나는 사과를 %d개 가지고 있어요.' %3
print(myStr)

num_apple = 10
myStr = '나는 사과를 %d개 가지고 있어요.' %num_apple
print(myStr)

num_apple = 100
myStr = '나는 사과를 {}개 가지고 있어요.' .format(num_apple)
print(myStr)

num_apple = 100
myStr = '나는 사과를 {}개, 바나나를 {}개 가지고 있어요.' .format(num_apple, num_apple + 100)
print(myStr)
#문자열의 포맷팅은 주로 이 형태를 사용한다.


#문자열 method를 이용해서 문자열 처리를 할 수 있어요!!
myStr = 'cocacola'
print(len(myStr))         #len()라는 '함수'를 이용.
print(myStr.count('c'))   #str의 count()라는 'method'를 이용.
print(myStr.find('o'))

myStr = '   myhobby'
print(myStr.upper())
print(myStr.strip())


#Sequence Type
#list
#임의의 객체(데이터)를 순서대로 저장하는 집합 자료형.
#list는 literal로 표현할 때 [] (그야말로 코드로 표현할 때)
my_list = []
print(type(my_list))
my_list = list() #이건 함수로 표현했을 때.
my_list = [1, 2, 3]
my_list = [1, 2, 3, 'hello']
my_list = [1, 2, 3, [5, 6], 'bye']  #중첩 리스트
print(my_list[-2])     #인덱싱은 요소만 떼어오는 것.
print(my_list[3:4])    #슬라이싱은 원래의 형태에서 일정부분을 띄어오는 것. 그래서 원래의 형태가 유지된 채로 추출.


#list연산
a = [1, 2, 3]
b = [4, 5 ,6]
print(a + b)

a = [1, 2, 3]
a[0] = 5
print(a)
a[0:1] = [7, 8, 9]   #여기서는 이만큼의 리스트를 바꾸는거고,
print(a)
a[0] = [7, 8, 9]     #여기서는 그냥 요소 하나는 통으로 바꾸는 거고.
print(a)

a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6, 7])
print(a)
#그러니까 +연산은 concat하는 거고, append는 요소적으로 붙이는 거.

my_list = ['홍길동', '아이유', '강감찬', '신사임당', 'Kim']
result = my_list.sort()  #객체를 바꾸고, 얘는 그냥 출력시에만 정렬해서 보여주는 것. 그래서 result에 return되지 않는다.
print(result)
print(my_list)


#tuple
#일단 한 번 만들어지면 내용 변경이 안 된다.
a = (3)  #이렇게 하면 연산인지 튜플인지 애매하다.
print(a)
a = (3,)  #이렇게 하면 요소가 1개인 튜플이다.
print(a)

a = 1, 2, 3
print(type(a))  #튜플은 괄호를 생략할 수 있다.

a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)

#range
#주로 반복문에서 사용.
#같은 데이터를 적은양의 데이터로 표현이 가능.
my_range = range(10)
print(7 in my_range)
print(my_range[4])
print(my_range[1:4])   #원래 객체가 range니까 슬라이싱도 당연히  range로 나온다.



#dictionary
#기본적으로 key와 value로 데이터를 저장하는 구조.
a = {'name':'홍길동', 'age':45}
print(list(a.keys()))
print(list(a.values()))
print(a.items())



#bool -> boolean(True, False)
#and, or, not 연산자를 사용할 수 있다.

#다음의 경우는 Python에서 False로 간주한다.
# 1. 빈 문자열
# 2. 빈 리스트
# 3. 빈 튜플
# 4. 빈 딕셔너리
# 5. 숫자 0
# 6. None (그렇다고 이게 boolean은 아니다.)

a = 5
b = 0
print(a and b)
#and연산은 기본적으로 boolean끼리 하는 거니까, 5는 True로, 0은 False로 간주해서 연산.

print(a & b)  #비트연산. 그래서 각각을 2진수로 바꾼다.
# 0101 & 0000 -> 0000  (둘 다 1이어야 1로 된다.)
print(a | b)


#Set
#집합 자료형이고 중복을 허용하지 않는다
#순서가 존재하지 않는 자료형

my_set = {1, 2, 3, 4, 1, 2}
print(my_set)
my_list = [1, 2, 3, 4, 1, 2]
my_set = set(my_list)
print(my_set)

my_str = 'hello'
my_set = set(my_str)
print(my_set)  #순서가 없으니까 어떤 식으로 가지고 있는지는 중요하지 않다.

#set에서 사용하는 연산자
# 합집합: uninon , |
# 교집합: intersection , &
# 차집합: difference , -

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}


#날짜
#date 와 datetime에 대해서 알아보자.

from datetime import date, datetime
today = date.today()
print(today)
#오늘 날짜는 : 2020년 7월 15일 입니다.
my_str = '오늘 날짜는 : {}년 {}월 {}일 입니다.'
my_str = my_str.format(today.year, today.month, today.day)
print(my_str)

my_datetime = datetime.today()
print(my_datetime)
print('현재시간은: {}시 입니다.' .format(my_datetime.hour))
print('현재시간은: {}시 {}분 입니다.' .format(my_datetime.hour, my_datetime.minute))

#날짜 연산
#오늘이 07월 15일이예요.
#내일의 날짜는 07월 16일이예요.

#오늘이 01월 31일이예요.
#내일의 날짜는 02월 01일이예요.

#오늘이 03월 01일이예요.
#어제의 날짜는 02월 ??일이예요.

#결론적으로 날짜 연산은 처리하기 힘들다. 계산으로 처리하지 않는다.
#delta이용해서 처리.
from datetime import date, timedelta
today = date.today()
days = timedelta(days = -20)  #날짜 차이가 -1이다. -> 하루 전을 의미한다.
print(today + days)

today = datetime.today()
hours = timedelta(hours = 3)  #3시간 뒤를 알려준다.
print(today + hours)

#한 달 전 날짜
#예) 오늘 날짜가 3월 31일 -> 1달 전 날짜는? 그냥 30일, 31일 빼서는 구할 수 없다.
today = date.today()
#여기서 timedelta에는 month, year는 없다.
'''
from dateutil.relativedelta imort relativedelta
지금 이거 모듈 다운로드가 안 됨.

today = date.today()
months = relativedelta(months = -1)
print(today + months)

#문자열로 되어있는 날짜를 진짜 날짜로 변환해서 연산하는 방법.
from dateuil.parser import parse
my_date = parse('2019-01-30')
print(my_date)

from datetime import datetime
my_date = datetime(2019, 1, 30)
#숫자로 되어 있을 때는 parse말고 datetime을 사용.

'''
