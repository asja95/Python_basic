#1990년도 이전에는,
#가장 대표적인 프로그램 작성 방식으로 구조적 프로그래밍(절차적 프로그래밍)
#프로그램 작성시 기능으로 세분화해서 각각의 기능을 모듈로 제작해서 프로그램을 작성.
#은행업무를 대분류에서 소분류로 차례대로 나눠보자면,
#은행업무 - 예금 - 입금 - 무통장입금 - ... 등등으로 각각의 기능으로 세분화할 수 있다.
#그러다가 더 이상 세분화할 수 없는 단계가 되면 그걸 모듈(함수)로 만든다.
#장점: 기능별로 나누기 때문에 설계하기가 편하다. (누가 봐도 기능은 동일하니까.) -> 빨리 처리할 수 있다.
#단점: 같은 기능을 사용하는 다른 부문에도 영향을 미칠 수 있기 때문에 유지/보수가 어렵다.
#     (예를 들어, 자행입금 기능은 예금 - 입금 의 하위분류에서 사용하는 기능이지만, 펀드 부문에서도 사용할 수 있다.
#      그런데 입금 기능을 위해 자행입금 기능을 수정했는데, 이게 펀드에도 영향을 미치게 된다. 그래서 수정이 힘들다.)
#그래서 이런 단점때문에 점점 인터넷 같은 것들이 규모가 커지니까 바꾸자 했음. 그래서 만들기는 힘들어도 시스템을 있는 그대로
#만들자고 한 것.
#현실세계의 해결해야 하는 문제에 대한 구성요소를 먼저 파악한다.
#은행 -> 은행지점, 고객, 텔러, ATM, 계좌, ...   ------->>>> "개체(object)"
#사람마다 바라보는 방식은 다를 수 있다. 그런데 수정하는 건 쉬워진다. 유지/보수가 쉬워짐.
# Object Oriented Programming (OOP)
# 개체들을 파악해서 그 개체들간의 관계를 프로그래밍 하는 방식을 -->> 객체지향 프로그래밍 이라고 한다.
#개체들을 파악하고, 이 각각의 객체를 프로그램적으로 표현하게 된다. -> '객체 모델링'
# 예) 사람을 프로그램적으로 묘사해보면,
#     그런데 사실 사람을 구성하는 요소를 생각해보면, 완벽하게 다 반영해서 만들어낼 수 없다. (키, 몸무게, 재산 등등)
#     그래서 단순하게 필요한 부분만 묘사하도록 한다. -> '추상화(Abstraction)'
#이런 개체들은 속성 + 행위 로 존재하더라.
#그러면 속성은 변수로, 행위는 함수로 표현하자.
#(변수=property, member field, field / 함수=method(그러니까 이 개체에 종속된 기능))
#class라는 걸 이용해서 추상화과정을 거친 개체를 프로그램적으로 표현하게 된다.

#class -> 1.객체모델링의 수단
#class 사람
#      키 (변수) height -> float
#      몸무게 (변수) weight -> float
#      나이 (변수) age -> int
#      걷는다 (메소드)
#      말한다 (메소드)
#      잔다 (메소드)
#class는 data type의 관점에서 봤을 때는 기존 데이터타입을 이용해서 새로운 데이터타입을 만드는 것이라고 볼 수 있다.
#그래서 class를 추상적인 데이터타입이라고 부른다. (Abstract data type = ADT)
#예를 들어, 빌트인 데이터타입하고 다른 것.



'''
구조적 프로그래밍(절차적 프로그래밍)
프로그램 작성 시 기능으로 세분화해서 각각의 기능을 모듈화(함수화)해서 구현
프로그램 구조를 이해하기 쉽고 프로그램을 빠르게 만들 수 있다
프로그램 규모가 커지면 유지보수와 코드 재사용에 한계가 있다

객체지향 프로그래밍
현실세계의 해결해야 하는 문제를 그대로 프로그램으로 묘사(표현)
프로그램을 구성하는 주체들(개체, 객체, object)를 파악하고
그 객체들간의 데이터 흐름에 초점을 맞추어서 프로그램을 작성
프로그램을 설계하고 작성이 상대적으로 어렵다
일단 제대로 작성된 객체지향 프로그램은 유지보수와 재사용에 상당한 이점이 있다
'''

