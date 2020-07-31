'''
#문제1) 1000보다 작은 자연수 중에서 3 또는 5의 배수들의 합은?
result = 0
for i in range(1, 1000) :
    if (i % 3 == 0) or (i % 5 == 0) :
        result += i
print(result)


#문제2) 피보나치 수열에서 짝수이면서 4백만 이하인 모든 항을 더하면 얼마입니까?
pibo = [1, 2]
result = 0
while True :
    if (pibo[-1] % 2 == 0) :
        result += pibo[-1]
    pibo.append(pibo[-1] + pibo[-2])
    if pibo[-1] > 400*(10**4) :
        break
print(result)

#문제3) 알파벳 대소문자로 된 문자열이 주어지면, 이 문자열에서 가장 많이 사용된 알파벳이 무엇인지 출력하라.
#       단, 대소문자는 구별하지 않는다. 동률이 있는 경우 알파벳 순으로 제일 앞에 있는 문자를 출력하라.
a = 'This is a sample Program mississippi river'
b = 'abcdacbbbsbdbadbababadbsbabd'

my_upper = list(b.upper())
my_keys = {}
for i in my_upper :
    if (i != ' ') and (i not in my_keys.keys()) :
        my_keys[i] = 1
    elif (i != ' ') and (i in my_keys.keys()) :
        my_keys[i] += 1
result = sorted(my_keys.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])


## 문제 4.
## 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이
## 같은 수를 대칭수(palindrome)라고 부릅니다.

## 두 자리 수를 곱해 만들 수 있는 대칭수 중
## 가장 큰 수는 9009 (= 91 × 99) 입니다.

## 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하세요

def solve(x) :
    left = 10**(x)-1
    right = 10**(x)-1
    result = 0
    for i in range(left, 0, -1) :
        for j in range(right, 0, -1) :
            mul = i * j
            var = list(str(mul))
            var_rev = list(reversed(var))
            if var == list(reversed(var)) and result < mul :
                result = mul
    return result

print(solve(3))


################################################

## 문제 5.
## 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

## 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

def solve(x) :
    result = 1
    for i in range(2, x+1) :
        if (result % i) != 0 :
            mul = i
            while mul <= x :
                result *= i
                mul *= i
    return result

print(solve(20))

#
# 1 2 3 4 5 6 7 8 9 10
#
# 2 2 2 3 3 5 7

#
################################################################

## 문제 6.
## 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

## 이 때 10,001번째의 소수를 구하세요.

def solve(x) :
    count = 1
    result = 2
    while count < x :
        result += 1
        breaker = False
        for i in range(2, result) :
            if result % i == 0 :
                breaker = True
                break
        if not breaker :
            count += 1
    return result

print(solve(10001))
'''



################################################################
#https://moon9342.github.io/python-lecture-python-program-exercise-1
################################################################

### 문제 1.
### 10보다 작은 자연수 중에서 3 또는 5의 배수는
### 3,5,6,9가 존재해요! 이것들의 합은 23입니다.

### 1000보다 작은 자연수 중에서 3 또는 5의 배수들을
### 구해서 모두 합하면 얼마인가요?

def solve(x, num_l, num_u) :
    result = 0
    for i in range(x) :
        if i % num_l == 0 or i % num_u == 0 :
            result += i

    return  result

print('1번정답', end=':')
print(solve(10, 3, 5))
print('1번정답', end=':')
print(solve(1000, 3, 5))


### 문제 2.
### 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다.
### 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

### 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
### 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?


def pibo(x) :
    result = 0
    lower = 1
    upper = 2
    while True :
        if upper > x :
            break
        if upper % 2 == 0 :
            result += upper
        copy = upper
        upper += lower
        lower = copy

    return result

print('2번정답', end=':')
print(pibo(400*(10**4)))



## 문제 3.
## 알파벳 대소문자로 된 문자열이 주어지면,
## 이 문자열에서 가장 많이 사용된 알파벳이
## 무엇인지 출력하는 프로그램을 작성하시오.
## 단, 대소문자는 구별하지 않아요. 만약 동률이 존재하는 경우
## 알파벳 순으로 제일 앞에 있는
## 문자를 출력하세요.

