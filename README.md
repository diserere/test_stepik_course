# ООП Python: Часть 2
### Практические занятия к курсу образовательной платформы Stepik

[![Python tests](https://github.com/diserere/test_stepik_course/actions/workflows/python-test.yml/badge.svg)](https://github.com/diserere/test_stepik_course/actions/workflows/python-test.yml)

Этот репозиторий содержит набор кода и тестов к нему из практических заданий по материалам курса [**ООП Python: Часть 2**](https://stepik.org/course/259051) на платформе [**Stepik**](https://stepik.org).


## Программа курса

1. **Магические методы и свойства**
   - 1.1 Введение: От фундамента к мастерству
   - 1.2 Как получить помощь? Связь с автором.
   - [1.3 Строковое представление: `__str__` и `__repr__`](./oop_python_part_2/s_1_magic_methods_and_properties/test_ch_1_3_str_repr.py)
   - [1.4 Перегрузка операторов](./oop_python_part_2/s_1_magic_methods_and_properties/test_ch_1_4_operator_overloading.py)
   - [1.5 Свойства (@property): элегантная инкапсуляция](./oop_python_part_2/s_1_magic_methods_and_properties/test_ch_1_5_properties.py)
   - [1.6 `__slots__`: Оптимизация памяти и производительности](./oop_python_part_2/s_1_magic_methods_and_properties/test_ch_1_6_slots.py)
2. **Продвинутые методы и управление классом**
   - [2.1 Методы класса (@classmethod)](./oop_python_part_2/s_2_advanced_methods/test_ch_2_1_classmethods.py)
   - [2.2 Статические методы (@staticmethod)](./oop_python_part_2/s_2_advanced_methods/test_ch_2_2_staticmethods.py)
3. **Архитектура и отношения между классами**
   - [3.1 Композиция вместо наследования](./oop_python_part_2/s_3_architecture_and_relations/test_ch_3_1_composition.py)
   - [3.2 Множественное наследование и Миксины](./oop_python_part_2/s_3_architecture_and_relations/test_ch_3_2_multiple_inheritance_mixins.py)
4. **Современные инструменты ООП в Python**
   - [4.1 Абстрактные базовые классы (ABC)](./oop_python_part_2/s_4_modern_oop_tools/test_ch_4_1_abc.py)
   - [4.2 Датаклассы (@dataclass)](./oop_python_part_2/s_4_modern_oop_tools/test_ch_4_2_dataclasses.py)
   - [4.3 Дескрипторы: `__get__`, `__set__`, `__delete__`](./oop_python_part_2/s_4_modern_oop_tools/test_ch_4_3_descriptors.py)
5. **Финальный проект и заключение**
   - [5.1 Создание собственных исключений](./oop_python_part_2/s_5_final_project_and_conclusion/test_ch_5_1_custom_exceptions.py)
   - [5.2 Финальные задачи](./oop_python_part_2/s_5_final_project_and_conclusion/test_ch_5_2_final_tasks.py)

## О проекте
Тесты написаны для автоматической проверки синтаксиса, корректности структуры классов и логики взаимодействия объектов, создаваемых в рамках обучения. В проекте используется инструментарий:
- **Pytest** — для запуска тестов.
- **Ruff** — для мгновенной проверки чистоты кода (Linter).
- **GitHub Actions** — настроен автоматический запуск тестов на пулл-реквестах в `master`.

## Как запустить локально

Для запуска тестов рекомендуется использовать виртуальное окружение (`virtualenv`), чтобы избежать конфликтов зависимостей.

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/diserere/test_stepik_course.git
   cd test_stepik_course
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   # Для Windows:
   source venv/Scripts/activate
   # Для macOS/Linux:
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите проверку кода и тесты:
   ```bash
   # Проверка линтером Ruff
   ruff check .
   # Запуск тестов
   pytest
   ```
   
## Настройки (pyproject.toml)
В проекте настроены специфические параметры:
* **ruff**
  * Максимальная длина строки: 120 символов.
  * Целевая версия Python: 3.13.
* **pytest**
  * ключи запуска: `-vsrA`
  * дефолтный путь для поиска тестов: `["oop_python_part_1", "oop_python_part_2"]`

## Благодарности

*   **Образовательной платформе [Stepik](https://stepik.org/learn)** — за удобную среду для обучения и роста.
*   **Автору курса** — [Александру Заплавному](https://stepik.org/users/554816359). Спасибо за глубокую подачу материала! Следить за новостями автора можно в его Telegram-канале: [Коммунист](https://t.me/+LG2cdbcirMA1Y2Ji).
*   **Сообществу Linux** — за философию открытого кода и прекрачные инструменты.
*   **Искусственному интеллекту** — небиологическому другу и верному ассистенту 🦆, который помог мне настроить CI-пайплайн, оптимизировать Ruff и оформить документацию, чтобы автор мог сфокусироваться на том, что ему нравится — изучении ООП 🤖🐍 \*

---

\* это ИИ, который и помогал мне написать это README, добавил такие смайлики в конце, и, честно говоря, я не очень понимаю, что это за пасхалка, так что я просто оставлю их здесь в его честь.

