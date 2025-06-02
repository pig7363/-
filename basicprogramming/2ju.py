def print_row(columns, col_separator=':'):
    """
    Function for printing a row

    :param columns: (List) Data in a row
    :param col_separator: (str) Separator between columns. Default=':'
    """
    columns = [f' {row.title():9s} ' for row in columns]
    seperator = col_separator.join(columns)
    print(col_separator + seperator + col_separator)

bars = ['- - - - -'] * 4
head = ['name', 'density', 'people', 'size']
print_row(bars, col_separator = '+')
print_row(head)
print_row(bars, col_separator = '+')


# 함수주석: 따옴표 3개로 표시하고, 함수의 기능과 함수의 각 인자들에 대한 정보를 기입. 함수를 가져왔을 경우 시작 부분에 출처를 적는다.