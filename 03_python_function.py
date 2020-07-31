#python의 함수
#크게 2가지 분류가 있다.
# 1. 내장함수
# 2. 사용자 정의 함수 (user define function)
#함수이름을 만들 때는 관용적으로 소문자와 언더스코어로 이름을 짓는다.
#함수 만들 때는 위에 최소 두 줄 이상 비우는 것이 좋다.


def my_sum(a, b, c) :
    return a + b + c

result = my_sum(10, 20, 30)
print(result)


#함수를 호출하는데 인자가 가변적인경우

def my_sum(*args) :
    tmp = 0
    for k in args :
        tmp += k
    return tmp

result = my_sum(10, 20, 30, 40, 55, 67)
print(result)


#python은 결과값이 두 개 이상일 수 있다.

def my_operator(a, b) :
    result1 = a + b
    result2 = a * b
    return result1, result2
#여기서 return의 모양의 의미가 튜플은 괄호를 생략할 수 있다는 특징. 그래서 튜플로 반환할 수 있는 것.

result = my_operator(4, 5)
print(result)

result1, result2 = my_operator(4, 5)   #이것 역시 튜플인 것.
print(result1, result2)



#python의 함수는 default parameter를 사용할 수 있다.
#단, 마지막에서만 지정 가능하다.
def my_default(a, b, c=True) :
    data = a + b
    if data > 10 and c :
        return data
    else :
        return 0
result1 = my_default(10, 20,  False)
result2 = my_default(10, 20)    #실인자
print(result1)
print(result2)



#python의 함수의 인자는 mutable, immutable 둘 중에 하나다.
#call-by-value & call-by-reference X
#python에서 함수에 인자를 전달하고 함수는 전달된 인자를 받는다.
#어떤 경우는 실인자의 데이터가 변하는 경우가 있고,
#어떤 경우는 실인자의 데이터가 변하지 않는 경우가 있다.

def my_func(tmp_number, tmp_list) :
    tmp_number = tmp_number + 100
    tmp_list.append(100)

data_x = 10
data_list = [10]

my_func(data_x, data_list)

print(data_x)      #변화가 없고   immutable
print(data_list)   #변화가 있다   mutable

#immutable에는 대표적으로 숫자, 문자열, tuple 등   -> 값을 넘기는 경우. call-by-value.
#mutable에는 대표적으로 lsit, dictionary 등  -> 주소를 넘기는 경우. call-by-reference.
#이게 전역변수, 지역변수와는 조금 다른 개념이다.






#내장함수

#함수  id()
#숫자인 경우 0~256까지는 너무나 많이 사용하는 객체(값)에 대해서는 예외적으로 같은 주소값을 가진다.
a = 100
b = 100
print(id(a))
print(id(b))


#lambda expression (람다표현식)
#힘수와는 다르지만 함수의 역할을 한다.
#한 줄로 함수를 정의 하는 방법
#함수의 이름이 없다.
#이름이 없기 때문에 변수에 저장, 함수의 인자로 사용.
#함수의 결과값으로 함수를 리턴.
# -> first class function.

my_lambda = lambda x1, x2, x3 : x1 + x2 + x3
print(my_lambda(1, 2, 3))