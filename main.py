import sys
import src.parser


if __name__ == "__main__":
    parser = src.parser.Parser(sys.argv[1], sys.argv[2])
    parser.parsing()
    parser.mark_wash_sales()
    parser.output_csv()