# 학생의 이름, 학과, 학번, 평균평점을 저장하는 방법
stu_name = '홍길동'
stu_dept = '심리학과'
stu_num = '20201134'
#기본적으로 숫자형으로 잡는 경우는 연산을 한다는 게 내포. 학번의 구성은 숫자지만 그럴 필요가 없으니까 처리가 더 편한 문자열로.
stu_grade = 3.5

#만약 3명의 학생이 있으면 어떻게 할까?
stu1_name = '홍길동'
stu1_dept = '심리학과'
stu1_num = '20201134'
stu1_grade = 3.5

stu2_name = '김길동'
stu2_dept = '통계학과'
stu2_num = '20202334'
stu2_grade = 3.8

#그런데 이렇게 하면, 코드가 너무 불필요하게 반복적이고 확장성이 없다.
stu_name = ['홍길동', '김길동', '신사임당']
stu_dept = ['심리학과', '컴퓨터', '경영학과']
stu_num = ['20201134', '20201135', '20201138']
stu_grade = [3.5, 2.0, 4.0]
#그리고 여기서는 같은 위치에 있는 데이터는 한 사람을 나타낸다는 게 내 마음에는 있다.
#그런데 index를 이용해 처리하는게 쉬운 작업은 아니고, 코드에 모든 의미가 다 내포되어 있는게 아닌 문제가 발생한다.

#그럼 이런 내용을 class를 이용해서 객체지향적으로 표현할 수 있는가.
class Student(object) :    #여기서의 괄호는 '상속'의 의미.
    def __init__(self, name, dept, num, grade) :   #모든 class가 필수적으로 가지고 있는 메소드.
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade

#클래스를 기반으로 메모리 공간이 만들어지고, 그 메모리 공간에 데이터가 저장된다.
#그 메모리 공간이 'instance'라고 하고, 그 instance의 정보를 가지고 있는 게 클래스다.
#instance: 프로그램적으로 만든 객체(object)라고 본다. 그냥 통상적으로 객체라고도 한다.
#그러니까, 클래스 자체에 저장되는 것이 아니다.
#그래서 __init__가 instance를 만들면서 그 공간을 초기화하는 역할을 한다.
#객체가 만들어지는 순간 자동으로 호출된다.
#초기화한다는 게, 새롭게 만든 메모리 공간에 데이터를 넣어서 만드는 것. 그래서 일반적으로 입력이 있는 것이 좋다.
#그리고 self는 만든 객체의 reference를 나타낸다. 그래서 self가 있어야 이게 어떤 객체를 가르키는지 알 수 있다.
#그러니까 self는 그 메모리 공간을 가르키는 것.
#그러면 self에다가 dot operator를 해주면, (self.~~) instance에 변수 공간을 만들고 거기에 데이터를 저장한다.

stu1 = Student('홍길동', '심리학과', '20201134', 3.5)  #self는 본래 존재하는 거고.
#이걸 여러명이 필요하다면,
students = []
students.append(Student('홍길동', '심리학과', '20201134', 3.5))
students.append(Student('김길동', '컴퓨터', '20201135', 2.0))
students.append(Student('신사임당', '경영학과', '20201138', 4.0))
#이렇게 되면 students라는 리스트에는 Student 클래스가 가지는 id를 정보로 가지고 있는 것.
print(students[0].dept)





# 그래서 Python은 객체지향 언어다!
#python에서 나오는 모든 것은 다 객체(instance)다!
a = 10
print(type(a))
#여기서 출력결과에 class가 있다는 것 자체가 파이썬이 class를 만들고 instance를 만들었다는 것. 그래서 다 객체다.

