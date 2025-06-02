def print_row(columns, col_separator=':'):
    """
    Function for printing a row

    :param columns: (List) Data in a row
    :param col_separator: (str) Separator between columns. Default=':'
    """
# 함수주석: 따옴표 3개로 표시하고, 함수의 기능과 함수의 각 인자들에 대한 정보를 기입. 함수를 가져왔을 경우 시작 부분에 출처를 적는다.
    new_columns = []
    for row in columns:
        if type(row) == str:
            new_columns.append(f' {row.title():9s} ')
        elif type(row) == int:
            new_columns.append(f' {row:9d} ')
        elif type(row) == float:
            new_columns.append(f' {row:9.3f} ')
        else:
            new_columns.append(f' {str(row):9s} ')
    separator = col_separator.join(new_columns)
    print(col_separator + separator + col_separator)

def read_row():
    """
    Read input from the user

    :return: Dictionary of a country
    """
    text = input('Type name, population, size of country: ').lower().strip()
    if text == 'exit':
        return{}
    
    columns = text.split(',')
    if len(columns) != 3:
        print('Please type 3 items.')
        return read_row()

    name, people, size = columns
    people = int(people)
    size = int(size)
    return{
        'name': name.title().strip(),
        'people': people,
        'size': size,
        'density': people/size
    }

def answer_question(countries):
    """
    Answer question of users:

    param countries: (List) Country dictionaries
    """
    text = input('Question? ').lower().strip()
    if text == 'exit':
        return
    
    operation, target = text.split(' ')
    target_list = [c[target] for c in countries]
    if operation == 'max':
        answer = max(target_list)
    if operation == 'min':
            answer = min(target_list)
    if operation == 'sum':
        answer = sum(target_list)
    if operation == 'average':
        answer = sum(target_list) / len(target_list)

    print(f'Answer: {answer:9.3f}')
    answer_question(countries)

if __name__ == '__main__':
    countries = []
    while True:
        columns = read_row()
        if len(columns) == 0:
            break

        countries.append(columns)

    bars = ['- - - - -'] * 4
    head = ['name', 'people', 'size', 'density']

    print_row(bars, col_separator = '+')
    print_row(head)
    print_row(bars, col_separator = '+')
    for item in countries:
        print_row([item[key] for key in head])
    print_row(bars, col_separator = '+')

    answer_question(countries)