#
# 날짜 : 2020.09.04
# 내용 : greedy 기본예제 풀이
#        example -> 예제 3-1
#        start_1 -> 실전문제 : 큰수의 법칙 (p.92)  
#        start_2 -> 실전문제 : 숫자 카드 게임 (p.96)
#        start_3 -> 실전문제 :   
#-----------------------------------------#

def example():
  # greedy 기본 개념

  # 손님에게 거슬러줘야 할 돈이 n 원 일 때 
  # 거슬러줘야할 동전의 최소 개수를 구하시오
  
  # 보유하고 있는 잔돈의 종류는 500원 100원 50원 10원이다.
  # 각 동전의 양은 무한하게 있다고 가정한다

  num = 1260
  numCoiun = 0
  conins = [500, 100, 50, 10]

  for coin in conins:
      divCoin = num // coin
      numCoiun += divCoin

      num %= coin

      print('coin : ', coin)
      print('coin count : ', divCoin)
      print('mod num : ', num)

  print(numCoiun)


def start_1():

  # 풀이시간 30분, 시간 제한 1초, 메모리 제한 128MB

  # 주어진 n 개의 숫자를 m 번 더하여 가장 큰수를 만든다
  # 단 배열의 특정한 인덱스가 k 번 반복되어선 안된다

  # 2, 4, 5, 4, 6 로 이루어진 배열이 있을 때 m 이 8이고 k가 3이라면
  # 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46 이 된다
  # 단, 서로다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주
  # 3, 4, 3, 4 로 이뤄진 배열이 있고 m이 7 k가 2 이면
  # 4 + 4 + 4 + 4 + 4 + 4 + 4 = 28 이 도출 된다

  # 주어지는 n, m, k 는 자연수이며 각 자연수는 공백으로 구분한다 
  # 2 <= n <= 1000
  # 1 <= m <= 10000
  # 1 <= k <= 10000

  # 두번째 줄에 입력되는 변수는 n 개의 자연수가 주어진다
  # 각 자연수는 공백으로 구분한다
  # 주어지는 자연수의 범위는 1 이상 10,000 이하의 값이다

  # 입력으로 주어지는 k는 항상 m 보다 작거나 같다

  # 출력은 위 공식을 사용하여 최대 값을 출력한다

  # N,K,M 인자를 공백으로 구분하여 할당
  n, m, k = map(int, input().split())

  # N 개의 수를 공백으로 구분하여 입력
  data = list(map(int, input().split()))
  data.sort()

  first = data[n-1]
  second = data[n-2]

  print("N, M, K -> ",n, m, k)
  print("Input number array -> ", data)
  # print("First -> ", first)
  # print("Second -> ", second)

  bigNumCount = int(m / (k + 1)) * k
  bigNumCount += m % (k + 1) 

  # print("Big number count : ", bigNumCount)

  result = 0
  result += bigNumCount * first
  result += (m - bigNumCount) * second

  print("RESULT => ",result)

def start_1_1():
  # start_1 을 수식이 아닌 프로그래밍 적인 방법으로 풀이한다

  # N,K,M 인자를 공백으로 구분하여 할당
  n, m, k = map(int, input().split())

  # N 개의 수를 공백으로 구분하여 입력
  data = list(map(int, input().split()))
  data.sort()

  print("N, M, K -> ",n, m, k)
  print("Input number array -> ", data)

  first = data[n-1]
  second = data[n-2]

  result = 0
  countLimit = 0

  # 만약 m 이 100억 이상 커진다면 시간초과판정을 받게 된다
  for idx in range(m):
    if countLimit < k :
      result += first
      countLimit += 1
    else :
      result += second
      countLimit = 0
    
  print("RESULT => ",result)


def start_2():
  
  # 시간제한 1초, 메모리제한 128MB

  # 숫자가 쓰인 카드들이 n X m 형태로 놓여있다. ( n : 행, m : 열)
  # 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다
  # 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
  # 따라서 처음에 카드를 골라낼 행을 선택할 때
  # 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을것을 고려하여
  # 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다

  # 3 1 2
  # 4 1 4
  # 2 2 2 
  # 위와 같은 카드배열이 있다면 첫번째 두번째 행의 최소값은 1
  # 세번째 행의 최소값은 2
  # 따라서 세번째 행을 선택해 2를 뽑는것이 정답이다

  # 각 입력값은 공백으로 구분한다
  # 첫째 줄에 카드들이 놓인 행 개수 n 과 열의개수 m 을 입력받는다
  # 1 <= n,m <= 100 
  # 둘째 줄부터 n개의 줄에 걸쳐 각 카드가 적힌 숫자가 주어진다
  # 각 숫자는 1 이상 10,000 이하의 자연수로 주어진다.

  # 출력은 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다


  n, m = map(int, input().split())

  result = 0

  for idx in range(n) :
    rowNum = list(map(int, input().split()))

    # 입력 받은 카드중 가장 작은값 선택
    minValue = min(rowNum)

    # 선택된 작은 값 중 큰값을 선택한다
    result = max(result, minValue)

  print(result)


def start_2_2():
  # start_2 을 2 중 반복문 구조를 사용하여 풀이
  
  n, m = map(int, input().split())

  result = 0

  for idx in range(n) :
    rowNum = list(map(int, input().split()))

    # 입력 받은 카드중 가장 작은값 선택
    minValue = 10001 # 최대값
    for num in rowNum :
      minValue = min(minValue, num)

    # 선택된 작은 값 중 큰값을 선택한다
    result = max(result, minValue)

    print(result)


def start_3():

  # 시간제한 1초, 메모리제한 128MB

  # 어떠한 수 n 이  1이 될 때 까지 다음의 두 과정 중 
  # 하나를 반복적으로 선택하여 수행하려 한다
  # 단 두번째 연산은 n 이 k 로 나누어 떨어질 때만 선택할 수 있다
  #   1. n 에서 1을 뺀다
  #   2. n 을 k 로 나눈다

  # 예를 들어 n 이 17 k 가 4 라고 가정하면
  # 1번의 과정을 한번 수행하면 n은 16이 된다
  # 이후에 2번의 과정을 두번 수행하면 n 은 1이 된다
  # 결과적으로 이 경우 전체과정을 실행한 횟수는 3이 된다.
  # 이는 n 을 1로 만드는 최소 횟수이다

  # 예를들어 n 이 17 k 가 4 이면 1번 과정 후 2번 과정을 두 번 수행

  # n 과 k 가 주어질 때 
  # 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하라

  # 입력은 첫째 줄에 n 과 k 가 공백으로 구분되며 각각 자연수로 주어진다
  # 2 <= n, k <= 100,000
  # n 은 항상 k 보다 크거나 같다

  # n이 1이 될때 까지 1번 혹은 2번의 과정을 수행해야하는
  # 횟수의 최솟값을 출력한다


  n, k = map(int, input().split())
   
  result = 0

  while True:
    
    # n 이 k 로 나누어 떨어지는 수가 될 때 까지 1을 뺀다
    quotient = (n // k) * k
    result += n - quotient
    n = quotient

    # n 을 k로 나눌 수 없으면 반복문 종료
    if n < k : 
      break
    
    # n을 k로 나눈다
    result += 1
    n //= k
    print('N : ',n) 

  print("remainder : ", n)
  
  # 나눌 수 없는 나머지값에 대하여 1씩 뺀다
  result += (n - 1)

  print("result : ", result)
  print("N : ", n )


  