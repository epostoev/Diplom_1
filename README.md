# Diplom_1 — Юнит-тесты для Stellar Burgers

Юнит-тесты для системы заказа бургеров Stellar Burgers.  
Покрыты классы `Bun`, `Ingredient`, `Burger`, `Database`.

## Список реализованных тестов

### 🍞 Булочка (`TestBun`)
Класс тестов, проверяющий модель булочки `Bun`.

| Тест | Описание |
|:---|:---|
| `test_get_name` | **Параметризованный тест (3 кейса):** Проверяет, что метод `get_name()` возвращает корректное название булочки. |
| `test_get_price` | **Параметризованный тест (3 кейса):** Проверяет, что метод `get_price()` возвращает корректную цену булочки. |

### 🥩 Ингредиент (`TestIngredient`)
Класс тестов, проверяющий модель ингредиента `Ingredient`.

| Тест | Описание |
|:---|:---|
| `test_get_name` | **Параметризованный тест (4 кейса):** Проверяет, что метод `get_name()` возвращает корректное название ингредиента. |
| `test_get_price` | **Параметризованный тест (4 кейса):** Проверяет, что метод `get_price()` возвращает корректную цену ингредиента. |
| `test_get_type` | **Параметризованный тест (4 кейса):** Проверяет, что метод `get_type()` возвращает корректный тип ингредиента (`SAUCE` или `FILLING`). |

### 🍔 Бургер (`TestBurger`)
Класс тестов, проверяющий модель бургера `Burger`. `Bun` и `Ingredient` замокированы.

| Тест | Описание |
|:---|:---|
| `test_set_buns` | **Параметризованный тест (3 кейса):** Проверяет, что метод `set_buns()` корректно устанавливает булочку в бургер. |
| `test_add_ingredient` | **Параметризованный тест (4 кейса):** Проверяет, что метод `add_ingredient()` добавляет ингредиент в список. |
| `test_remove_ingredient` | Проверяет, что метод `remove_ingredient()` удаляет ингредиент по индексу. |
| `test_move_ingredient` | Проверяет, что метод `move_ingredient()` корректно перемещает ингредиент на новую позицию. |
| `test_get_price` | **Параметризованный тест (3 кейса):** Проверяет расчёт цены бургера по формуле `bun * 2 + ингредиенты`. |
| `test_get_receipt` | **Параметризованный тест (3 кейса):** Проверяет, что метод `get_receipt()` формирует корректный чек бургера. |

### 🗄 База данных (`TestDatabase`)
Класс тестов, проверяющий класс `Database`.

| Тест | Описание |
|:---|:---|
| `test_available_buns_returns_list` | Проверяет, что метод `available_buns()` возвращает список. |
| `test_available_buns_not_empty` | Проверяет, что список булочек не пустой. |
| `test_available_buns_contains_bun_instances` | Проверяет, что все элементы списка булочек являются экземплярами класса `Bun`. |
| `test_available_ingredients_returns_list` | Проверяет, что метод `available_ingredients()` возвращает список. |
| `test_available_ingredients_not_empty` | Проверяет, что список ингредиентов не пустой. |
| `test_available_ingredients_contains_ingredient_instances` | Проверяет, что все элементы списка ингредиентов являются экземплярами класса `Ingredient`. |

---

## 🛠 Технические особенности реализации

* **Моки (`unittest.mock.Mock`)** — в `test_burger.py` объекты `Bun` и `Ingredient` замокированы через фикстуры `mock_bun`, `mock_sauce`, `mock_filling` и `mock_ingredient`. Это позволяет тестировать логику `Burger` в изоляции от реальных реализаций зависимых классов.
* **Параметризация** — используется в `test_bun.py`, `test_ingredient.py` и `test_burger.py` через `@pytest.mark.parametrize`. Тестовые данные вынесены в классы `BunData`, `IngredientData` и `ResultTest` в `data.py`.
* **Фикстуры** — `mock_bun` и `mock_ingredient` параметризованы через `@pytest.fixture(params=...)` в `conftest.py`. Это позволяет автоматически прогонять тесты для всех наборов данных без дублирования кода.
* **Паттерн AAA** — каждый тест разделён на блоки Arrange, Act, Assert.
* **Независимость тестов** — каждый тест создаёт свой объект через `setup_method`, без общего состояния между тестами.

---

## 🚀 Запуск проекта

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск тестов
```bash
pytest -v
```

### Запуск с отчётом о покрытии
```bash
pytest --cov=praktikum --cov-report=term-missing
```

---

## 📊 Покрытие тестами

```
Name                            Stmts   Miss  Cover
-----------------------------------------------------
praktikum/__init__.py               0      0   100%
praktikum/bun.py                    8      0   100%
praktikum/burger.py                27      0   100%
praktikum/database.py              21      0   100%
praktikum/ingredient.py            11      0   100%
praktikum/ingredient_types.py       2      0   100%
-----------------------------------------------------
TOTAL                              69      0   100%
```

---

## 📁 Структура проекта

```
Diplom_1/
├── praktikum/
│   ├── __init__.py
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   ├── ingredient_types.py
│   └── praktikum.py
├── tests/
│   ├── __init__.py
│   ├── test_bun.py
│   ├── test_burger.py
│   ├── test_database.py
│   └── test_ingredient.py
├── .coveragerc
├── conftest.py
├── data.py
├── requirements.txt
└── README.md
```