## 문자열) "This is a sample Program mississippi river"
## 문자열) "abcdabcdababccddcd"


def solve(x) :
    upper = list(x.upper())
    count_dict = {}
    for abc in upper :
        if abc != ' ' and abc not in count_dict.keys() :
            count_dict[abc] = 1
        elif abc != ' ' :
            count_dict[abc] += 1
    result = sorted(count_dict.items(), key=lambda x : (-x[1], x[0]))

    return  result[0][0]

print('3번정답', end=':')
print(solve("This is a sample Program mississippi river"))
print('3번정답', end=':')
print(solve("abcdabcdababccddcd"))





## 문제 4.
## 로또 프로그램 작성
## 5000원으로 로또복권을 5장 자동으로 구매합니다.
## 이번 주 로또 당첨번호를 생성하여 로또 당첨을 확인하세요!
## 쉬운버전으로 먼저 작성합니다.
## 6숫자가 다 맞으면 1등, 5개 맞으면 2등으로 처리합니다.
## 즉, 쉬운버전은 보너스 숫자는 없는 것으로 간주합니다.
## 쉬운버전을 해결했다면
## 보너스 숫자를 이용하여 로또 당첨을 확인합니다.
## 보너스 숫자를 제외한 모든 숫자가 다 맞으면 1등,
## 보너스 숫자를 포함하여 6개의 숫자가 맞으면 2등,
## 보너스를 제외하고 5개의 숫자가 맞으면 3등으로 처리합니다.

## 쉬운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
## 4등 몇개, 꽝 몇개로 출력
## 어려운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
## 4등 몇개, 5등 몇개, 꽝 몇개로 출력

## 랜덤값을 도출하기 위해서는 다음의 코드를 이용한다.
import random

i = random.randint(1, 100)  # 1부터 100 사이의 임의의 정수
f = random.random()  # 0부터 1 사이의 임의의 float
i = random.randrange(1, 101, 2)  # 1부터 100 사이의 임의의 짝수
i = random.randrange(10)  # 0부터 9 사이의 임의의 정수

##### 추가문제
##### 1등에 당첨될려면 평균적으로 얼마만큼의 돈을 투자해야 할까요?
##### 로또 1게임은 1000원입니다.

#쉬운 버전

def solve_easy(win) :
    import random
    nums = []
    all_num = range(1, 46)
    for _ in range(5):
        nums.append(random.sample(all_num, 6))

    def check(x, y):
        count = [0] * 7
        for i in x:
            count[len(set(y) - set(i))] += 1
        return count

    ans = check(nums, win)
    print('**4번 정답_easy**')
    print('1등 {}개'.format(ans[0]))
    print('2등 {}개'.format(ans[1]))
    print('3등 {}개'.format(ans[2]))
    print('4등 {}개'.format(ans[3]))
    print('5등 {}개'.format(ans[4]))
    print('꽝 {}개'.format(sum(ans[5:])))

solve_easy(random.sample(range(1, 46), 6))


#어려운 버전

def solve_hard(win) :
    import random
    nums = []
    all_num = range(1, 46)
    for _ in range(5):
        nums.append(random.sample(all_num, 6))

    win_fix = win[:6]
    bonus = win[6]

    def check(x, y, b) :
        count = [0]*7
        count_bonus = 0
        for i in x :
            count[len(set(y) - set(i))] += 1
        for i in x :
            if len(set(y) - set(i)) == 5 and b in i :
                count_bonus += 1

        return count, count_bonus

    ans = check(nums, win_fix, bonus)
    print('**4번 정답_hard**')
    print('1등 {}개'.format(ans[0][0]))
    print('2등 {}개'.format(ans[1]))
    print('3등 {}개'.format(ans[0][1]))
    print('4등 {}개'.format(ans[0][2]))
    print('5등 {}개'.format(ans[0][3]))
    print('꽝 {}개'.format(sum(ans[0][4:])))

solve_hard(random.sample(range(1, 46), 7))


