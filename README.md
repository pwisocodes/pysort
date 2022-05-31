# Sorting Algortihms 

- Quicksort
- Mergesort



# How to use?

```bash
usage: sort_array.py [-h] array algo verbose
positional arguments:
  array
  algo
  verbose

optional arguments:
  -h, --help  show this help message and exit
```
# Example

```bash
$ python3 sort_array.py 60,8,20,5,94,13,7,3,4 mergesort 1
```

# Using as Library

```python
import random
from sort_array import main

if __name__ == "__main__":
    a = random.sample(range(1, 1000), 100)
    array = ",".join([str(i) for i in a])
    main([array, "quicksort", "1"])
```