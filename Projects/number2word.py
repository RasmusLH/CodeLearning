# Program that takes in a number and returns the word form of the number

number_words = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'one hundred',
    '1000': 'one thousand',
    '1000000': 'one million',
    '1000000000': 'one billion',
    '1000000000000': 'one trillion'
}

def number_to_word(number):
    if number in number_words:
        return number_words[number]
    elif len(number) == 2:
        return number_words[number[0] + '0'] + " " + number_words[number[1]]
    elif len(number) == 3:
        return number_words[number[0]] + " hundred " + number_to_word(number[1:])
    elif len(number) == 4:
        return number_words[number[0]] + " thousand " + number_to_word(number[1:])
    elif len(number) == 7:
        return number_words[number[0]] + " million " + number_to_word(number[1:])
    elif len(number) == 10:
        return number_words[number[0]] + " billion " + number_to_word(number[1:])
    elif len(number) == 13:
        return number_words[number[0]] + " trillion " + number_to_word(number[1:])
    else:
        return "Number out of range"
print(number_to_word(input("Enter a number: ")))