#얼마 투자해야 할까?
def solve(win) :
    import random
    nums = []
    all_num = range(1, 46)
    for _ in range(5):
        nums.append(random.sample(all_num, 6))

    win_fix = win[:6]
    bonus = win[6]

    def check(x, y, b) :
        count = [0]*7
        count_bonus = 0
        for i in x :
            count[len(set(y) - set(i))] += 1
        for i in x :
            if len(set(y) - set(i)) == 5 and b in i :
                count_bonus += 1

        return count, count_bonus

    return check(nums, win_fix, bonus)

def how_much() :
    import random
    count = 0
    while True :
        count += 1
        if solve(random.sample(range(1, 46), 7))[0][0] > 0 :
            print(1000*count)
            break
        else :
            count += 1

#how_much()   2482893번의 시도 끝에 1등 당첨자가 나왔다.




## 문제 5.
## 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고,
## 이 소수들을 그 수의 소인수라고 합니다.
## 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

## 600851475143의 소인수 중에서 가장 큰 수를 구하세요.


'''
#이 수가 소수인지 확인한다.
def is_only(x) :
    for i in range(2, x) :
        if x % i == 0 :
            return False
    return True

#큰 수부터 하나씩 나누어떨어지는지 확인한다.
def solve(x) :
    for i in range(x-1, 1, -1) :
        if x % i == 0 and is_only(i) :
            return i

print('5번 정답', end=':')
print(solve(600851475143))

#너무 오래 걸린다.


def is_only(x) :
    for i in range(2, x) :
        if x % i == 0 :
            return False
    return True

def solve(x) :
    result = 2
    for i in range(3, x) :
        if i % 2 != 0 and is_only(i) :
            result *= i
            if result == x :
                return i

print('5번 정답', end=':')
print(solve(600851475143))
'''


#일단 작은 소수부터 나눈다. 나눠지면 그 나머지에 대해서만 소인수를 찾는데, 그 전의 소수보다 큰 값부터 찾는다.

def is_only(x) :
    for i in range(2, x) :
        if x % i == 0 :
            return False
    return True

def solve(x) :
    num = x
    result = 0
    for i in range(2, x) :
        if num % i == 0 and is_only(i) :
            num = num / i
            result = i
            if num == 1 :
                return result

print('5번 정답', end=':')
print(solve(600851475143))
#금방 나온다.
#이미 나눠지는 소수를 구했으면 원래 수에서 나눠지는지 확인할 필요가 없다.
#나눈수에서 확인하면 된다.






## 문제 6.
## 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이
## 같은 수를 대칭수(palindrome)라고 부릅니다.

## 두 자리 수를 곱해 만들 수 있는 대칭수 중
## 가장 큰 수는 9009 (= 91 × 99) 입니다.

## 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하세요

def solve(x) :
    left = 10**(x)-1
    right = 10**(x)-1
    result = 0
    for i in range(left, 0, -1) :
        for j in range(right, 0, -1) :
            mul = i * j
            var = list(str(mul))
            if var == list(reversed(var)) and result < mul :
                result = mul
    return result

print('6번 정답', end=':')
print(solve(3))








## 문제 7.
## 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

## 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
def solve(x) :
    result = 1
    for i in range(2, x+1) :
        if (result % i) != 0 :
            mul = i
            while mul <= x :
                result *= i
                mul *= i
    return result

print('7번 정답', end=':')
print(solve(20))




## 문제 8.
## 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
## 1**2 + 2**2 + ... + 10**2 = 385

## 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
## (1 + 2 + ... + 10)**2 = 552 = 3025

## 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의
## 차이는 3025 - 385 = 2640 이 됩니다.

## 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는
## 얼마입니까?


def solve(x) :
    square = sum([i**2 for i in range(1, x+1)])
    add_sq = sum(list(range(1, x+1)))**2

    return abs(square - add_sq)

print('8번 정답', end=':')
print(solve(100))






## 문제 9.
## 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

## 이 때 10,001번째의 소수를 구하세요.
def solve(x) :
    count = 1
    result = 2
    while count < x :
        result += 1
        breaker = False
        for i in range(2, result) :
            if result % i == 0 :
                breaker = True
                break
        if not breaker :
            count += 1
    return result

#print('9번 정답', end=':')
#print(solve(10001))          #좀 오래걸림


