# 사용자로부터 두 정수 입력받기
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

# 합, 차, 곱셈, 나눗셈 계산
sum_result = num1 + num2
difference_result = num1 - num2
multiplication_result = num1 * num2
division_result = num1 / num2 if num2 != 0 else "0으로 나눌 수 없습니다"

# 결과 출력
print(f"두 정수의 합: {sum_result}")
print(f"두 정수의 차: {difference_result}")
print(f"두 정수의 곱: {multiplication_result}")
print(f"두 정수의 나눗셈: {division_result}")
print("hello1")