import argparse
import logging

from pysort.mergesort import mergesort
from pysort.quicksort import quicksort


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("array", type=str)
    parser.add_argument("algo")
    parser.add_argument("verbose", type=int)
    args = parser.parse_args(argv)

    if args.verbose == 2:
        logging.basicConfig(
            format="%(asctime)s %(levelname)-8s-> %(message)s", level=logging.DEBUG
        )
        logging.info("Verbose output.")
    if args.verbose == 1:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

    if args.algo == "quicksort":

        result_array = quicksort(list(map(int, args.array.split(","))))

        print(f"Sorted array: {result_array}")
    if args.algo == "mergesort":

        result_array = mergesort(list(map(int, args.array.split(","))))

        print(f"Sorted array: {result_array}")


if __name__ == "__main__":
    SystemExit(main())
