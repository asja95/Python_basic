#Maginc function

# 1. method의 이름 앞뒤에 더블 언더스코어(__)가 붙는 method.
# 가장 대표적인 magic function은, __init__(생성자) 등등.
# 2. 클래스 안에 정의할 수 있는 특수한 형태의 method
# 3. 특수한 상황에서 그에 맞는 magic function이 호출된다.

class Student(object):

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        print('{} {} 학생이 생성되었습니다.' .format(self.dept, self.name))

    def __del__(self):
        print('소멸자가 호출되었어요!!')    #만들어진 리소스를 제거하는 역할.

stu1 = Student('홍길동', '심리학과')

del stu1   #객체를 메모리에서 삭제한다. __del__가 호출되는 것.




####################


a = 100
print(type(a))    #'int'라는 클래스가 존재한다는 걸 알 수 있다.

class MyInt(int):
    pass

my_num = MyInt(100)   #이런 식으로 정수를 만드는 것도 가능하다.
print(my_num + 200)
print(my_num.__add__(200))
# + 연산자 자체가 __add__를 호출하도록 되어있다.
#그런데 리스트에다 +하면 리스트끼리 잇는다. 즉, __add__안에서 그렇게 명시되어있다.
#숫자에 대한 작업, 리스트에 대한 작업들이 구분되어 정의되어 있는 것.





###################################

class Student(object):

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        print('{} {} 학생이 생성되었습니다.' .format(self.dept, self.name))


stu1 = Student('홍길동', '심리학과')
print(stu1)
#instance의 class정보와 저장되어 있는 메모리 주소가 출력된다.

class Student(object):

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        print('{} {} 학생이 생성되었습니다.' .format(self.dept, self.name))

    def __repr__(self):
        return self.name


stu1 = Student('홍길동', '심리학과')
print(stu1)
#onverriding해서 다른 걸 출력하도록 했다.



class Car(object):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __lt__(self, other):     #car1이 self, car2가 other로.
        if self.price < other.price :
            return '{} 가격이 더 낫습니다.' .format(self.model)
        else :
            return '{} 가격이 더 높습니다.' .format(other.model)

car1 = Car('G70', 5000)
car2 = Car('Sonata', 3000)

print(car1 < car2)  #원래 이건 오류다. 그런데 __lt__를 통해 연산자를 오버라이딩할 수 있다.
#그러면 연산자를 호출할 때 오버라이딩 된 method를 호출한다.