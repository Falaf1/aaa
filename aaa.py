import math

class Value:
    def __init__(self, val, err=0.0):
        self.val, self.err = float(val), float(err)

    def __str__(self): return f"{self.val} ± {self.err}"
    def add(self, o): return Value(self.val + o.val, self.err + o.err)
    def sub(self, o): return Value(self.val - o.val, self.err + o.err)
    def mul(self, o): return Value(self.val * o.val, abs(self.val) * o.err + abs(o.val) * self.err)
    def div(self, o): return Value(self.val / o.val, (abs(o.val) * self.err + abs(self.val) * o.err) / (o.val ** 2))
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
    o = Value(v, e)

    ops = {"+": current.add, "-": current.sub, "*": current.mul, "/": current.div}
    if cmd in ops:
        current = ops[cmd](o)
        print("Результат:", current)
    else:
        print("Неизвестная операция")

