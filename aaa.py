import math

class Value:
    def __init__(self, val, err=0.0):
        self.val, self.err = float(val), float(err)

    def __str__(self): return f"{self.val} ± {self.err}"
    def add(self, а): return Value(self.val + a.val, self.err + a.err)
    def sub(self, a): return Value(self.val - a.val, self.err + a.err)
    def mul(self, a): return Value(self.val * a.val, abs(self.val) * a.err + abs(a.val) * self.err)
    def div(self, a): return Value(self.val / a.val, (abs(a.val) * self.err + abs(self.val) * a.err) / (a.val ** 2))
    def power(self, n): return Value(self.val ** n, abs(n * self.val ** (n - 1) * self.err))
    def sqrt(self): return Value(math.sqrt(self.val), self.err / (2 * math.sqrt(self.val)))

print(
    "Калькулятор с абсолютной погрешностью\nФормат числа: значение погрешность  (пример: 10 0.2)\nКоманды: +  -  *  /  ^  sqrt  exit\n")

current = None

while True:
    if not current:
        v, e = map(float, input("Введите число и погрешность: ").split())
        current = Value(v, e)
        print("Текущее значение:", current)
        continue

    cmd = input("\nОперация (+ - * / ^ sqrt exit): ").strip()
    if cmd == "exit": break
    if cmd == "sqrt":
        current = current.sqrt()
        print("Результат:", current)
        continue
    if cmd == "^":
        current = current.power(float(input("Введите степень: ")))
        print("Результат:", current)
        continue

    v, e = map(float, input("Введите второе число и погрешность: ").split())
    a = Value(v, e)

    ops = {"+": current.add, "-": current.sub, "*": current.mul, "/": current.div}
    if cmd in ops:
        current = ops[cmd](a)
        print("Результат:", current)
    else:
        print("Неизвестная операция")
