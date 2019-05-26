# data_structures_with_python

## notion
자료구조란?
일련의 동일한 타입의 데이터를 정돈하여 저장한 구성체.
동일한 타입으로 데이터를 정돈하는 이유는 데이터에 대해 탐색, 삽입, 삭제 등의 연산을 효율적으로 수행하기 위해서.
자료구조 설계시에는 데이터와 데이터에 관련된 연산을 함께 고려해야 함.
추상데이터타입을 구체적으로 구현한 것.

추상데이터타입이란?
데이터와 데이터에 대한 추상적인 연산들로 구성된 것.

두 개념의 관계 예시) 건축 설계도 : 건물 = 추상데이터타입 : 자료구조

## 자료구조의 효율성
알고리즘 수행시간, 연산의 수행시간으로 효율성을 측정한다.
수행시간을 나타내는 시간복잡도(Time Complexity)와 사용되는 메모리 공간의 크기를 나타내는 공간복잡도(Space Complexity)에 기반하여 평가한다.
시간복잡도는 알고리즘이 실행되는 동안에 사용된 기본적인 연산 횟수를 입력 크기의 함수로 표현.
기본적인 연산(Elementary Operation)이란 데이터간 크기 비교, 데이터 읽기 및 갱신, 숫자 계산같은 단순한 연산을 의미.

최악경우(Worst-case) : 어떤 입력이 주어지더라도 얼마 이상은 넘지 않는다는 상한의 개념
평균경우(Average-case) : 균등분포에 따른 무작위 입력이 주어졌을 때 소요되는 시간
최선경우(Best-case) : 가장 빠른 수행시간을 고려하기에 최적 알고리즘을 찾는데 활용

점근표기법
입력의 크기에 대한 함수

O(Big-Oh)-표기법 : 모든 $N \ge N_0$ 에 대해서 $f(N) \le cg(N)$이 성립하는 양의 상수 $c$와 $N_0$이 존재하면, $f(N) = O(g(N))$이다.
상한 표기
$&Omega;$(Big-Omega)-표기법 : 모든 $N \ge N_0$ 에 대해서 $f(N) \ge cg(N)$이 성립하는 양의 상수 $c$와 $N_0$이 존재하면, $f(N) = &Omega;(g(N))$이다.
하한 표기 
$\Theta$(Theta)-표기법 : 모든 $N \ge N_0$ 에 대해서 ${c_1}g(n) \ge f(N) \ge {c_2}g(N)$이 성립하는 양의 상수 $c_1$, $c_2$, $N_0$이 존재하면, $f(N) = \Theta(g(N))$이다.
중간 표기, O-표기와 $&Omega;$-표기가 동일한 경우에 사용

주로 O-표기법을 사용한다.

## 기타
파이썬 언어의 기본사항
순환(Recursion)