def is_only(x) :
    for i in range(2, x) :
        if x % i == 0 :
            return False
    return True

def solve(x) :
    count = 1
    result = 2
    while True :
        if count == x :
            return result
        result += 1
        if is_only(result) :
            count += 1

print('9번 정답', end=':')
print(solve(10001))       #이 방법도 오래걸림




## 문제 10.
## 세 자연수 a, b, c 가 피타고라스 정리 a**2 + b**2 = c**2 를 만족하면
## 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
## 예를 들면 3**2 + 4**2 = 9 + 16 = 25 = 5**2이므로
## 3, 4, 5는 피타고라스 수입니다.

## a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다.
## 이 때, a × b × c 는 얼마입니까?

def solve(x) :
    for a in range(1, x) :
        for b in range(a+1, x-a) :
            c = x - b - a
            if a**2 + b**2 == c**2 :
                return a*b*c

print('10번 정답', end=':')
print(solve(1000))
#고민은 좀 했는데 바로 나온다. 생각보다 간단하다.





## 문제 11.
## 양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.

## n → n / 2 (n이 짝수일 때)
## n → 3 * n + 1 (n이 홀수일 때)

## 13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.

## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

## 아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도
## 마지막에는 1로 끝나리라 생각됩니다.
## (이런 수들을 우박수 hailstone sequence라 합니다.)

## 그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데
## 가장 긴 과정을 거치는 숫자는 얼마입니까?
## 계산 과정 도중에는 숫자가 백만을 넘어가도 괜찮습니다.


#저 이상한 계산 과정을 수행하는 함수를 만든다.
def calcualte(x) :
    count = 0
    num = x
    while True :
        if num == 1 :
            return count
        if num % 2 == 0 :
            num /= 2
            count += 1
            continue
        if num % 2 != 0 :
            num = 3*num + 1
            count += 1
            continue

#이제 백만 이하의 모든 수들에 대해 확인해본다.
def solve(x) :
    result = -1
    ans = 0
    for i in range(1, x+1) :
        if calcualte(i) > result :
            result = calcualte(i)
            ans = i

    return ans

# print('11번 정답', end=':')
# print(solve(1000000))    #837799. 오래 걸린다.






## 문제 12.
## 다음과 같은 특성을 갖는 숫자의 개수를 찾는 기능을 구현합니다.
## 입력으로 두개의 숫자( x, y )를 이용합니다.
## - 두 개의 숫자 x와 y를 이용하여,
##   x초과 y미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##   되는 숫자를 찾습니다.
## - 숫자들을 모두 찾은 후 해당 숫자가 총 몇 개인지를 출력합니다.

## 예1) 두 개의 숫자 1과 100이 주어졌을 경우,
##      1초과 100미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##      되는 숫자를 찾습니다.
##      - 20의 경우 각 자리 숫자를 모두 더한 값이 2이므로, 적합하지 않다.
##      - 23의 경우 각 자리 숫자를 모두 더한 값이 5이므로, 적합하다.
##      [총 개수] 19

## 예2) 두 개의 숫자 5와 500이 주어졌을 경우,
##      5초과 500미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##      되는 숫자를 찾습니다.
##      [총 개수] 98

## 입력으로 주어지는 두 개의 수 : 100 10000

#각 자리의 숫자의 합이 5가 되는지 판별하는 함수를 먼저 만든다.
def check(x) :

    if sum([int(i) for i in list(str(x))]) % 5 == 0 :
        return 1
    return 0

def solve(lower, upper) :
    ans = 0
    for i in range(lower+1, upper) :
        ans += check(i)

    return ans


print('12번 정답', end=':')
print(solve(100, 10000))




## 문제 13.
## 6자리 이상 9자리 미만의 수를 입력으로 사용합니다.

## 수의 중앙을 기준으로 두 개의 수로 분리한 후 큰 수를 선택한다.
## - 수의 숫자개수가 홀수 개인 경우 수의 중앙 숫자를 기준으로
##   왼쪽과 오른쪽 수로 분리
## - 수의 숫자개수가 짝수 개인 경우 수를 반으로 나누어
##   왼쪽과 오른쪽 수로 분리
## 예1) 1234567 -> (123, 567) -> (567)
## 예2) 34217869 -> (3421, 7869) ->(7869)

