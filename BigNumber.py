class BigNumber:
    
    def __init__(self, s):
        if s.startswith('-'):
            self.sign = -1
            s = s[1:]
        else:
            self.sign = 1
        self.digits = [int(d) for d in s]
        
        if not self.digits:
            self.digits = [0]

    def __str__(self):
        if not self.digits:
            return "0"
        sign = "-" if self.sign == -1 else ""
        return sign + "".join(map(str, self.digits))

    # Sum
    def __add__(self, other):
        a = self.digits[::-1]
        b = other.digits[::-1]
        result = []
        carry = 0
        i = 0

        while i < len(a) or i < len(b) or carry:
            x = a[i] if i < len(a) else 0
            y = b[i] if i < len(b) else 0
            total = x + y + carry
            result.append(total % 10)
            carry = total // 10
            i += 1

        sign = 1
        if self.sign == -1 and other.sign == -1:
            sign = -1
        elif self.sign == -1:
            return other - (-self)
        elif other.sign == -1:
            return self - (-other)

        return BigNumber("".join(map(str, result[::-1])) if sign == 1 else "-" + "".join(map(str, result[::-1])))

    #  -
    def __sub__(self, other):
        # فقط حالت |self| >= |other| رو مستقیم بقیه رو تبدیل به جمع
        if self.sign == -1 and other.sign == 1:
            return -( (-self) + other )
        if self.sign == 1 and other.sign == -1:
            return self + (-other)
        if self.sign == -1 and other.sign == -1:
            return (-other) - (-self)

        if self < other:
            res = other - self
            res.sign = -1
            return res

        a = self.digits[::-1]
        b = other.digits[::-1]
        result = []
        borrow = 0
        i = 0

        while i < len(a) or i < len(b) or borrow:
            x = a[i] if i < len(a) else 0
            y = b[i] if i < len(b) else 0
            diff = x - y - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append(diff)
            i += 1

        # remove 0  
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return BigNumber("".join(map(str, result[::-1])))

    # product
    def __mul__(self, other):
        a = self.digits[::-1]
        b = other.digits[::-1]
        result = [0] * (len(a) + len(b))

        for i in range(len(a)):
            for j in range(len(b)):
                result[i + j] += a[i] * b[j]

        # cary
        for i in range(len(result) - 1):
            if result[i] >= 10:
                result[i + 1] += result[i] // 10
                result[i] %= 10

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        sign = self.sign * other.sign
        res_str = "".join(map(str, result[::-1]))
        return BigNumber(res_str if sign == 1 else "-" + res_str)

    # divide
    def __truediv__(self, other):
        if str(other) == "0":
            return BigNumber("divide by zero")

        dividend = abs(self)
        divisor = abs(other)

        if dividend < divisor:
            return BigNumber("0")

        result = []
        remainder = 0
        for digit in dividend.digits:
            remainder = remainder * 10 + digit
            quotient = 0
            while remainder >= int(str(divisor)):
                remainder -= int(str(divisor))
                quotient += 1
            result.append(quotient)

        # remove first 0
        while len(result) > 1 and result[0] == 0:
            result = result[1:]

        sign = self.sign * other.sign
        res_str = "".join(map(str, result))
        return BigNumber(res_str if sign == 1 else "-" + res_str)