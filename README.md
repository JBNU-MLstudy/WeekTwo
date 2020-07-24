# WeekTwo
2주차 <br>
200722 summary
--------------

### 백준 알고리즘 
#### while 2번  
: 두 정수 a와 b를 입력받은 다음, a+b를 출력하는 프로그램을 작성하시오 <br>
while True: # true지정하여 infinite loop <br>
    try:  # 시행 <br>
        a,b = map(int, input().split()) # 변수 a, b 선언 <br>
        print("{}".format(a+b)) # a,b 합한 값 출력 <br>
    except: # 입력값 없으면 <br>
        break # loop out  <br>
<br>
#### while 3번
> 더하기 사이클, 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. <br> 
  그 다음 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. <br> 
  이 사이클의 길이를 구하는 프로그램을 작성하시오. <br>
<br>
N = int(input()) # 입력변수 <br>
c=0 # 사이클 counting하는 변수 초기값 0으로 선언 <br>
r=N # n을 받아 operating하는 변수 선언 <br>
while True : # 무한루프 <br>
    s=int(r/10)+r%10  <br>
# '/ -> 몫, % -> 나머지' 연산자를 이용하여, 두자리 수를 받았을 때 10으로 나누어 몫과 나머지 합을 구함. 이떄 몫은 실수(float)가 될 수 있으므로 정수로 선언 <br>
    r=10*(r%10)+s%10 <br>
# 나머지 연산자를 이용하여 나머지끼리 더함 <br>
    c=c+1 # 위의 연산과정 counting <br>
    if r==N : # r의 결과값과 입력값 n과 같은지 확인 <br>
        break # 맞으면 loop out <br>
print(c) # 연산 횟수 출력 <br>
<br>
while ==> 조건반복문(conditional loop) <br> 
for ==> 범위지정 반복문(range) <br>
% 둘 다 if문 선언 가능함  <br>

#### 함수 
def와 class가 있음 <br>
def(변수): <br>
   내용 <br>
<br>
class(변수 or class or 함수): <br> 
   내용(함수(def여러개 작성 가능)) <br>
==> class는 상속개념 내포되어 있음 <br>
<br>
클래스(상속개념까지)
<ul> https://wikidocs.net/16073 </ul>  

#### DS[데이터사이언스] ) = AI[인공지능] ) = ML[머신러닝] ) = DL[딥러닝] ) =
> 범위를 단정짓기에 조금 모호함 <br>
  손바닥으로 치자면 딥러닝은 손톱, 머신러닝은 손가락, 인공지능은 손바닥 <br>

#### 딥러닝 공부하면서 느낀 것: 
> 미적분과 선형대수 필수로 공부해야함. <br>
  요즘 머신러닝을 수학없이 구현할 수 있지만(하지만, 수학 없는 머신러닝은 모래성 쌓기와 비슷함), <br>
  딥러닝은 개념 이해를 위해 수학적 지식이 필요함<br>

#### supervised learning vs unsupervised learning
- 속성(column)에 대한 정보 인지의 유무에 대해 나뉘어짐 <br>
- unsupervised learning ex) 주식예측(언제 변화될지 모르기에) <br>  
- supervised learning ex) 학생 등록금 분류 <br>

#### 선형회귀(Linear regression)
Y = AX+B <br>
주어진 데이터를 예측하는 것(선형성, 독립성, 등분산성을 가짐)<br>
Y: 종속변수, 주어진 데이터에 따라 값이 달라짐 즉, 종속성을 띔<br>
X: 독립변수, 주어지는 데이터 즉, 독립성을 띔 <br>
<ul> https://danbi-ncsoft.github.io/study/2018/05/04/study-regression_model_summary.html </ul>

#### 로지스틱회귀(Logistic regression)
Y = e^x/1+e^x <br>
종속변수 y의 결과가(실패, 성공)와 같이 2개의 카테고리가 존재하는 것을 의미 <br>
classification할 때 쓰임 <br>
 <ul> https://3months.tistory.com/327 </ul>
<br>
※ 마지막에 로지스틱 회귀 설명을 다중선형회귀와 헷깔려서 로지스틱을 다중선형회귀로 설명해 드렸습니다. 죄송합니다. 
<br>

오늘 진행한 스터디는 유튜브에 일부공개로 올렸습니다.
<ul> https://youtu.be/GUe3C5aRlXg </ul>
