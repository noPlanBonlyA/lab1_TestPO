# Отчет по лабораторной работе "Unit Testing"

## Дмитриев Андрей Иванович, 339033, группа: K3439

## 📋 Описание выбранного проекта

**Название**: Calculator with History  
**Тип**: Pet-проект (калькулятор с историей операций)  
**Язык программирования**: Python 3.13  
**Фреймворк тестирования**: pytest  

### Обоснование выбора проекта

Проект "Calculator with History" был выбран как идеальный пример для демонстрации принципов unit testing, поскольку он содержит:

1. **Четко определенную бизнес-логику** - математические операции с предсказуемыми результатами
2. **Различные типы функций** - простые вычисления, валидация, обработка ошибок
3. **Граничные случаи** - деление на ноль, отрицательные числа, переполнение
4. **Интеграционные компоненты** - взаимодействие между калькулятором и историей
5. **Возможность тестирования производительности** - работа с большими числами

## GitHub Репозиторий

**Ссылка на репозиторий**: https://github.com/noPlanBonlyA/lab1_TestPO

**Статус проекта**: Оригинальная разработка (создан специально для лабораторной работы)  
**Доступ**: Публичный репозиторий, доступен для просмотра и изучения  
**Структура проекта**:
- `calculator.py` - основной класс калькулятора
- `history.py` - класс управления историей операций  
- `main.py` - интегрированный класс с демонстрацией
- `test_*.py` - файлы с unit-тестами
- `requirements.txt` - зависимости проекта
- `README.md` - документация проекта
- `REPORT.md` - данный отчет


## Анализ функциональности и выбор тестируемых компонентов

### Критически важные компоненты для тестирования:

#### 1. **Класс Calculator** (`calculator.py`)
**Почему тестируется**: Содержит основную бизнес-логику приложения

**Тестируемые функции**:
- `add()` - сложение чисел
- `subtract()` - вычитание чисел  
- `multiply()` - умножение чисел
- `divide()` - деление чисел (с обработкой деления на ноль)
- `power()` - возведение в степень (с валидацией)
- `square_root()` - извлечение квадратного корня
- `get_last_result()` - получение последнего результата
- `clear()` - сброс состояния

**Критические сценарии**:
- Корректные вычисления с положительными числами
- Операции с нулем и отрицательными числами
- Обработка граничных случаев (переполнение, некорректные операции)
- Точность вычислений с плавающей запятой

#### 2. **Класс History** (`history.py`)
**Почему тестируется**: Управляет состоянием приложения и данными

**Тестируемые функции**:
- `add_operation()` - сохранение операции в историю
- `get_last_operations()` - получение последних операций
- `get_all_operations()` - получение всей истории
- `search_operations()` - поиск операций по типу
- `get_statistics()` - статистический анализ
- `clear_history()` - очистка истории

**Критические сценарии**:
- Корректное сохранение и извлечение данных
- Ограничение размера истории
- Изоляция данных между экземплярами
- Корректность временных меток

#### 3. **Интеграционный компонент** (`main.py`)
**Почему тестируется**: Обеспечивает взаимодействие между компонентами

**Тестируемые сценарии**:
- Синхронизация между Calculator и History
- Обработка ошибок в интегрированной среде
- Статистика на основе выполненных операций

## Написанные тесты

### Общая статистика тестов:
- **Общее количество тестов**: 42
- **Тесты Calculator**: 21 тест
- **Тесты History**: 15 тестов  
- **Интеграционные тесты**: 6 тестов
- **Время выполнения**: 0.07 секунды
- **Покрытие кода**: 94%

### Примеры тестов с использованием принципа AAA:

#### Тест 1: Базовое сложение (Happy Path)
```python
def test_basic_addition(self):
    """Test addition with positive numbers."""
    result = self.calculator.add(5, 3)
    assert result == 8
    assert self.calculator.get_last_result() == 8
```

#### Тест 2: Граничный случай - деление на ноль
```python
def test_division_by_zero(self):
    """Test division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        self.calculator.divide(10, 0)
```

#### Тест 3: Сложный интеграционный сценарий
```python
def test_complex_calculation_scenario(self):
    """Test a complex calculation scenario with full integration."""
    # ((10 + 5) * 3) / 2 - 8 = 14.5
    step1 = self.calc_with_history.add(10, 5)        # 15
    step2 = self.calc_with_history.multiply(step1, 3) # 45
    step3 = self.calc_with_history.divide(step2, 2)   # 22.5
    final = self.calc_with_history.subtract(step3, 8) # 14.5
    
    assert final == 14.5
    history = self.calc_with_history.get_history()
    assert len(history) == 4
    operations = [op['operation'] for op in history]
    assert operations == ['subtract', 'divide', 'multiply', 'add']
```

