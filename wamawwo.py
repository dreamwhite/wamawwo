#!/usr/bin/python3
try:
    import clipboard
    from pyperclip import PyperclipException
    clipboard_support = True
except ImportError:
    clipboard_support = False


def wamawwo(string):
    return ''.join([letter.replace("r", "w") if letter == "r" else letter.replace("R", "W") for index, letter in enumerate(string)])

phrase = input(wamawwo('Input phrase to Wamawwizzawe: '))
print('----------------------------------------------')
wamawwo_phrase = wamawwo(phrase)

if clipboard_support:
    try:
        clipboard.copy(wamawwo_phrase)
        print(wamawwo('Wamawwized phwase is in your clipboard.'))
    except PyperclipException:
        print(wamawwo('Something went wwong while attempting to put the phwase into the clipboawd.'))
else:
    print(wamawwo('Clipboawd suppowt unavailable.'))

print(wamawwo('Here is your wamawwizzed phwase wwitten out:'))
print('----------------------------------------------')
print(wamawwo_phrase)
