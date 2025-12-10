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

    def to_int(self):
        return int(str(self))
    
    def clean(self):
        i = 0
        while i < len(self.digits) - 1 and self.digits[i] == 0:
            i += 1

        new_digits = self.digits[i:]

        result = BigNumber("".join(str(d) for d in new_digits))
        result.sign = self.sign
        return result
    
    def split_low(self, half):
        if half >= len(self.digits):
            return BigNumber(str(self))
        low = self.digits[-half:]
        return BigNumber("".join(str(d) for d in low))


    def split_high(self, half):
        if half >= len(self.digits):
            return BigNumber("0")
        high = self.digits[:-half]
        return BigNumber("".join(str(d) for d in high))


    # Sum
    def __add__(self, other):
        a = self.digits[::-1]
        b = other.digits[::-1]
        result = []
        carry = 0
        i = 0 # shomarande arghaam

        while i < len(a) or i < len(b) or carry:
            x = a[i] if i < len(a) else 0 # if not enough digits, initialize 0
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

    # product -1
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

    # product -2 : recursive
    def multiply_recursive(self, other):
        a = self.clean()
        b = other.clean()

        if a.to_int() < 1000 or b.to_int() < 1000:
            return a * b

        # select longest length
        n = max(len(a.digits), len(b.digits))
        half = (n + 1) // 2

        # two parts, up and down
        x1 = a.split_high(half)
        x0 = a.split_low(half)
        y1 = b.split_high(half)
        y0 = b.split_low(half)

        # 3 products recursive
        p1 = x1.multiply_recursive(y1)                    # X₁ × Y₁
        p2 = x0.multiply_recursive(y0)                    # X₀ × Y₀
        p3 = (x0 + x1).multiply_recursive(y0 + y1)         # (X₀+X₁) × (Y₀+Y₁)

        # middle = p3 - p1 - p2
        middle = p3 - p1 - p2

        # جابجایی به توان‌های 10
        shift_2m = BigNumber("1" + "0" * (2 * half))
        shift_m  = BigNumber("1" + "0" * half)

        result = p1 * shift_2m + middle * shift_m + p2

        result.sign = self.sign * other.sign
        return result.clean()
    
    # 4 recursive
    def multiply_recursive(self, other):
        a = self.clean()
        b = other.clean()

        if a.to_int() < 1000 or b.to_int() < 1000:
            return a * b

        n = max(len(a.digits), len(b.digits))
        half = (n + 1) // 2

        # split numbers
        x1 = a.split_high(half)
        x0 = a.split_low(half)
        y1 = b.split_high(half)
        y0 = b.split_low(half)

        z2 = x1.multiply_recursive(y1)      # X₁ * Y₁
        z1 = x1.multiply_recursive(y0)      # X₁ * Y₀
        z0 = x0.multiply_recursive(y1)      # X₀ * Y₁
        z3 = x0.multiply_recursive(y0)      # X₀ * Y₀

        shift_2m = BigNumber("1" + "0" * (2 * half))
        shift_m  = BigNumber("1" + "0" * half)

        result = z2 * shift_2m + (z1 + z0) * shift_m + z3

        result.sign = self.sign * other.sign
        
        return result.clean()

    
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
    
x = BigNumber("12300")
y = BigNumber("15000")

result = x.multiply_recursive(y)
print(result)