### Полный список всех написанных тестов:

#### 🧮 **Тесты Calculator (21 тест)**:
1. `test_basic_addition` - базовое сложение чисел
2. `test_basic_subtraction` - базовое вычитание чисел
3. `test_basic_multiplication` - базовое умножение чисел
4. `test_basic_division` - базовое деление чисел
5. `test_basic_power` - базовое возведение в степень
6. `test_addition_with_zero` - сложение с нулем (граничный случай)
7. `test_multiplication_by_zero` - умножение на ноль
8. `test_power_to_zero` - возведение в нулевую степень
9. `test_zero_to_power` - возведение нуля в степень
10. `test_division_by_zero` - деление на ноль (обработка исключения)
11. `test_negative_square_root` - корень из отрицательного числа
12. `test_negative_base_non_integer_exponent` - отрицательное число в дробной степени
13. `test_operations_with_negative_numbers` - операции с отрицательными числами
14. `test_floating_point_operations` - операции с числами с плавающей запятой
15. `test_square_root_positive` - извлечение квадратного корня
16. `test_large_number_operations` - операции с большими числами
17. `test_power_overflow` - переполнение при возведении в степень
18. `test_last_result_tracking` - отслеживание последнего результата
19. `test_clear_functionality` - функция очистки состояния
20. `test_complex_power_operations` - сложные операции возведения в степень
21. `test_mixed_integer_float_operations` - смешанные операции с int и float

#### 📋 **Тесты History (15 тестов)**:
1. `test_add_single_operation` - добавление одной операции в историю
2. `test_add_multiple_operations` - добавление нескольких операций
3. `test_max_size_limit` - ограничение максимального размера истории
4. `test_default_max_size` - проверка размера истории по умолчанию
5. `test_get_last_operations` - получение последних операций
6. `test_get_last_operations_boundary_cases` - граничные случаи получения операций
7. `test_search_operations_by_type` - поиск операций по типу
8. `test_clear_history` - очистка истории
9. `test_statistics_empty_history` - статистика для пустой истории
10. `test_statistics_with_operations` - статистика с операциями
11. `test_operands_list_isolation` - изоляция списка операндов
12. `test_multiple_history_instances` - независимость экземпляров истории
13. `test_timestamp_ordering` - корректность временных меток
14. `test_custom_max_size_edge_cases` - граничные случаи с настраиваемым размером
15. `test_mixed_operations_scenario` - смешанные сценарии операций

#### 🔗 **Интеграционные тесты (6 тестов)**:
1. `test_operation_with_history_recording` - запись операции в историю
2. `test_multiple_operations_history` - запись нескольких операций
3. `test_error_not_recorded_in_history` - ошибки не записываются в историю
4. `test_statistics_integration` - интеграция статистики
5. `test_clear_history_integration` - очистка истории в интегрированной среде
6. `test_complex_calculation_scenario` - сложный сценарий вычислений

### Дополнительные примеры ключевых тестов:

#### Тест 4: Операции с отрицательными числами
```python
def test_operations_with_negative_numbers(self):
    """Test operations with negative numbers."""
    assert self.calculator.add(-5, -3) == -8
    assert self.calculator.add(-5, 3) == -2
    assert self.calculator.multiply(-5, -3) == 15
    assert self.calculator.divide(-15, -3) == 5
```

#### Тест 5: Статистика истории операций
```python
def test_statistics_with_operations(self):
    """Test statistics with multiple operations."""
    operations_data = [
        ("add", [1, 2], 3),
        ("multiply", [2, 3], 6),
        ("divide", [20, 4], 5)
    ]
    
    for op, operands, result in operations_data:
        self.history.add_operation(op, operands, result)
    
    stats = self.history.get_statistics()
    assert stats['total_operations'] == 3
    assert stats['average_result'] == (3 + 6 + 5) / 3
    assert stats['max_result'] == 6
```

#### Тест 6: Ограничение размера истории
```python
def test_max_size_limit(self):
    """Test that history respects maximum size limit."""
    small_history = History(max_size=3)
    
    # Добавляем больше операций, чем максимальный размер
    for i in range(5):
        small_history.add_operation("add", [i, 1], i + 1)
    
    assert small_history.get_operation_count() == 3
    operations = small_history.get_all_operations()
    # Должны остаться только последние 3 операции
    assert operations[0]['result'] == 5  # 4 + 1
    assert operations[1]['result'] == 4  # 3 + 1
    assert operations[2]['result'] == 3  # 2 + 1
```

