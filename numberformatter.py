import csv

class NumberFormatter:
    def __init__(self, numbers_dict_csv):
        self.numbers_dict_csv = numbers_dict_csv
        self.numbers_dict = self.load_dictionary()

    def load_dictionary(self):
        reader = csv.reader(open(self.numbers_dict_csv, mode='r'), delimiter=',')
        numbers_dict = {}
        for row in reader:
            zeroes = '0'*int(row[1]) if int(row[1])>0 else ''
            numbers_dict[row[2]] = row[0] + zeroes
        return numbers_dict

    def format_numbers(self, numbers_tuple):
        formatted_lines = []
        for number in numbers_tuple:
            formatted_lines.append(self.format_number(number))
        return formatted_lines

    def format_number(self, number):
        mil_pos = -1
        number_split = number.split(' ')
        while 'y' in number_split: number_split.remove('y')

        if len(number_split) == 0:
            print('Empty string provided.')
            return None
        if 'mil' in number_split:
            mil_pos = len(number_split) - 1 - number_split[::-1].index('mil')
            if len(number_split[mil_pos+1:]) > 0:
                cent = self.format_up_to_3_digits(number_split[mil_pos+1:])
            else:
                cent = ''
            if len(number_split[:mil_pos+1]) > 0:
                mil = self.format_more_than_3_digits(number_split[:mil_pos+1])
            else:
                mil = ''
            if len(cent) > 0:
                formatted_number = mil[:-len(cent)] + cent
            else:
                formatted_number = mil
        else:
            formatted_number = self.format_up_to_3_digits(number_split)
            
        return formatted_number

    def format_up_to_3_digits(self, number_split):
        numbers = []
        if len(number_split) == 1:
            formatted_number = self.numbers_dict.get(number_split[0])
        elif len(number_split) == 2:
            for number in number_split:
                numbers.append(self.numbers_dict.get(number))
            formatted_number = numbers[0][:-len(numbers[1])] + numbers[1]
        elif len(number_split) == 3:
            for number in number_split:
                numbers.append(self.numbers_dict.get(number))
            formatted_number = numbers[0][:-len(numbers[1])] + numbers[1][:-len(numbers[2])] + numbers[2]
        else:
            print('Number not supported.')
            formatted_number = None
        return formatted_number
    
    def format_more_than_3_digits(self, number_split):
        numbers = []
        if len(number_split) == 1:
            formatted_number = self.numbers_dict.get(number_split[0])
        elif len(number_split) == 2:
            for number in number_split:
                numbers.append(self.numbers_dict.get(number))
            formatted_number = numbers[0] + numbers[1][1:]
        elif len(number_split) == 3:
            for number in number_split:
                numbers.append(self.numbers_dict.get(number))
            formatted_number = numbers[0][:-len(numbers[1])] + numbers[1] + numbers[2][1:]
        elif len(number_split) == 4:
            for number in number_split:
                numbers.append(self.numbers_dict.get(number))
            formatted_number = numbers[0][:-len(numbers[1])] + numbers[1][:-len(numbers[2])]+ numbers[2] + numbers[3][1:]
        else:
            print('Number not supported.')
            formatted_number = None
        return formatted_number