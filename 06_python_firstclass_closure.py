#first-class
#first-class citizen(1급 시민)
#프로그램의 구성요소(개체)가 다음의 조건을 만족하면 first-class citizen이라고 부른다.
#1. 구성요소가 변수나 데이터 구조의 속성으로 저장될 수 있다.
#2. 함수의 인자로 전달될 수 있다.
#3. 함수의 결과로 리턴될 수 있다.

#아주 쉽게 생각하면, 우리가 사용하는 일반 숫자 타입의 데이터 같은

#우리가 사용하는 객체(class로부터 파생된 instance)

#python의 함수는 어떻게 될까?
#만약 1급 시민의 조건을 만족한다면 일급 함수(first class function)라고 부른다.
# "결국 함수를 일급 시민으로서 사용할 수 있느냐"
# -->> 함수를 runtime으로 생성할 수 있다!!





# 1. 함수를 변수에 저장할 수 있다.

def my_add(x, y) :
    return x + y

print(my_add)   #이 함수도 메모리 주소를 가지고 있다는 것. 실제 실행 내용은 그 주소에 있다.
f = my_add  #결국 f도 같은 메모리 주소를 가지도록 하는 것.
print(f)
print(f(100, 200))   #같은 주소를 따라갈테니까 당연히 실행된다.

#즉, 함수도 마찬가지로, 그 내용 자체를 가지고 있는 것이 아니라, 주소를 가르키는 것. 변수에 함수를 저장할 수 있다는 것.




#2. 함수를 다른 함수의 인자로 전달할 수 있다.

def my_operation(arg_list) :
    result = []

    for (tmp1, tmp2) in arg_list :
        result.append(tmp1 + tmp2)

    return result

data = [(1, 2), (3, 4), (5, 6)]
print(my_operation(data))


#그런데, 어떨 때는 이 함수에서 빼기 연산을 하고 싶을 수 있다. 그래서 수정해버리면,
#다른 곳에서도 모두 영향을 받게 된다.
#그래서 연산에 대한 것도 따로 인자로 받을 수 있도록 하면 되지 않겠느냐.

def my_add(x, y) :
    return x + y

def my_sub(x, y) :
    return x - y

def my_operation(func, arg_list) :
    result = []

    for (tmp1, tmp2) in arg_list :
        result.append(func(tmp1, tmp2))    #여기서 함수 자체를 넘겨주면 된다.

    return result

data = [(1, 2), (3, 4), (5, 6)]
print(my_operation(my_add, data))
print(my_operation(my_sub, data))



#3. 함수를 다른 함수의 리턴값으로 사용할 수 있다.
# -->> "Closure" 도 같이 이해해야 한다.

def addMaker():

    def my_add_maker():
        return 100

    return my_add_maker   #이 함수를 리턴하는 거니깐, 실행 코드 자체를 리턴하는 것!!
                          #my_add_maker()라고 하면 실행결과가 리턴되는 것!!

addMaker()   #여기까지 하면 my_add_maker를 리턴할 것. 딱 그 함수만 호출하고 끝.
addMaker()()   #이렇게 하면 my_add_maker를 실행하는 것까지 한다.
print(addMaker()())



tmp1 = 100

def my_func() :
    tmp2 = 200

    return tmp2

print(tmp1)
my_func()   #여기서 tmp2를 리턴하자마자 tmp2는 메모리에서 날아간다.
#print(tmp2)    #지역변수니까 이미 소멸된 변수다.


def my_func(x) :
    tmp2 = 300    #매개변수도 지역변수다.
    return x

print(tmp1)
my_func(1000)
#print(x)  역시 에러.


#일단 함수가 호출되면 지역변수가 생성되고, 작업을 하다가 return을 만나면 모두 소멸된다.

def addMaker(x) : #x는 지역변수로, 함수가 호출되면 생성되고 함수가 종료되면 없어진다.

    def my_add_maker(y) :
        return x + y

    return my_add_maker

add_5 = addMaker(5)
add_10 = addMaker(10)
print(add_5(100))
print(add_10(100))
#5라는 지역변수는 addMaker안에서 my_add_maker를 만나서 작업을 하다가,
#return을 만나면서 사라지니까 사실은 my_add_maker가 실행되기도 전에 사라지니까 말이 안 되는 함수다.
#그런데 closure가 저장하고 있어서 x라는 값이 기억된다.
#결국 위의 add_5라는 함수는 어떤 값에든 5를 더할 수 있게 된다. 이런 게 동적인 코딩이다.







##########################################################################################