#숫자도, 리스트도, 문자열도, 함수도 모두 객체다!!
#객체가 있다는 건, class가 존재한다는 것 -> 변수, method
my_list = [10, 20]
my_list.append(30)   #my_list라는 객체가 가지고 있는 append라는 method

#객체(instance)란, 속성과 같은 여러가지 데이터+메소드를 가지고 있는 데이터 구조를 지칭한다.



class Student(object) :    #여기서의 괄호는 '상속'의 의미.
    def __init__(self, name, dept, num, grade) :   #생성자(constructor), initializer
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade

    def __repr__(self) :   #클래스를 호출하면 이 값을 리턴하도록 한다. 원래는 메모리 주소값이 나올건데 그걸 재정의한 것.
        return self.name

student = Student('홍길동', '심리학과', '20201134', 4.5)
print(student)  #Student라는 클래스의 object이고 id는 ~~다.   (repr를 정의하지 않았을 때.)
                #repr를 정의하고 나면 홍길동이 출력된다.]


print(student.dept)
student.dept = '경영학과'
print(student.dept)
#student의 주소를 따라가서 수정하는 거니까. 그런데 instance의 데이터를 이런식으로 direct로 수정하는 건 좋지 않다.
#대신 instance가 가지고 있는 method를 이용해서 접근하는 게 좋겠다.
# -->> information hiding = 정보은닉
#데이터의 오염을 방지하는 것. 예를 들어, 우리 학교에는 임상병리학과가 없는데, 이런 식으로 특정 학생의 과를 임상병리학과로 고치면,
#코드는 문제가 없지만, logical하게 오류다. 그래서 이런 걸 방지하기 위해 method를 거쳐서 하도록.

class Student(object) :    #여기서의 괄호는 '상속'의 의미.
    def __init__(self, name, dept, num, grade) :   #생성자(constructor), initializer
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade

    def __repr__(self) :   #클래스를 호출하면 이 값을 리턴하도록 한다. 원래는 메모리 주소값이 나올건데 그걸 재정의한 것.
        return self.name

    def change_dept(self, tmp_dept) :
        # tmp_dept가 정상적인 학과인지 체크하는 코드가 들어갈 라인.
        # 여기서 정상적인 학과가 아니라면 바꾸지 않고, 정상적이라면 바꾼다.
        self.dept = tmp_dept

student = Student('홍길동', '심리학과', '20201134', 4.5)
student.change_dept('임상병리학과')
print(student.dept)   #사실 이것도 이렇게 직접 가져오기보다는 method를 통해서 가져오는 것이 낫다.




################################

#python이 제공하는 내장함수 중 dir()에 대해 알아보자.
#객체가 인자로 들어오면 해당 객체의 모든 속성과 메소드를 알려준다.
print(dir(student))
student.depts = '철학과'
#depts는 원래 student에 없는 속성이니까 다른 자바나 C에서는 에러다.
#하지만 파이썬에서는 없는 걸 추가하는구나~ 하고 새로 만들어준다.
print(dir(student))   #depts가 추가되었다.

#python의 함수도 객체다
def my_func(a, b) :
    return a + b

print(dir(my_func))

my_func.myName = '홍길동'
print(dir(my_func))
#python의 모든 게 객체다.









class Student(object) :

    scholarship_rate = 3.0  #class variable 이라고 한다. class가 가지고 있는 variable이다.

    def __init__(self, name, dept, num, grade) :
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade

    def is_scholarship(self) :
        if self.grade > Student.scholarship_rate :
            return True
        else :
            return  False

student = Student('홍길동', '심리학과', '20201134', 4.5)

#class variable은 하나의 class로 만들어진 모든 instance가 공유하는 값이다.
#class를 100개 만들면 name 등응 각 instance에서 하나씩 존재해서 100개가 있겠지만,
#scholarship_rate는 한 개만 존재한다.
#self.grade: 이 학생(self)의 학점이
#Student.scholarship_rate: class가 가지고 있는 변수보다
#크면 장학금 대상이다.


