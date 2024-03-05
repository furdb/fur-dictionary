import converter
from config import *


def main():
    word = "anomaly"

    encoded = converter.encode(word)
    decoded = converter.decode(encoded, WORD_SIZE)

    print(word, encoded, decoded)


if __name__ == "__main__":
    main()