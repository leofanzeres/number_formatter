import csv

class NumberFormatter:
    def __init__(self, numbers_dict_csv):
        self.numbers_dict_csv = numbers_dict_csv

    def load_dictionary(self):
        reader = csv.reader(open(self.numbers_dict_csv, mode='r'), delimiter=',')
        numbers_dict = {}
        for row in reader:
            numbers_dict[row[1]] = row[0]
        return numbers_dict

    def format_numbers(self, text):
        with open(text) as f:
            lines = f.readlines()
        formatted_lines = []
        for l in lines:
            formatted_lines.append(self.format_number(l))
        return formatted_lines

    def format_number(self, number):
        numbers_dict = self.load_dictionary()
        number_split = number.split(' ')
        if len(number_split) == 0:
            print('Empty string provided.')
            formatted_number = None
        elif len(number_split) == 1:
            formatted_number = numbers_dict.get(number_split[0])
        elif len(number_split) == 2:
            # TODO
            formatted_number = None
        else:
            print('Number not supported.')
            formatted_number = None
        return formatted_number
