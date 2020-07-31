#python에서 module은 함순사 변수 또는 클래스를 모아놓은 파일을 지칭한다.
#다른 python파일에서 불러와서 사용할 수 있다.

#module을 사용하는 이유는 코드의 재사용성과 관리 목적

#python모듈은 크게 2가지가 있다.
#1. C언어로 구성된 binary module
#2. python언어로 구현된 일반 module

#module을 사용하기 위해 사용되는 키워드는 "import"
#결국 module도 파이썬 입장에서는 객체로 관리된다.


import sys
print(sys.path)
#특정 위치에 모듈이 있어야 사용할 수 있다. 아무데나 있어서는 쓸 수 없다.
#그래서 이 위치에 있으면 된다.
#sys.path.append("내가 모듈을 저장하는 폴더의 위치") 이렇게 해줄 수 있겠다.
sys.path.append('C:/python_data')
print(sys.path)  #추가 되었다.



#이제 module을 만들어보자.
#python file을 생성하면 된다. C:/python_data 위치에 파일을 만들어서 사용한다.

import module1
print(module1.my_pi)           #모듈에 있는 변수
print(module1.my_adder(3, 4))  #모듈에 있는 함수

import module1 as m1
print(m1.my_pi)
print(m1.my_adder(3, 4))




from module1 import my_adder    #모듈로부터 함수를 import 했다.
print(my_adder(30, 40))


from module1 import *
print(my_pi)



#C:/python_data 안에 module1.py를 저장해 놨다.
#패키지는 모듈을 담아놓은 것. 폴더의 중접구조가 된다.
#C:/python_data/test_module/module1.py 로 다시 저장해본다.

import test_module.module1
print(test_module.module1.my_pi)

import test_module.module1 as m1
print(m1.my_pi)


#참고로, sys에 append하는 방법은 일시적인 거라, 고정적으로 sys.path에 C:/python_data가 추가되어있지 않다.









###############################################

#exceptino(예외)
#Error - compile time error : 문법오류
#      - runtime error : 실행시 발생하는 오류

#어떤 runtime error들은 비정상 종료되지 않고 프로그램을 지속적으로 수행시킬 수 있는 방법이 있다.
#exception 처리는 하나의 구문밖에 없다.
#try
#except
#else
#finally


def my_func(my_list) :
    total_sum = 0   #리스트 안의 숫자들을 누적한다.
    try :
        total_sum = my_list[0] + my_list[1] + my_list[2]
        print('try가 수행되었습니다.')
    except Exception :    #오류가 있으면 여기로 온다. Exception은 발생가능한 모든 오류를 지칭한다.
        print('오류가 존재합니다.')    #여기서 예외처리를 해야한다.
    else :  #오류가 없으면 여기로 온다.
        print('오류가 없어요.')
    finally :  #오류가 있든 없든 무조건 수행하는 부분
        print('무조건 수행돼요!!')


my_func([1, 2, 3])    #try, else, finally가 수행된다.
my_func([1, 2])       #except, finally가 수행된다.