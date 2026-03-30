import re

class Calculator:
    def __init__(self):
        self.elem1 = 0
        self.elem2 = 0
        self.calculator = ""
        self.validation_result = 0
        
    def get_data(self):
        data = input()
        result = self.validate_input(data)
        if result == 0 :
            return self.get_data()
        elif result == 1:
            data = data.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ")
            splitted_data = data.split()
            self.elem1 = int(splitted_data[0])
            self.calculator = splitted_data[1]
            self.elem2 = int(splitted_data[2])
        elif result == 2:
            data = data.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ")
            splitted_data = data.split()
            self.calculator = splitted_data[0]
            self.elem2 = int(splitted_data[1])
        elif result == "q":
            print("프로그램을 종료합니다.")
            return "q"
        else :
            print("알 수 없는 오류가 발생했습니다.")
            return self.get_data()

    def validate_input(self, data):
        if not re.match("^\d+\s*[+\-*/]\s*\d+$", data) and not re.match("^[+\-*/]\s*\d+$", data):
            print("잘못된 입력 형식입니다. 입력 형식은 '숫자 연산자 숫자' 또는 '연산자 숫자'이어야 합니다. 다시 입력해주세요.")
            return 0
        elif re.match("^\d+\s*[+\-*/]\s*\d+$", data):
            return 1
        elif re.match("^[+\-*/]\s*\d+$", data):
            return 2
        elif data == 'q':
            print("프로그램을 종료합니다.")
            return "q"
        else :
            print("알 수 없는 오류가 발생했습니다. 다시 입력해주세요.")
            return 0
    
    def calculate(self):
        result = 0
        if self.calculator == "+":
            result = self.elem1 + self.elem2
        elif self.calculator == "-":
            result = self.elem1 - self.elem2
        elif self.calculator == "*":
            result = self.elem1 * self.elem2
        elif self.calculator == "/":
            if self.elem2 != 0:
                print("0으로 나눌 수 없습니다.")
                return self.get_data()
            result = self.elem1 / self.elem2
        else :
            print("잘못된 연산자입니다.")
            return self.get_data()
        print("계산 결과:", result)
        self.elem1 = result
        return result
1+3
calc = Calculator()
while True:
    calc.get_data()
    if calc.calculate() == "q":
        print("프로그램을 종료합니다.")
        break