####################################################################################################
class Student(object) :

    scholarship_rate = 3.0  #class variable 이라고 한다. class가 가지고 있는 variable이다.

    def __init__(self, name, dept, num, grade) :
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade

    def is_scholarship(self) :
        if self.grade > Student.scholarship_rate :
            return True
        else :
            return  False

student = Student('홍길동', '심리학과', '20201134', 4.5)

# namespace(네임스페이스)
#객체가 가지는 데이터를 나누어서 관리하는 공간
# 1. instance namespace
# 2. class namespace
# 3. superclass namespace
# instance namespace < class namespace < superclass namespace (포함관계)
#제일 처음에 instance에서 찾고, 거기에 없으면 class에서 찾고, 거기에도 없으면 supercalss에서 찾고, 없으면 없는거다.
#예를 들어, scholarship_rate는 class namespace에 있고, self.~~는 instance namespace에 있다.
#그래서 self.scholarship_rate라고 쓰면 문법적으로는 잘못됐지만, 속성을 찾아오는 데는 문제가 없다.

#파이썬은 동적으로 속성이나 method를 추가할 수 있다.
student.scholarship_rate = 4.5
#이렇게 하면 우리 생각으로는 class variable이 2.0에서 4.5로 바뀔 거라고 생각하지만,
#student는 instance이기 때문에 instance의 공간에 새로 추가된다.
#그러면 class와 instance namspace에 변수명이 동일한 변수가 동시에 존재하는 것.
#그래서 class variable을 사용할 때는 명확하게 self가 아닌 클래스명을 붙여주는 게 좋다.
#그러면 밖에서 class variable을 수정하고 싶으면, 클래스명.variable = ~~로 해주면 된다.
#어차피 모든 클래스가 공유하는 변수니까.
#class 내에서 class variable을 생성하고, 그걸 다시 class내에서 사용할 때는 반드시 어디서 찾으라는 표시가 있어야 한다.
#그냥 변수명만 사용해서 사용할 수 없다. ex) Student.scholarship_rate




#instance method

#instance method(self 인자를 가지고 있는 method)는 하나의 인스턴스에 한정된 데이터를 생성, 변경, 참조하기 위해 사용된다.
#class method는 class를 인자로 받아서 class variable을 생성, 변경, 참조하기 위해서 사용

class Student(object) :

    scholarship_rate = 3.0

    def __init__(self, name, dept, num, grade) :
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade

    @classmethod   #class method decorator: 아 얘가 class를 인자로 받겠구나 알려주는.
    def change_scholarship(cls, rate) :   #class를 인자로 받겠다. instance('self')가 아니라.
        cls.scholarship_rate = rate

    def is_scholarship(self) :
        if self.grade > Student.scholarship_rate :
            return True
        else :
            return  False

student = Student('홍길동', '심리학과', '20201134', 4.5)

#그래서 student.chage_scholarship()하면 문법적으로는 좋지 않다.
#이거는 instance method가 아니라 class method니까. Student.chage_scholarship() 이 좋다.



#static method
#class 안에서 정의된 일반 함수.
#class도, instance도 인자로 받지 않는다.

class Student(object):
    scholarship_rate = 3.0

    def __init__(self, name, dept, num, grade):
        self.name = name
        self.dept = dept
        self.num = num
        self.grade = grade

    @classmethod
    def change_scholarship(cls, rate):
        cls.scholarship_rate = rate

    @staticmethod
    def is_valid_scolarship(rate) :
        if rate < 0 :
            print('장학금 기준 학점은 음수가 될 수 없습니다.')


    def is_scholarship(self):
        if self.grade > Student.scholarship_rate:
            return True
        else:
            return False


