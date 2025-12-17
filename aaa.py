import math

def f(x):
    """Функция x^2 - sin(x) - 1 = 0"""
    return x**2 - math.sin(x) - 1

def bisection_method(a, b, iterations):
    """
    Метод половинного деления (дихотомии)
    
    Параметры:
    a, b - границы интервала [1, 2]
    iterations - количество итераций
    
    Возвращает:
    приближенное значение корня
    """
    # Проверка, что функция меняет знак на концах интервала
    if f(a) * f(b) >= 0:
        return "На интервале [a, b] функция должна иметь разные знаки"
    
    for i in range(1, iterations + 1):
        # Находим середину интервала
        c = (a + b) / 2
        
        # Выводим информацию о текущей итерации
        print(f"Итерация {i}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {f(c):.6f}")
        
        # Определяем, в какой половине находится корень
        if f(a) * f(c) < 0:
            b = c  # корень в левой половине
        else:
            a = c  # корень в правой половине
    
    # Возвращаем среднее значение последнего интервала
    root = (a + b) / 2
    return root

def main():
    print("МЕТОД ПОЛОВИННОГО ДЕЛЕНИЯ (ДИХОТОМИИ)")
    print("=" * 50)
    print("Решение уравнения: x^2 - sin(x) - 1 = 0")
    print("Интервал: [1, 2]")
    print("=" * 50)
    
    # Ввод количества итераций
    try:
        iterations = int(input("Введите количество итераций: "))
        
        if iterations <= 0:
            print("Количество итераций должно быть положительным числом!")
            return
        
        # Заданные параметры
        a = 1.0
        b = 2.0
        
        print(f"\nНачальные значения:")
        print(f"a = {a}, f(a) = {f(a):.6f}")
        print(f"b = {b}, f(b) = {f(b):.6f}")
        print(f"f(a)*f(b) = {f(a)*f(b):.6f}")
        
        if f(a) * f(b) >= 0:
            print("\nВНИМАНИЕ: f(a)*f(b) >= 0, метод может не работать!")
            print("Но продолжим вычисления...")
        
        print("\n" + "=" * 50)
        print("Процесс вычислений:")
        print("=" * 50)
        
        # Выполнение метода
        result = bisection_method(a, b, iterations)
        
        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТ:")
        print("=" * 50)
        
        if isinstance(result, str):
            print(result)
        else:
            print(f"Приближенный корень: {result:.10f}")
            print(f"Значение функции: f({result:.6f}) = {f(result):.10e}")
            print(f"Количество итераций: {iterations}")
    
    except ValueError:
        print("Ошибка! Введите целое число итераций.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
