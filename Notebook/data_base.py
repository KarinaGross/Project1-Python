import json
import os

import view


notebook = 'C:/Users/karin/OneDrive/Рабочий стол/GB/Промежуточная аттестация/Notebook/notebook.json' # файл notebook должен существовать до запуска программы


def add_note(name, body, time):
     if os.stat(notebook).st_size == 0: # проверка на пустоту файла notebook
          new_dict = {'id': 0, 'records': {}}
        
          with open(notebook, 'w', encoding='utf8') as file:
               json.dump(new_dict, file, indent=4, ensure_ascii=False)

     with open(notebook, encoding='utf8') as file:
         jsondata = json.load(file)

     count = jsondata['id'] + 1
     jsondata['id']+=1

     jsondata['records'][name] = {
                                   'ID': count,
                                   'note_body': body,
                                   'time_record': time
                                   }

     with open(notebook, 'w', encoding='utf8') as file:
         json.dump(jsondata, file, indent=4, ensure_ascii=False)


def search_note(name):
     try:
          with open(notebook, encoding='utf8') as file:
               jsondata = json.load(file)
          
          return jsondata['records'][name]['note_body']
     
     except KeyError:
          return view.incorrect_input()


def view_all():
     with open(notebook, encoding='utf8') as file:
          jsondata = json.load(file)

     for key in jsondata['records'].keys():
          print(f"heading: {key}")
          view.tabular_output(jsondata['records'][key])
          print('______________________')


def delete_note(name):
     try:
          with open(notebook, encoding='utf8') as file:
               jsondata = json.load(file)
          
          del jsondata['records'][name]
          
          with open(notebook, 'w', encoding='utf8') as file:
               json.dump(jsondata, file, indent=4, ensure_ascii=False)
          
          view.successful_delete()
     except KeyError:
          print(view.incorrect_input())
          


def change_note(name, body):
     try:
          with open(notebook, encoding='utf8') as file:
               jsondata = json.load(file)

          jsondata['records'][name]['note_body'] = body

          with open(notebook, 'w', encoding='utf8') as file:
               json.dump(jsondata, file, indent=4, ensure_ascii=False)
     except KeyError:
          print(view.incorrect_input())


def search_by_date(date):
     with open(notebook, encoding='utf8') as file:
          jsondata = json.load(file)

     notes = []
     for record in jsondata['records']:
          if date in jsondata['records'][record]['time_record']:
               notes.append(search_note(record))
     if len(notes) == 0:
          print(view.incorrect_input())
     else:
          print(*notes, sep='\n')

          
     
