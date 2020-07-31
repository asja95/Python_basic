#python의 입출력
#console입력을 받으려면 input()을 이용
'''
my_input = input('입력값을 넣으세요:')
print(my_input)
'''

#기본적으로 print() 함수는 한줄을 출력한 후 line feed(줄바꿈)을 수행한다.
# my_input = input('입력값을 넣으세요:')
# print(type(my_input), end=' ')
# print(my_input)



# 1. if문
a = 15
if a % 3 == 0 :
    print('3의 배수 입니다.')
elif a % 5 == 0 :
    print('5의 배수 입니다.')
else :
    print('3의 배수도 5의 배수도 아닙니다.')

if a % 3 == 0 :
    pass


#in을 이용한 구문
my_list = ['서울', '인천', '부산']
if '수원' in my_list :
    pass


# 2. for문
#두 가지 형태로 사용한다.
#for ~ in range() : 반복 횟수를 지정할 경우
#for ~ in list, tuple, etc ... : 가지고 있는 데이터만큼 반복할 경우

my_sum = 0
for tmp in range(1, 101, 1) :
    my_sum += tmp
print('누적값은 {}입니다.' .format(my_sum))

my_list = ['서울', '인천', '부산']
for tmp in my_list :
    print(tmp)

#tuple 관련 예
total = 0
my_data = [(1, 2), (3, 4), (5, 6)]
for (tmp1, tmp2) in my_data :
    total += (tmp1 + tmp2)
print(total)



#list comprehension
#하나의 자료형으로 다른 list를 쉽게 생성하는 방법
myList = [1, 2, 3, 4, 5]

goal = []
for tmp in myList :
    goal.append(tmp*2)
print(goal)

goal = [2*tmp for tmp in myList]
print(goal)

myList = [1, 2, 3, 4, 5]
goal = [tmp for tmp in myList if tmp % 2 == 0]
print(goal)


#while문

idx = 0
while idx < 10 :
    print('현재 idx의 값은 {}입니다.' .format(idx))
    idx += 1