student = Student('홍길동', '심리학과', '20201134', 4.5)
Student.is_valid_scolarship(-2.4)
#사용할 때는 class에다가 붙여서 사용한다.


'''
지금까지 class안에 들어간 것들: class variable, instance variable, class method, instance method,
                            initializer, magic function, static method, decorator
'''






#information hiding (정보 은닉)
#instance가 가지는 속성은 매우 매우 중요한 데이터이기 때문에 외부에서 직접적으로 access하는 건 좋지 않다.
#그러면 어떻게 적접적으로 access하는 걸 막을 수 있는가.
#Java -> access modifier(접근제어자)
#        public vs private
#student.dept = '컴퓨터'라고 하면 이게 public하게 접근하는 것.
#그러면 어떻게 하면 private으로 지정할 수 있을까.
class Student(object):

    def __init__(self, name, dept, num, grade):
        self.name = name
        self.__dept = dept  #private처리: __를 붙인다.
        self.num = num
        self.grade = grade


student = Student('홍길동', '심리학과', '20201134', 4.5)

#print(student.__dept)   #이렇게 하면 에러 뜬다. access가 안 된다.
#private으로 처리된 속성이 있으면 외부에서 직접적인 access가 안 되기 때문에 method를 사용하도록 처리.
#private으로 되어 있는 속성의 값을 알아오는 용도의 method가 필요하고,
#그 method를 'getter' 라고 한다.
# getter: 이름 짓는 방법이 정해져 있다. 규칙!!  예) def getDept  (앞에 get을 쓰고 속성은 첫자를 대문자로)
class Student(object):

    def __init__(self, name, dept, num, grade):
        self.name = name
        self.__dept = dept  #private처리
        self.num = num
        self.grade = grade

    def getDept(self) :   #getter
        return self.__dept


student = Student('홍길동', '심리학과', '20201134', 4.5)
print(student.getDept())   #이제 이렇게 하면 access가 된다.

#setter: 값을 설정해주는 method.
class Student(object):

    def __init__(self, name, dept, num, grade):
        self.name = name
        self.__dept = dept  # private처리
        self.num = num
        self.grade = grade

    def getDept(self):  # getter
        return self.__dept

    def setDept(self, dept) :  #setter
        self.__dept = dept


student = Student('홍길동', '심리학과', '20201134', 4.5)
student.setDept('컴퓨터')
print(student.getDept())
#private해졌으니까 setter로 바꾸고, 불러올 때는 getter로 불러온다.



#method도 private하게 된다.
class Student(object):

    def __init__(self, name, dept, num, grade):
        self.name = name
        self.__dept = dept  # private처리
        self.num = num
        self.grade = grade

    def getDept(self):  # getter
        return slef.__dept

    def setDept(self, dept):  # setter
        self.__dept = dept

    def __print_data(self) :   # private처리
        return self.name


student = Student('홍길동', '심리학과', '20201134', 4.5)



###########################################################################

#객체지향을 하는 이유는, 유지보수 + 재사용성
#이번에는 재사용성에 초점.
#재사용성을 위한 대표적인 객체지향 기법 -> inheritance 상속.
#sub class(사람)는 super class(포유류)다. 역은 성립 x.
#예를 들어, 오버워치의 모든 캐릭터는 공격력을 가지고 있는데, 그 정도가 다르다.
#모든 캐릭터에 공격력, 체력, 방어력 등을 부모 클래스가 부여하고, 자식 클래스는 각 캐릭터에 맞게 변형한다.

#파이썬의 모든 클래스는 object class 다!!  (실제 class object()가 존재한다!!)
#즉, 파이썬의 모든 클래스는 object class를 상속해야 한다.

class Unit(object) :   #()의 의미는 상속을 받는다는 것. object라는 클래스를 상속받겠다.
    pass
#여기서 별다른 작업을 안 해도 object가 가지는 것들을 받아올 것. __init__같은 애들.

