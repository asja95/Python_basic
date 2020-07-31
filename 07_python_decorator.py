#Decorator

#dacorator의 사전적 의미는, 장식가, 모배업자
#python에서 Dacorator는 기존의 코드에 여러가지 기능을 추가하는 구문이라고 이해하면 편하다.

#Closure
#파이썬은 일급함수를 지원하는 언어다.
#1. 파이썬의 함수는 변수에 저장할 수 있다.
#2. 함수의 인자로 함수를 이용할 수 있다.
#3. 함수의 결과값(리턴값)으로 함수를 이용할 수 있다.

def my_outer_func(func) :   #함수를 인자로 받는다.

    def my_inner_func() :
         func()      #인자로 들어온 함수를 실행하겠다.

    return my_inner_func      #함수의 실행코드를 리턴한다. 결과값을 리턴하는 것과는 다르다.

def my_func() :
    print('my_func() 함수가 호출되었습니다.')

my_outer_func(my_func)      #아무것도. 실행코드만 리턴한 격이니까.
my_outer_func(my_func)()    #my_func함수가 실행되어서 리턴된다. 리턴받은 inner함수의 실행코드를 실행한 거니까.

decorated_my_func = my_outer_func(my_func)
decorated_my_func()
my_func()

import time
def my_outer_func(func) :

    def my_inner_func() :
        print('{} 함수 수행 시간을 계산합니다.' .format(func.__name__))
        start = time.time()   #1970년 1월 1일 0시 0분 0초 = 0  --> 1초마다 하나씩 올라간다.
        func()    #이 함수가 중간에 있으니까, 이 함수의 실행 시간을 계산할 수 있게 된다.
        end = time.time()
        print('함수 수행 시간은 {}입니다.' .format(end - start))

    return my_inner_func

def my_func() :
    print('my_func() 함수가 호출되었습니다.')

decorated_my_func = my_outer_func(my_func)
decorated_my_func()
#기존 코드에 새로운 코드를 추가해서 수행하 수 있도록 해준다.
#원래 함수 자체는 수정하고 싶지 않고 말 그대로 데코하는 걸 가능하게 해주는 것.
#위 코드에서 원래 함수는 그대로 수행하되, 함수 수행시간을 계산한 것처럼.
#이게 Dacorator다. 원래 함수는 보존하되, 기능을 확장시켜주는 것.
#이것 역시도 Closure가 func를 저장하고 있기 때문에 my_func를 실행한 값을 리턴할 수 있다.



#실제로는 이렇게 사용한다.
def my_outer_func(func) :

    def my_inner_func() :
        print('{} 함수 수행 시간을 계산합니다.' .format(func.__name__))
        start = time.time()
        func()
        end = time.time()
        print('함수 수행 시간은 {}입니다.' .format(end - start))

    return my_inner_func

@my_outer_func    #my_func를 my_outer_func의 인자로 전달해서 사용해라.  이게 Decorator
def my_func() :
    print('my_func() 함수가 호출되었습니다.')

my_func()   #그럼 그냥 이렇게만 실행한다.
#이게 Dacorator의 기본적인 구조다.
#기존 함수의 기능을 확장시킨 것. 건드리지는 않고.






def print_user_name(*args) :
    #args는 튜플로 받는다.
    for name in args :
        print(name)


print_user_name('홍길동', '신사임당')
print_user_name('홍길동', '신사임당', '유관순')


def print_user_name(**kwargs) :
    #kwargs는 딕셔너리로 받는다.
    for key in kwargs.keys() :
        print(kwargs.get(key))


print_user_name(name1='홍길동', name2='신사임당')   #key=value 이게 딕셔너리로 넘어간다.




#Decorator에 대해 한 가지 더 알아보자.

def my_func() :
    print('이것은 소리없는 아우성..')

def my_add(x, y) :
    print('두 수의 합은: {}' .format(x + y))
#이 두 함수의 기능을 확장시켜보고싶다.




def my_outer(func) :

    def my_inner() :
        print('데코레이터 시작')   #원하는 기능1
        func()
        print('데코레이터 끝')    #원하는 기능2

    return my_inner

@my_outer
def my_func() :
    print('이것은 소리없는 아우성..')

@my_outer
def my_add(x, y) :
    print('두 수의 합은: {}' .format(x + y))
#이 두 함수의 기능을 확장시켜보고싶다.

my_func()   #자동으로 my_outer함수에서 실행된다.
#my_add(3, 4)  #my_add위에는 안 붙여주면 그냥 이 함수만 실행.

#my_add(3, 4)    #그런데 my_add위에도 붙여주면 일단 데코레이터를 실행한다.
#하지만, inner함수에서는 인자가 없는 함수를 실행하도록 되어 있어서 오류가 난다.

#그리고 참고로, my_outer를 먼저 만들어줘야 데코레이터가 먹힌다.



def my_outer(func) :

    def my_inner(*args, **kwargs) :   #인자가 있든 없든 모두 수행할 수 있도록 해준다.
        print('데코레이터 시작')
        func(*args, **kwargs)
        print('데코레이터 끝')

    return my_inner

@my_outer
def my_func() :
    print('이것은 소리없는 아우성..')

@my_outer
def my_add(x, y) :
    print('두 수의 합은: {}' .format(x + y))


my_func()
my_add(3, 4)
#그러니까 인자가 있는게 들어올지, 없는 게 들어올지, 모든 경우를 받을 수 있도록.