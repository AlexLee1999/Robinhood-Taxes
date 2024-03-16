import sys
import pandas
import src.parser as parser


if __name__ == "__main__":
    table = parser.parsing(sys.argv[1])
    print(table)

