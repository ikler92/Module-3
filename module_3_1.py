calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    lent = len(string)
    up = string.upper()
    low = string.lower()
    count_calls()
    return lent, up, low


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        compare1 = string.lower()
        compare2 = list_to_search[i]
        result_of_low = compare2.lower()
        if compare1 != result_of_low:
            pass
        if compare1 == result_of_low:
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
