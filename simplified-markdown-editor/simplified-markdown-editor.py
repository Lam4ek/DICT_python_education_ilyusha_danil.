i = True
function = ['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'unordered-list', 'ordered-list', 'new-line', '!help']
while i == True:
    a = input('Choose a formatter: ')
    if a not in ('plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line', '!help', '!done'):
        print('Unknown formatting type or command')
    if a == ('!help'):
        print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line' '\n' 'Special commands: !help !done')
    if a == ('!done'):
        i = False