class Unit(object) :
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__   #이 instance가 가르키는 class를 찾아가서 이름을 가져온다.
        self.damage = damage
        self.life = life

    def show_status(self):
        print('직업: {}' .format(self.utype))
        print('공격력: {}' .format(self.damage))
        print('생명력: {}' .format(self.life))

class Marine(Unit) :
    pass
#지금 여기에는 생성자도 뭐도 아무것도 없는 상태다.

marine_1 = Marine(100, 500)
#이렇게 Marine class를 호출하면 instance를 만드는데, 실제 Marine class에는 아무것도 없다.
#그러면 class namespace에 없으니까 superclass namespace로 가서 Unit에서 찾는다.
#즉, 상속을 받는다고 해서 코드 자체가 클래스 안으로 들어오는 게 아니다.
#직업 이름이 Marine이 되는 이유는, 마린 클래스에 아무것도 없지만, 클래스는 존재하니까 __class__는 Marine을 가르키게 되는 것.
#그 외의 나머지 속성들은 마린에 없으니까 유닛에서 찾을 것.

marine_1.show_status()

class Unit(object) :
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__   #이 instance가 가르키는 class를 찾아가서 이름을 가져온다.
        self.damage = damage
        self.life = life

    def show_status(self):
        print('직업: {}' .format(self.utype))
        print('공격력: {}' .format(self.damage))
        print('생명력: {}' .format(self.life))

class Marine(Unit) :
    def __init__(self, damage, life, range_upgrade):
        self.utype = self.__class__.__name__
        self.damage = damage
        self.life = life
        self.range_upgrade = range_upgrade

    def show_status(self):
        print('직업: {}' .format(self.utype))
        print('공격력: {}' .format(self.damage))
        print('생명력: {}' .format(self.life))
        print('사거리 업그레이드 유무: {}' .format(self.range_upgrade))

#이렇게 하면 마린 클래스에서 method를 재정의하게 된다. 이걸 오버라이딩이라고 한다.
#그런데 이렇게 하면 상속받는 게 의미가 없다. 상위클래스의 내용을 가져오면 된다.

class Unit(object) :
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__   #이 instance가 가르키는 class를 찾아가서 이름을 가져온다.
        self.damage = damage
        self.life = life

    def show_status(self):
        print('직업: {}' .format(self.utype))
        print('공격력: {}' .format(self.damage))
        print('생명력: {}' .format(self.life))

class Marine(Unit) :
    def __init__(self, damage, life, range_upgrade):
        super(Marine, self).__init__(damage, life)    #Marine 클래스의 상위클래스를 찾아가라.
        self.range_upgrade = range_upgrade    #추가하는 것.

    def show_status(self):
        super(Marine, self).show_status()
        print('사거리 업그레이드 유무: {}' .format(self.range_upgrade))


marine_1 = Marine(100, 100, True)
marine_1.show_status()
#상위클래스에서 받아온 __init__같은 경우, 원래 인자 2개가 필요했으니까 damge랑 life를 넣어준다.









###################################################################################################

#스타크래프트 게임 시나리오
#사용할 유닛들은, Marine, Medic, Vulture, Dropship

class Unit(object):

    def __init__(self, damage, life):
        self.utype = self.__class__.__name__
        self.damage = damage
        self.life = life

    def show_status(self):
        print('직업: {}' .format(self.utype))
        print('공격력: {}' .format(self.damage))
        print('생명력: {}' .format(self.life))

    def attack(self):
        pass    #유닛마다 공격방식이 달라서 그냥 공격이 있어 하고 만들어놓기만 하고, 오버라이딩 할 것.

class Marine(Unit):

    def __init__(self, damage, life, range_upgrade):
        super(Marine, self).__init__(damage, life)
        self.range_upgrade = range_upgrade

    #overriding
    def show_status(self):
        super(Marine, self).show_status()
        print('사거리 업그레이드 유무: {}' .format(self.range_upgrade))

    #overriding
    def attack(self):
        print('마린이 공격합니다. 땅땅!!!')

    def stimpack(self):    #이건 마린만의 독립적인 능력치.
        if self.life < 20 :
            print('체력이 낮아서 수행이 불가능합니다.')
        else :
            self.life -= 10
            self.damage *= 1.5
            print('마린이 스팀팩을 사용했어요!!!')

