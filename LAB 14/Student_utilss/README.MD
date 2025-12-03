# student_utils Package

This package contains math and string utility functions, as well as helper
functions for message formatting.

## Example usage

```python
from student_utils import add, to_upper
from student_utils.helpers import prefix_message

print(add(5, 10))
print(to_upper("hello"))
print(prefix_message("Task completed"))



## 3. (Опционально) добавить функции для индивидуального задания
Добавь одну math-функцию (например, `median`), одну string-функцию (`reverse_string`) и helper (`suffix_message`).

Открой `student_utils/math_tools.py` и допиши:
```python
def median(numbers):
    s = sorted(numbers)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid-1] + s[mid]) / 2
