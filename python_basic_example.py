'''
Class Example
'''

class student:
    def __init__(self, name, id): ## 객체 생성자
        self.name = name ## 인스턴스 변수
        self.id = id
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id

best = student('lee', 101)
best.get_name()
best.get_id()

'''
List Example
'''

a = [40, 10, 70, 60] # a[0]에는 40이라는 정수 객체의 레퍼런스가 저장된다.
a.pop() # 리스트 마지막 항목 제거
print(a)
a.pop(0) # 리스트 첫 항목 제거
print(a)

'''
수행시간 측정
'''
import time
start_time = time.time()
print("%s seconds" % (time.time()-start_time))

'''
난수발생
'''

import random
random.seed(0) # 초기값 지정
random.randint(1, 1000) # 1과 1000 사이의 난수 1개를 생성

'''
내장함수
'''

ord("문자") # 문자의 unicode 값을 리턴
reversed([]) # 리스트를 역순으로 만든다
lambda 인자(auguments) : 식(expression) # 함수의 이름도 return도 없이 수행되는 함수
filter(expression, sequence)
map(expression, sequence)

'''
Lambda, Filter, Map Example
'''
a = [1,5,4,6,8,11,3,12]
even = list(filter(lambda x : x%2==0, a)) # a에서 짝수만 리스트로 리턴
ten_times = list(map(lambda x : x*10, a)) # a에 10배하여 리스트로 리턴

b = [[0,1,8],[7,2,2],[5,3,10],[1,4,5]]
b.sort(key = lambda x: x[2]) # b의 각 원소의 마지막 숫자를 기준으로 정렬, sort는 in-place 함수

'''
recursion
'''

def recurse():
    print(' *')
    recurse()

recurse()
## RecursionError : 스스로의 호출을 중단시킬 수 있는 조건문이 없기 때문