#Closure
#first class function(일급함수)의 개념을 이용하여
#스코프에 묶인 변수를 바인딩 하기 위한 기술을 의미한다.
#closure는 데이터를 저장한 레코드다. 스코프 안의 변수가 소멸되어도 그에 대한 접근을 closure를 통해서 할 수 있다.
#closure의 도움을 받아 런타임시에 내가 필요한 함수를 만들어 낼 수 있다.




###############################################################################################
print('='*70)
print('\n')
###############################################################################################

# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.

#4이하, 5이상인 자동차를 골라내고, 자동차별로 연비의 평균을 구한다.

class Car(object):
    def __init__(self, manufacturer, model, displ, year, cyl, trans, drv, cty, hwy, fl, car_class):
        self.manufacturer = manufacturer
        self.model = model
        self.displ = displ
        self.year = year
        self.cyl = cyl
        self.trans = trans
        self.drv = drv
        self.cty = cty
        self.hwy = hwy
        self.fl = fl
        self.car_class = car_class

    def __repr__(self):
        return '{}-{}' .format(self.manufacturer, self.model)

file = open('C:/Users/i/Desktop/mpg.txt')
cars = []
while True :
    line = file.readline().rstrip()
    if not line :
        break
    c_d = line.split(',')
    cars.append(Car(c_d[0], c_d[1], c_d[2], c_d[3], c_d[4], c_d[5], c_d[6], c_d[7], c_d[8], c_d[9], c_d[10]))
file.close()
cars = cars[1:]

def check_hwy(my_list) :
    result = {}
    for car in my_list :
        if int(car.hwy) <= 4 or int(car.hwy) >= 5 :
            if car.model in result.keys() :
                result[car.model][0] += int(car.hwy)
                result[car.model][1] += 1
            else :
                result[car.model] = [int(car.hwy), 1]

    return  result


ans1 = {}
chk = check_hwy(cars)
for k, v in chk.items() :
    ans1[k] = round(v[0] / v[1], 1)

ans2 = sorted(ans1.items(), key = lambda x : -x[1])

#정답출력
print('<1번 정답>')
for line in ans2 :
    print(line[0])



# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.

def check_man_cty(my_list) :
    result = {}
    for car in my_list :
        if car.manufacturer in ['audi', 'toyota'] and car.manufacturer in result.keys():
            result[car.manufacturer][0] += float(car.cty)
            result[car.manufacturer][1] += 1
        if car.manufacturer in ['audi', 'toyota'] and car.manufacturer not in result.keys() :
            result[car.manufacturer] = [float(car.cty), 1]

    return result

ans = {}
for k, v in check_man_cty(cars).items() :
    ans[k] = round(v[0] / v[1], 1)

#정답출력
print('<2번 정답>')
print(sorted(ans.items())[1][0])




# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.

def check_man_hwy(my_list) :
    result = {}
    for car in my_list :
        if car.manufacturer in ['chevrolet', 'ford', 'honda'] and car.manufacturer in result.keys():
            result[car.manufacturer][0] += float(car.hwy)
            result[car.manufacturer][1] += 1
        if car.manufacturer in ['chevrolet', 'ford', 'honda'] and car.manufacturer not in result.keys() :
            result[car.manufacturer] = [float(car.cty), 1]

    return result

ans = {}
for k, v in check_man_hwy(cars).items() :
    ans[k] = round(v[0] / v[1], 1)


#정답출력
print('<3번 정답>')
for k, v in ans.items() :
    print(k, ':', v)


# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.

def check_audi(my_list) :
    result = {}
    for car in my_list :
        if car.manufacturer == 'audi' :
            name = '{} {} {} {} {}' .format(car.model, car.displ, car.year, car.cyl, car.trans)
            if name in result.keys() :
                result[name][0] += float(car.hwy)
                result[name][1] += 1
            else :
                result[name] = [float(car.hwy), 1]

    return  result

ans1 = check_audi(cars)
ans2 = sorted(ans1.items(), key = lambda x : -(x[1][0] / x[1][1]))
print('<4번 정답>')
for line in ans2[:5] :
    print(line[0])





# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로(hwy)와 도시(cty))의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.

def check_suv(my_list) :
    result = {}
    for car in my_list :
        if car.car_class == 'suv' :
            if car.manufacturer in result.keys() :
                result[car.manufacturer][0] += (float(car.hwy) + float(car.cty)) / 2
                result[car.manufacturer][1] += 1
            else :
                result[car.manufacturer] = [(float(car.hwy) + float(car.cty)) / 2, 1]

    for k, v in result.items() :
        result[k] = round(v[0] / v[1], 1)

    return result

ans1 = check_suv(cars)
ans2 = sorted(ans1.items(), key = lambda x : -x[1])

