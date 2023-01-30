import csv
import fnmatch

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
        number_split = number.split(' ')
        while 'y' in number_split: number_split.remove('y')

        if len(number_split) == 0:
            print('Empty string provided.')
            return None
        million_pos = [i for i, s in enumerate(number_split) if 'illón' in s]
        millions_pos = [i for i, s in enumerate(number_split) if 'illones' in s]
        million_pos = million_pos + millions_pos
        million_pos.sort()
        if len(million_pos) > 0:    
            if len(number_split[million_pos[-1]+1:]) > 0:
                if 'mil' in number_split[million_pos[-1]+1:]:
                    after_million = self.split_thousands(number_split[million_pos[-1]+1:])
                else:
                    after_million = self.format_up_to_3_digits(number_split[million_pos[-1]+1:])
            else:
                after_million = ''
            if len(number_split[:million_pos[-1]+1]) > 0:
                if 'mil' in number_split[:million_pos[-1]+1]:
                    millions = self.split_thousands(number_split[:million_pos[-1]]) # Get thousands only, without millions
                    millions += self.format_more_than_3_digits(number_split[million_pos[-1]:million_pos[-1]+1])[1:] # Add millions
                else:
                    millions = self.format_more_than_3_digits(number_split[:million_pos[-1]+1])
            else:
                millions = ''
            if len(after_million) > 0:
                formatted_number = millions[:-len(after_million)] + after_million
            else:
                formatted_number = millions
                
        elif 'mil' in number_split:
            formatted_number = self.split_thousands(number_split)
        else:
            formatted_number = self.format_up_to_3_digits(number_split)
            
        return formatted_number
    
    def split_thousands(self,number_split):
        thousand_pos = len(number_split) - 1 - number_split[::-1].index('mil') # get positin of last ocurrence of 'mil'
        if len(number_split[thousand_pos+1:]) > 0:
            hundreds = self.format_up_to_3_digits(number_split[thousand_pos+1:])
        else:
            hundreds = ''
        if len(number_split[:thousand_pos+1]) > 0:
            thousands = self.format_more_than_3_digits(number_split[:thousand_pos+1])
        else:
            thousands = ''
        if len(hundreds) > 0:
            formatted_number = thousands[:-len(hundreds)] + hundreds
        else:
            formatted_number = thousands
        return formatted_number

    def format_up_to_3_digits(self, number_split):
        numbers = []
        for number in number_split:
            numbers.append(self.numbers_dict.get(number))
        if len(number_split) == 1:
            formatted_number = numbers[0]
        elif len(number_split) == 2:       
            formatted_number = numbers[0][:-len(numbers[1])] + numbers[1]
        elif len(number_split) == 3:
            formatted_number = numbers[0][:-len(numbers[1])] + numbers[1][:-len(numbers[2])] + numbers[2]
        else:
            print('Number not supported.')
            formatted_number = None
        return formatted_number
    
    def format_more_than_3_digits(self, number_split):
        numbers = []
        for number in number_split:
            numbers.append(self.numbers_dict.get(number))
        if len(number_split) == 1:
            formatted_number = numbers[0]
        elif len(number_split) == 2:
            formatted_number = numbers[0] + numbers[1][1:]
        elif len(number_split) == 3:
            if 'millones' in number_split and 'mil' in number_split:
                formatted_number = numbers[0] + numbers[1][1:] + numbers[2][1:]
            else:
                formatted_number = numbers[0][:-len(numbers[1])] + numbers[1] + numbers[2][1:]
        elif len(number_split) == 4:
            if 'millones' in number_split and 'mil' in number_split:
                formatted_number = numbers[0][:-len(numbers[1])] + numbers[1] + numbers[2][1:] + numbers[3][1:]
            else:
                formatted_number = numbers[0][:-len(numbers[1])] + numbers[1][:-len(numbers[2])]+ numbers[2] + numbers[3][1:]
        elif len(number_split) == 7:
            formatted_number = numbers[0][:-len(numbers[1])] + numbers[1][:-len(numbers[2])]+ numbers[2] + numbers[3][1:]
        else:
            print('Number not supported.')
            formatted_number = None
        return formatted_number