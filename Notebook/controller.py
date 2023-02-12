import datetime

import model
import view
import data_base


def main():
    action = view.get_action()
    model.init_action(action)

    if action == 'добавить':
        name = view.get_name()
        body = view.get_body()
        time = str(datetime.datetime.now())
        model.init(name, body, time)
        data_base.add_note(name, body, time)
        view.successful_addition()  

    elif action == 'найти':
        name = view.get_note_from_notebook()
        model.init_criteria_name(name)
        result = data_base.search_note(name) 
        view.view_data(result)  

    elif action == 'все заметки':
        data_base.view_all()  

    elif action == 'удалить':
        name = view.get_name()
        model.init_criteria_name(name)
        data_base.delete_note(name)
    
    elif action == 'редактировать':
        name = view.get_name()
        model.init_criteria_name(name)
        old_note = data_base.search_note(name)
        print(old_note)
        
        if old_note != view.incorrect_input():
            print('Новая заметка:')
            body = view.get_body()
            model.init_criteria_body(body)
            data_base.change_note(name, body)
            view.successful_change()

    elif action == 'по дате':
        date = view.get_notes_by_date()
        model.init_time(date)
        data_base.search_by_date(date)

    else:
        view.view_data('Такой команды нет')
    
    answer = view.get_permission()
    model.init_action(answer)

    if answer == 'да':
        main()

    