#정답출력
print('<5번 정답>')
for line in ans2[:5] :
    print(line[0])






# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.

def check_var_cty(my_list) :
    result = {}
    for car in my_list :
        if car.car_class in result.keys() :
            result[car.car_class][0] += float(car.cty)
            result[car.car_class][1] += 1
        else :
            result[car.car_class] = [float(car.cty), 1]

    for k, v in result.items() :
        result[k] = round(v[0] / v[1])

    return result

ans = list(reversed(sorted(check_var_cty(cars).items(), key = lambda x : x[1])))

#정답출력
print('<6번 정답>')
for line in ans :
    print(line[0])




# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.

def check_man_hwy(my_list) :
    result = {}
    for car in my_list :
        if car.manufacturer in result.keys() :
            result[car.manufacturer][0] += float(car.hwy)
            result[car.manufacturer][1] += 1
        else :
            result[car.manufacturer] = [float(car.hwy), 1]

    for k, v in result.items() :
        result[k] = round(v[0] / v[1], 1)

    return result

ans1 = check_man_hwy(cars)
ans2 = list(reversed(sorted(ans1.items(), key = lambda x : x[1])))


#정답출력
print('<7번 정답>')
for line in ans2[:3] :
    print(line[0])





# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.

def count_campact(my_list) :
    result = {}
    for car in my_list :
        if car.car_class == 'compact' and car.manufacturer in result.keys() :
            result[car.manufacturer] += 1
        elif car.car_class == 'compact' and car.manufacturer not in result.keys() :
            result[car.manufacturer] = 1

    return result

ans = count_campact(cars)

#정답출력
print('<8번 정답>')
for line in reversed(sorted(ans.items(), key = lambda x : x[1])) :
    print(line[0])






##############################################################################################################
##############################################################################################################
#공통된 부분을 통일할 수 있는 함수 만들기.
print('\n')
print('='*70)

class Car(object):
    def __init__(self, manufacturer, model, displ, year, cyl, trans, drv, cty, hwy, fl, car_class):
        self.manufacturer = manufacturer
        self.model = model
        self.displ = displ
        self.year = year
        self.cyl = cyl
        self.trans = trans
        self.drv = drv
        self.cty = cty
        self.hwy = hwy
        self.fl = fl
        self.car_class = car_class

    def __repr__(self):
        return '{}-{}' .format(self.manufacturer, self.model)

file = open('C:/Users/i/Desktop/mpg.txt')
cars = []
while True :
    line = file.readline().rstrip()
    if not line :
        break
    c_d = line.split(',')
    cars.append(Car(c_d[0], c_d[1], c_d[2], c_d[3], c_d[4], c_d[5], c_d[6], c_d[7], c_d[8], c_d[9], c_d[10]))
file.close()
cars = cars[1:]


