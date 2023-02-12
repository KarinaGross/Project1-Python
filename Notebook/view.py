def view_data(data):
    print(data)

def get_name():
    return input('Заголовок: ')

def get_body():
    return input('Тело заметки: ')

def successful_addition():
    print("\nЗаметка добавлена!\n")

def successful_delete():
    print("\nЗаметка удалена!\n")

def successful_change():
    print("\nЗаметка изменена!\n")

def get_note_from_notebook():
    return input('Введите заголовок для поиска: ')

def get_notes_by_date():
    return input("Введите дату в формате yyyy-mm-dd: ")

def get_action():
    return input("\nДля сохранения новой заметки введите 'добавить'.\nДля поиска заметки введите 'найти'.\nДля поиска по дате введите 'по дате'.\nДля просмотра списка заметок введите 'все заметки'.\nДля редактирования заметки введите 'редактировать'\nДля удаления контакта введите 'удалить'. \n>>>>>").lower()

def get_permission():
    return input("\nХотите сделать что-то еще?(введите да или нет):\n>>>>>").lower()

def tabular_output(data: dict):
    for key in data.keys():
        print(f'{key}: {data[key]}')

def incorrect_input():
    return 'Заметки с такими данными не существует'