#1000
# A, B = map(int, input().split())
# #split() 의미 : 빈칸을 기준으로 나눔
# #각각의 요소들을 map 함수를 통해 int로 바꾸어줌!
# print(A+B)

#2558
# A = int(input())
# B = int(input())
# print(A+B)

#10950
# testCase = int(input())
# i = 0
# while i < testCase:
#   A, B = map(int, input().split())
#   print(A+B)

#10951
# while 1:
#   try:   
#     A, B = map(int, input().split())
#     print(A+B)
#   except:  #런타임 오류 피하기 위해
#     break

#10952
# while 1:    #무한 루프를 돌려줘야하니까
#   a, b = map(int, input().split())
#   if a == 0 and b == 0:
#     break
#   print(a+b)  

#10953
# testCase = int(input())
# i=0
# while i<testCase:
#   try:
#     a, b = map(int, input().split(','))
#     print(a+b)
#   except:
#     break

#11021
# testCase = int(input())
# for i in range(1, testCase+1):
#   a, b = map(int, input().split())
#   print("Case #"+str(i)+':',a+b)
#궁금 : print()에서 +와 ,의 차이!! -> +은 공백 없이 출력되고 ,는 공백있게 출력됨


#11022
# testCase = int(input())
# for i in range(1, testCase+1):
#   a,b = map(int, input().split())
#   print("Case #"+str(i)+":",str(a),'+',str(b),'=',str(a+b))

#11718
# while 1:
#   try:
#     print(input())    #입력값을 그대로 출력해준다
#   except EOFError:    #입력값이 안들어온다면(End Of File 상태)
#     break
  
#11719
#빈줄, 줄의 앞뒤 공백 가능
# while 1:
#   try:
#     print(input())
#   except EOFError:
#     break

#11720

