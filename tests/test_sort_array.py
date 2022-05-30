import sys
import random

from sort_array import main


def test_quicksort(capsys):
    a = random.sample(range(1, 1000), 100)
    array = ",".join([str(i) for i in a])
    a.sort()

    sys.argv = ["sort_array.py", array, "quicksort", "1"]
    main()

    out, err = capsys.readouterr()
    assert f"Sorted array: {a}\n" in out in out
    assert err == ""


def test_mergesort(capsys):
    a = random.sample(range(1, 1000), 100)
    array = ",".join([str(i) for i in a])
    a.sort()

    sys.argv = ["sort_array.py", array, "mergesort", "1"]
    main()

    out, err = capsys.readouterr()
    assert f"Sorted array: {a}\n" in out
    assert err == ""