## 입력으로 제공된 수를 더 이상 두 개의 수로 분리할 수 없을 때까지
## 과정을 반복하여 남은 최종 숫자를 구해 출력한다.
## 예1) 567 -> (5, 7) -> (7)
## 예2) 7869 -> (78, 69) -> (78) -> (7, 8) -> (8)

#그러니까, 한자리 수가 되면 끝난다.

#먼저, 나누고 큰 수를 고르는 함수부터 만든다.
# def split_num(x) :
#     result = str(x)
#     ind = len(result) // 2
#     left = int(result[:ind])
#     right = int(result[ind:]) if ind % 2 == 0 else int(result[ind+1:])
#     return max(left, right)
#

#이걸 다시 함수에서 쓸 필요 없고, 그냥 단순 반복하면 되겠다.
def solve(x) :
    result = str(x)
    while True :
        if len(result) == 1 :
            return int(result)
        ind = len(result) // 2
        left = int(result[:ind])
        right = int(result[ind:]) if len(result) % 2 == 0 else int(result[ind+1:])
        result = str(max(left, right))

print('13번 정답', end=':')
print(solve(34217869))





## 문제 14.
## 2**15 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.

## 2**1000의 각 자리수를 모두 더하면 얼마입니까?

def solve(x) :
    return sum(int(i) for i in list(str(x)))

print('14번 정답', end=':')
print(solve(2**1000))







## 문제 15.
## 각 부품의 생산정보가 문자열로 제공된다.
## [부품생산정보] : A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8

## 각 부품정보는 부품명과 품질데이터로 구성된다.
## - A,B,C 3개의 부품이 있으며 품질은 1이상 10미만의 정수.
##   예) A7 : A부품, 품질 7

## 생산정보에서 품질이 7이상인 부품만을 순서대로 선택한다.
## [생산정보] A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8
## [품질이 7이상인 부품 목록] A7A8B9A8B9C7C7B9A7B8C9A8

## 품질이 7이상인 부품들을 조립해 완성품을 만든다.
## A, B, C 세 부품이 순서대로 있을 때만 부품을 조립한다.
## A7A8B9A8B9C7C7B9A7B8C9A8 => A8B9C7, A7B8C9 2개 조립
## 조립한 부품의 목록과 전체 조립한 개수를 출력


def solve(x) :
    ind = len(x) // 2
    result = []
    ans = []
    for i in range(ind) :
        lower = 2*i
        upper = lower+2
        if int(x[lower+1]) >= 7 :
            result.append(x[lower:upper])
    for i in range(len(result)-2) :
        try :
            if (result[i][0], result[i+1][0], result[i+2][0]) == ('A', 'B', 'C') :
                ans.append(result[i]+result[i+1]+result[i+2])
        except :
            return ans, '{}개' .format(len(ans))
    return ans, '{}개' .format(len(ans))


print('15번 정답', end=':')
print(solve('A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8'))





## 문제 16.
## n! 이라는 표기법은 n × (n − 1) × ... × 3 × 2 × 1을 뜻합니다.

## 예를 들자면 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 이 되는데,
## 여기서 10!의 각 자리수를 더해 보면 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 입니다.

## 100! 의 자리수를 모두 더하면 얼마입니까?


def solve(x) :
    ans = 1
    for i in range(2, x+1) :
        ans *= i
    return sum(int(i) for i in list(str(ans)))

print('16번 정답', end=':')
print(solve(100))








## 문제 17.
## 최소 10개 이상 최대 20개 이하의 숫자로 구성된 숫자목록이 배열 혹은 리스트 형태로 제공된다.
## 숫자목록 : 1,3,4,5,7,9,2,3,4,7

