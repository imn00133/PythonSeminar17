class LongFloat:
    """
    소수부분을 정수로 저장하여 정확한 소수계산을 하도록 만드는 class
    나눗셈에서는 출력할 소수 자리수를 받아온다.
    초기화시, string을 입력받는다.
    둘 다 양수일 때만 작동한다.
    값을 전부 가지게 만드는 함수가 필요하다.
    """
    def __init__(self, num="0.0"):
        # 초기화, 정수부, 소수부가 없을 때도 만들어줌
        if num.find('.') > 0:
            self.integer = num[0:num.find('.')]
            self.decimal = num[num.find('.')+1:]
        elif num.find('.') == 0:
            self.integer = "0"
            self.decimal = num[1:]
        else:
            self.integer = num
            self.decimal = "0"

    def __add__(self, other):
        rt_float = LongFloat
        # 정수끼리 덧셈
        rt_float.integer = str(int(self.integer)+int(other.integer))
        # 소수 자리수 맞추기
        if len(self.decimal) > len(other.decimal):
            for i in range(len(self.decimal)-len(other.decimal)):
                other.decimal += "0"
        else:
            for i in range(len(other.decimal)-len(self.decimal)):
                self.decimal += "0"
        rt_float.decimal = str(int(self.decimal)+int(other.decimal))
        # 자리수 올림
        if len(rt_float.decimal) != len(other.decimal):
            rt_float.integer = str(int(rt_float.integer)+1)
            rt_float.decimal = rt_float.decimal[1:]
        return self

    def __sub__(self, other):
        pass

    def __truediv__(self, other):
        rt_float = LongFloat()
        deci_pt = int(input("소수 몇 번째 자리까지 나누시겠습니까?: "))
        val_self = int(self.integer+self.decimal)
        val_other = int(other.integer+other.decimal)
        # 소수점 자리수 맞추기
        if len(self.decimal) >= len(other.decimal):
            for i in range(len(self.decimal)-len(other.decimal)):
                val_other *= 10
        else:
            for i in range(len(other.decimal)-len(self.decimal)):
                val_self *= 10
        # 정수부 계산
        rt_float.integer = str(val_self // val_other)
        val_self = val_self % val_other
        # 소수부 계산
        rt_float.decimal = ""
        for i in range(deci_pt):
            val_self *= 10
            rt_float.decimal += str(val_self // val_other)
            val_self = val_self % val_other
            # 다 나눠지면 종료
            if val_self == 0:
                break
        val_self *= 10
        # 마지막 반올림
        if val_self // val_other >= 5:
            rt_float.decimal = str(int(rt_float.decimal)+1)
        return rt_float

    def __mul__(self, other):
        rt_float = LongFloat()
        deci_pt = len(self.decimal)+len(other.decimal)
        val_self = int(self.integer+self.decimal)
        val_other = int(other.integer+other.decimal)
        total = str(val_self * val_other)
        rt_float.integer = total[0:len(total)-deci_pt]
        rt_float.decimal = total[len(total)-deci_pt:]
        return rt_float

    def __str__(self):
        return "%s.%s" % (self.integer, self.decimal)


a = LongFloat(input("첫 번째 수를 입력하세요 :"))
b = LongFloat(input("두 번째 수를 입력하세요 :"))
c = a / b
print(c)
print(a)