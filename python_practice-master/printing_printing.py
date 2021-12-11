formatter = '{} {} {} {} {} {} {} {} {} {}'
print(formatter.format(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(formatter.format('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'))
print(formatter.format(True, False, True, False, True, False, True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter, formatter, formatter, formatter, formatter, formatter, formatter))
print(formatter.format(
    'one two three',
    'pailam ekta biri',
    'biri te nai agun',
    'pailam ekta begun',
    'begun e nai bichi',
    'pailam ekta kachi',
    'kachi te nai dhar',
    'pailam ekta har',
    'har e nai locket',
    'pailam ekta pocket'
 ))