#-*- coding: utf-8 -*-
from lib import schedule_parser, file_reader



def main():
    file_path = "input_data/input.inc"
    data = file_reader.read_file(file_path)
    result_data = schedule_parser.parse_schedule(data)
    schedule_parser.result_to_csv(result_data)
    print("output.csv записан и лежит в папке output_data")

if __name__ == "__main__":
    main()





