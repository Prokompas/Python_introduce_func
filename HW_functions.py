#Python функции домашняя работа


documents = [
  {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
  {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

def get_owner_name (documents_list = documents):
  """
  p – people – функция спрашивает номер документа и выведет имя человека, которому он принадлежит
  """
  num = input('Введите номер документа ')
  for document in documents_list:
    if num == document['number']:
      print('Владелец документа ', document['name'])

#get_owner_name()


def get_list_documents (documents_list = documents):
  """
  l– list – выводит список всех документов
  """
  for document in documents_list:
    print('{} {} {}\n'. format(document['type'], document['number'], document['name']))

#get_list_documents()


def get_shelf(directory_dict = directories):
  """
  s – shelf – спрашивает номер документа и выводит номер полки, на которой он находится
  """
  num = str(input('Введите номер документа '))
  for shelf, number in directory_dict.items():
    if num in number:
        print('Номер полки ', shelf)

#get_shelf()


def add_records (document = documents, directory_dict = directories):
  """
  a – add – добавляет новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться
  """
  type = input('Введите тип документа ')
  number = input('Введите номер документа ')
  name = input('Введите кому принадлежит документ ')
  document_info = {'type':type, 'number':number, 'name':name}
  document.append(document_info)
  shelf = input('Введите номер полки ')
  if shelf not in directory_dict.keys():
    directory_dict[shelf] = []
  directory_dict[shelf].append(number)

#add_records()


def del_document (documents_list = documents, directory_dict = directories):
  """
  d – delete – спрашивает номер документа и удаляет его из каталога и из перечня полок
  """
  num = input('Введите номер документа ')
  i = 0
  for document in documents_list:
    if num == document['number']:
      del(documents_list[i])
    i+=1
  for shelf, value in directory_dict.items():
    if num in value:
      value.remove(num)

#print(documents)
#print(directories)
#dict = {4:['3','5']}
#directories.update(dict)
#del_document()


def move_document (directory_dict = directories):
  """
  m – move – спрашивает номер документа и целевую полку и перемещает его с текущей полки на целевую
  """
  num = input('Введите номер документа ')
  shelf = input('Введите номер целевой полки ')
  for key, value in directory_dict.items():
    if num in value:
      value.remove(num)
  if shelf not in directory_dict.keys():
    directory_dict[shelf] = []    
  directory_dict[shelf].append(num)
      
#move_document()
 

def add_shelf (directory_dict = directories):
  """
  as – add shelf – спрашивает номер новой полки и добавляет ее в перечень
  """
  shelf = input('Введите номер новой полки ')
  if shelf not in directory_dict.keys():
    directory_dict[shelf] = []    

#add_shelf()
#print(directories) 

def main():
  while True:
    user_input = input('Введите команду ')
    if user_input == 'p':
      get_owner_name()
    elif user_input == 'l':
      get_list_documents()
    elif user_input == 's':
      get_shelf()
    elif user_input == 'a':
      add_records()
    elif user_input == 'd':
      del_document()
    elif user_input == 'm':
      move_document()
    elif user_input == 'as':
      add_shelf()
    elif user_input == 'q':
      print('Have a good day!')
      break

main()