## 아래의 순서로 숫자목록의 숫자를 교환하여 재배치한다.
## 1) 숫자목록의 앞에서부터 4개의 숫자를 선택한다.
##    목록에서 숫자 선택 : [1,3,4,5],7,9,2,3,4,7
## 2) 선택된 4개의 숫자의 합을 구한다.
##    4개의 숫자 합 : [1,3,4,5],7,9,2,3,4,7 => 13
## 3) 첫 번째와 두 번째 숫자를 교환하고 세 번째와 네 번째 숫자를 교환한다.
##    숫자 교환 : [3,1,5,4],7,9,2,3,4,7
## 4) 오른쪽으로 한칸씩 이동하여 순서대로 1,2,3번 과정을 반복해 숫자목록의 숫자를 재배치한다.
## 예) [1,3,4,5],7,9,2,3,4,7 =>
##     [3,1,5,4],7,9,2,3,4,7 =>
##     3,[1,5,4,7],9,2,3,4,7 -> …

## 숫자목록의 끝까지 숫자배치를 진행할 때 선택되는 4개의 수의 최대 합을 출력

## [초기 입력 데이터]
## 1 3 4 5 7 9 2 3 4 7
## ---------------------------------------------------------------
## [선택된 4개의 수의 최대 합]: 21


## [초기 입력 데이터]
## 10 15 3 5 9 5 7 8 9 15 44 54 15 67 32 25 48 98 44 56
## ---------------------------------------------------------------
## [선택된 4개의 수의 최대 합]: 159



def solve(x) :
    xx = [int(i) for i in x.split()]
    ans = 0
    for i in range(len(xx)-3) :
        ans = max(ans, sum(xx[i:i+4]))
        first = xx[i]
        second = xx[i+1]
        xx[i] = second
        xx[i+1] = first
        third = xx[i+2]
        fourth = xx[i+3]
        xx[i+2] = fourth
        xx[i+3] = third

    return ans


print('17번 정답', end=':')
print(solve('10 15 3 5 9 5 7 8 9 15 44 54 15 67 32 25 48 98 44 56'))








## 문제 18.
## 어떤 대상을 순서에 따라 배열한 것을 순열이라고 합니다.
## 예를 들어 3124는 숫자 1, 2, 3, 4로 만들 수 있는 순열 중 하나입니다.

## 이렇게 만들 수 있는 모든 순열을 숫자나 문자 순으로 늘어놓은 것을
## 사전식(lexicographic) 순서라고 합니다.

## 0, 1, 2로 만들 수 있는 사전식 순열은 다음과 같습니다.
## 012   021   102   120   201   210


## 0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 사전식 순열에서
## 1,000,000번째는 무엇입니까?



#재귀와 연관이 있어 보이는데...












## 문제 19.
## 입력으로 제공되는 숫자열에서 짝수와 홀수를 추출하여 새로운 숫자열을 생성한다.
## 1) 입력된 숫자열에서 짝수와 홀수를 순서대로 추출한다.
##    [입력] 78235169
##    [짝수 추출] 826
##    [홀수 추출] 73519
## 2) 추출된 짝수의 뒤에 추출된 홀수를 연결하여 새로운 숫자열을 생성한다.
##    [짝수와 홀수 연결] 82673519

## 결과숫자열을 앞에서부터 순서대로 뺄셈 연산 또는 덧셈 연산 한다.
## 숫자열의 앞에서 부터 순서대로 뺄셈 연산한다.
## 단, 앞선 연산 결과가 0 이하이면 그 차례에는 덧셈 연산한다.
## [결과 숫자열] 82673519
## [각 수의 연산 순서와 방법]
##   8 - 2 = 6
##   6 – 6 = 0
##   0 + 7 = 7 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   7 – 3 = 4
##   4 – 5 = -1
##  -1 + 1 = 0 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   0 + 9 = 9 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
## [연산 결과] 9

## [입력]: 78235169
## [출력]: 9

## [입력]: 693756874
## [출력]: 7



def solve(x) :
    even = ''
    odd = ''
    for i in str(x) :
        if int(i) % 2 == 0 :
            even += i
        else :
            odd += i
    result = even+odd
    ans = int(result[0])
    start = True
    for i in range(1, len(result)) :
        if start or ans > 0 :
            ans -= int(result[i])
            start = False
        else :
            ans += int(result[i])

    return ans



print('19번 정답', end=':')
print(solve(693756874))