class Medic(Unit):

    #overriding
    def attack(self):
        print('메딕이 치료합니다. 힐힐!!!')


class Vulture(Unit):

    def __init__(self, damage, life, amount_of_mine):
        super(Vulture, self).__init__(damage, life)
        self.amount_of_mine = amount_of_mine

    #overriding
    def attack(self):
        print('벌처가 공격합니다. 뚜뚜!!!')

class Dropship(Unit):

    #overriding
    def attack(self):
        print('특정 목표지점으로 이동합니다. 슈웅~!!')

    def board(self, unit_list):    #여러 유닛들을 태운다.
        self.unit_list = unit_list
        print('유닛들을 태웠습니다.')

    def drop(self):    #태운 유닛들을 내린다.
        print('모든 unit이 드랍십에서 내립니다.')
        return self.unit_list

#marine을 생성합니다. 3마리.
marine_1 = Marine(100, 100, False)
marine_2 = Marine(100, 100, False)
marine_3 = Marine(100, 100, False)

#medic을 생성합니다. 1마리.
medic = Medic(0, 100)

#vulture를 생성합니다. 2마리.
vulture_1 = Vulture(200, 100, 3)
vulture_2 = Vulture(200, 100, 3)

#list를 이용해서 여러 개의 객체를 저장한다.
troop = list()
troop.append(marine_1)
troop.append(marine_2)
troop.append(marine_3)
troop.append(medic)
troop.append(vulture_1)
troop.append(vulture_2)

#dropship을 생성한다.
dropship = Dropship(0, 100)

#dropship에 유닛들을 태운다.
dropship.board(troop)

#공격지점으로 이동한다.
dropship.attack()

#공격지점에서 유닛들을 내린다.
my_list = dropship.drop()

#스팀팩을 쓰고 공격하기
for unit in my_list :
    if isinstance(unit, Marine) :
        unit.stimpack()
    unit.attack()








#####################################################################################

file1 = open('C:/python_data/student_score.txt', 'r')
while True :
    line = file1.readline()   #한 줄을 읽으니까 실제로는 마지막에 개행문자까지 읽게 되서 한 줄씩 공백이 생긴다.
    if not line :
        break
    print(line)

file1.close()

file1 = open('C:/python_data/student_score.txt', 'r')
scores = []
while True :
    line = file1.readline().rstrip()
    if not line :
        break
    scores.append(line)
file1.close()
print(scores)

scores.sort(key = lambda x : -(int(x.split(',')[1]) + int(x.split(',')[2]) + int(x.split(',')[3]))/3)
for n, line in enumerate(scores) :
    print('%d등: ' %(n+1), line.split(',')[0],
          round((int(line.split(',')[1]) + int(line.split(',')[2]) + int(line.split(',')[3]))/3, 1))


#####################################################################################
class Student(object) :

    def __init__(self, name, kor, eng, math):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__math = math
        self.avg = round((kor + eng + math) / 3, 1)


    def __repr__(self):
        return '{} {}' .format(self.__name, self.avg)

students = list()
file = open('C:/python_data/student_score.txt', 'r')
while True :
    line = file.readline().rstrip()
    if not line :
        break
    stu_data = line.split(',')
    students.append(Student(stu_data[0], int(stu_data[1]), int(stu_data[2]), int(stu_data[3])))
file.close()

students.sort(key = lambda x : -x.avg)
#result = sorted(students, key = lambda x : -x.avg)
#result = reversed(sorted(students, key = lambda x : x.avg))

for n, stu_class in enumerate(students) :
    print('{}등' .format(n+1), stu_class)  