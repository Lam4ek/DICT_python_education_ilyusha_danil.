i = True
text = ''
function = ['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'unordered-list', 'ordered-list', 'new-line', '!help']
while i == True:
    a = input('Choose a formatter: ')
    if a not in ('plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line', '!help', '!done'):
        print('Unknown formatting type or command')
    if a == ('plain'):
        text = text + input('Text: ') + '\n'
        print(text)
    if a == ('bold'):
        text = text + '**' + input('text') + '**' + '\n'
        print(text)
    if a == 'italic':
        text = text + '*' + input('text') + '*' + '\n'
        print(text)
    if a == 'header':
        header_level = int(input('Level: '))
        if header_level > 7 or header_level < 0:
            print('The level should be within the range of 1 to 6.')
        else:
            text = text + header_level * '#' + input('text') + header_level * '#' + '\n'
            print(text)
    if a == 'link':
        text = text + '[' + input('Label: ') + ']' + input('Url: ') + '\n'
        print (text)
    if a == 'inline-code':
        text = text + '`' + input('Code: ') + '`' + '\n'
        print(text)
    if a == 'new-line':
        text = text + "\n"
        print(text)
    if a == 'ordered-list':
        n = int(input('Number of rows: '))
        if n < 1:
            print('The number of rows should be greater than zero.')
        else:
            for i in range(1, n+1):
                listText = input('Row #' + str(i) + ": ")
                text = text + '\n' + str(i) + ". " + listText
        print(text + '\n')
        i = True
    if a == 'unordered-list':
        m = int(input('Number of rows: '))
        if m < 1:
            print('The number of rows should be greater than zero.')
        else:
            for i in range(1, m+1):
                listText = input('Row #' + str(i) + ": ")
                text = text + '\n' + "- " + listText 
        print(text + '\n')
        continue
    if a == ('!help'):
        print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line' '\n' 'Special commands: !help !done')
    if a == ('!done'):
        i = False
        my_file = open("results.txt", "w+")
        my_file.write(text)