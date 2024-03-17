import sys
import src.parser


if __name__ == "__main__":
    parser = src.parser.Parser(sys.argv[1], sys.argv[2])
    parser.parsing()
    parser.merging_same_day_transactions()
    parser.mark_wash_sales()
    parser.calculate_total_gain()
    parser.calculate_total_gain_in_integer()
    parser.output_csv()

