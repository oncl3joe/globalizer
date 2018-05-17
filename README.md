# Python Globalizer Object

```python
from globalizer import globalizer

globalizer.my_name = {"a" : 1}

value = globalizer.my_name["a"]

del globalizer.my_name

globalizer.my_name1.my_name2.my_name3 = "test"

print(globalizer.my_name1.my_name2.my_name3)
```