class Solve(object) :

    def __init__(self, my_list):
        self.list = my_list

    #1.
    def check_hwy(self, num_l, num_u) :
        self.result_1 = {}
        for car in self.list :
            if int(car.hwy) <= num_l or int(car.hwy) >= num_u:
                if car.model in self.result_1.keys():
                    self.result_1[car.model][0] += int(car.hwy)
                    self.result_1[car.model][1] += 1
                else:
                    self.result_1[car.model] = [int(car.hwy), 1]

        for k, v in self.result_1.items() :
            self.result_1[k] = round(v[0] / v[1], 1)

        self.ans_1 = reversed(sorted(self.result_1.items(), key = lambda x : x[1]))

        print('\n', end='')
        print('**<1번 정답>**')
        for line in self.ans_1 :
            print(line[0])


    #2.
    def check_man_cty(self):
        self.result_2 = {}
        for car in self.list :
            if car.manufacturer in ['audi', 'toyota'] and car.manufacturer in self.result_2.keys():
                self.result_2[car.manufacturer][0] += float(car.cty)
                self.result_2[car.manufacturer][1] += 1
            if car.manufacturer in ['audi', 'toyota'] and car.manufacturer not in self.result_2.keys():
                self.result_2[car.manufacturer] = [float(car.cty), 1]

        for k, v in self.result_2.items() :
            self.result_2[k] = round(v[0] / v[1], 1)

        self.ans_2 = reversed(sorted(self.result_2.items(), key = lambda x : x[1]))

        print('\n', end='')
        print('**<2번 정답>**')
        for line in self.ans_2 :
            print(line[0])


    #3.
    def check_man_hwy_3(self):
        self.result_3 = {}
        for car in self.list :
            if car.manufacturer in ['chevrolet', 'ford', 'honda'] and car.manufacturer in self.result_3.keys():
                self.result_3[car.manufacturer][0] += float(car.hwy)
                self.result_3[car.manufacturer][1] += 1
            if car.manufacturer in ['chevrolet', 'ford', 'honda'] and car.manufacturer not in self.result_3.keys():
                self.result_3[car.manufacturer] = [float(car.cty), 1]

        for k, v in self.result_3.items():
            self.result_3[k] = round(v[0] / v[1], 1)

        print('\n', end='')
        print('**<3번 정답>**')
        for k, v in self.result_3.items():
            print(k, ':', v)


    #4.
    def check_audi(self):
        self.result_4 = {}
        for car in self.list :
            if car.manufacturer == 'audi':
                self.name_4 = '{} {} {} {} {}'.format(car.model, car.displ, car.year, car.cyl, car.trans)
                if self.name_4 in self.result_4.keys():
                    self.result_4[self.name_4][0] += float(car.hwy)
                    self.result_4[self.name_4][1] += 1
                else:
                    self.result_4[self.name_4] = [float(car.hwy), 1]

        for k, v in self.result_4.items():
            self.result_4[k] = round(v[0] / v[1], 1)

        self.ans_4 = list(reversed((sorted(self.result_4.items(), key = lambda x : x[1]))))

        print('\n', end='')
        print('**<4번 정답>**')
        for k, v in self.ans_4[:5] :
            print(k)


    #5.
    def check_suv(self):
        self.result_5 = {}
        for car in self.list :
            if car.car_class == 'suv':
                if car.manufacturer in self.result_5.keys():
                    self.result_5[car.manufacturer][0] += (float(car.hwy) + float(car.cty)) / 2
                    self.result_5[car.manufacturer][1] += 1
                else:
                    self.result_5[car.manufacturer] = [(float(car.hwy) + float(car.cty)) / 2, 1]

        for k, v in self.result_5.items():
            self.result_5[k] = round(v[0] / v[1], 1)

        self.ans_5 = reversed((sorted(self.result_5.items(), key = lambda x : x[1])))

        print('\n', end='')
        print('**<5번 정답>**')
        for line in ans2[:5]:
            print(line[0])


    #6.
    def check_var_cty(self):
        self.result_6 = {}
        for car in self.list :
            if car.car_class in self.result_6.keys():
                self.result_6[car.car_class][0] += float(car.cty)
                self.result_6[car.car_class][1] += 1
            else:
                self.result_6[car.car_class] = [float(car.cty), 1]

        for k, v in self.result_6.items():
            self.result_6[k] = round(v[0] / v[1])

        self.ans_6 = list(reversed(sorted(self.result_6.items(), key=lambda x: x[1])))

        print('\n', end='')
        print('**<6번 정답>**')
        for line in self.ans_6:
            print(line[0])


    #7.
    def check_man_hwy(self):
        self.result_7 = {}
        for car in self.list:
            if car.manufacturer in self.result_7.keys():
                self.result_7[car.manufacturer][0] += float(car.hwy)
                self.result_7[car.manufacturer][1] += 1
            else:
                self.result_7[car.manufacturer] = [float(car.hwy), 1]

        for k, v in self.result_7.items():
            self.result_7[k] = round(v[0] / v[1], 1)

        self.ans_7 = list(reversed(sorted(self.result_7.items(), key=lambda x: x[1])))

        print('\n', end='')
        print('**<7번 정답>**')
        for line in self.ans_7:
            print(line[0])


    #8.
    def count_campact(self):
        self.result_8 = {}
        for car in self.list:
            if car.car_class == 'compact' and car.manufacturer in self.result_8.keys():
                self.result_8[car.manufacturer] += 1
            elif car.car_class == 'compact' and car.manufacturer not in self.result_8.keys():
                self.result_8[car.manufacturer] = 1

        print('\n', end='')
        print('**<8번 정답>**')
        for line in reversed(sorted(self.result_8.items(), key=lambda x: x[1])):
            print(line[0], ':', line[1])




print('\n')
print('"통합 클래스 사용한 정답"')
solve_prob = Solve(cars)
solve_prob.check_hwy(4, 5)
solve_prob.check_man_cty()
solve_prob.check_man_hwy_3()
solve_prob.check_audi()
solve_prob.check_suv()
solve_prob.check_var_cty()
solve_prob.check_man_hwy()
solve_prob.count_campact()


#객체의 속성은 class에 넣어서 구동하지만, business logic은 그냥 밖에서 함수로서 구동하면 된다.
#꼭 클래스 안에 안 넣어도 된다.
#그냥 위에서처럼 각각의 함수로 밖에서 구현해도 된다.
#괜히 개고생함 ㅡㅡ.