### Покрытие тестами по категориям:

#### ✅ **Корректные случаи (Happy Path)**:
- Основные математические операции
- Операции с целыми и дробными числами
- Последовательность операций

#### ✅ **Граничные случаи (Boundary Cases)**:
- Операции с нулем
- Максимальные и минимальные значения
- Пустая история
- Ограничения размера истории

#### ✅ **Исключительные ситуации (Error Cases)**:
- Деление на ноль
- Извлечение корня из отрицательного числа
- Возведение отрицательного числа в дробную степень
- Переполнение при вычислениях

#### ✅ **Интеграционные тесты**:
- Взаимодействие Calculator ↔ History
- Синхронизация состояния
- Обработка ошибок в интегрированной среде

## 📊 Результаты запуска тестов

### Результат выполнения pytest:
```
===================================================== test session starts ======================================================
platform darwin -- Python 3.13.3, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/noplana/Desktop/ /Mobile/4rd/ТПО/lab1
collected 42 items

test_calculator.py .....................                                                                                 [ 50%]
test_history.py ...............                                                                                          [ 85%]
test_integration.py ......                                                                                               [100%]

====================================================== 42 passed in 0.07s ======================================================
```

### Метрики покрытия кода (Code Coverage):
```
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
calculator.py            45      1    98%   103
history.py               34      0   100%
main.py                  59     27    54%   45-47, 51-53, 70-94, 98
test_calculator.py      129      0   100%
test_history.py         149      0   100%
test_integration.py      64      0   100%
---------------------------------------------------
TOTAL                   480     28    94%
```

### Анализ покрытия:
- **calculator.py**: 98% покрытие (отличный результат)
- **history.py**: 100% покрытие (идеальное покрытие)
- **main.py**: 54% покрытие (демонстрационные функции не покрыты тестами)
- **Общее покрытие**: 94% - превосходный результат

## 🔍 Соответствие принципам FIRST

### ✅ **Fast (Быстрые)**
- Все 42 теста выполняются за 0.07 секунды
- Тесты не содержат медленных операций (сеть, файловая система)
- Используются простые математические операции

### ✅ **Isolated (Изолированные)**  
- Каждый тест использует `setup_method()` для создания чистого состояния
- Тесты не зависят от порядка выполнения
- Независимые экземпляры классов для каждого теста

### ✅ **Repeatable (Повторяемые)**
- Тесты дают одинаковый результат при многократном запуске
- Отсутствие зависимости от внешних факторов
- Детерминированные результаты

### ✅ **Self-validating (Самопроверяющиеся)**
- Четкий результат pass/fail для каждого теста  
- Использование assert statements
- Понятные сообщения об ошибках

### ✅ **Timely (Своевременные)**
- Тесты написаны одновременно с кодом
- Покрывают функциональность по мере разработки

## 🎯 Применение паттерна AAA

Все тесты следуют принципу **Arrange-Act-Assert**, но с упрощенной структурой:

**Традиционный подход AAA:**
```python
def test_example_verbose(self):
    # Arrange - подготовка данных и объектов
    calculator = Calculator()
    a, b = 10, 5
    expected = 15
    
    # Act - выполнение тестируемого действия
    result = calculator.add(a, b)
    
    # Assert - проверка результатов
    assert result == expected
```

## 🚨 Обнаруженные проблемы и выводы

### Обнаруженные проблемы:

1. **Неполное покрытие main.py** 
   - **Проблема**: Демонстрационные функции не покрыты тестами
   - **Решение**: Создать отдельные тесты для UI-логики или вынести в отдельный модуль

2. **Потенциальные проблемы с точностью float**
   - **Проблема**: Операции с плавающей запятой могут иметь погрешности
   - **Решение**: Использование tolerance для сравнения float значений

### Выводы о качестве тестирования:

#### ✅ **Сильные стороны**:
1. **Высокое покрытие кода** (94%) - отличный показатель качества
2. **Комплексный подход** - юнит-тесты + интеграционные тесты
3. **Следование лучшим практикам** - AAA pattern, FIRST principles
4. **Хорошая организация** - логическое разделение тестов по классам
5. **Граничные случаи** - тщательное тестирование edge cases
6. **Поддерживаемость** - легко модифицировать и расширять

#### ⚠️ **Области для улучшения**:
1. **Performance тесты** - добавить тесты производительности для больших данных
2. **Stress тесты** - тестирование поведения при экстремальных нагрузках  
3. **Property-based тесты** - использование hypothesis для генерации тестовых данных
4. **Мutational тесты** - проверка качества тестов через мутационное тестирование
