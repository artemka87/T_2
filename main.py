
with open('1.txt', encoding='utf-8') as f:
  data=f.read()
  print(type(data))
  list = []
  for file in data.split("\n"):
    # if not file.strip():
    #   continue
    list.append(file.lstrip())
  # print(list)
  for file in enumerate(list):
    print(file)

with open('2.txt', encoding='utf-8') as a:
  data_1=a.read()
  # print(type(data))
  list_1 = []
  for files in data_1.split("\n"):
    list_1.append(files.lstrip())
  # print(list)
  for files in enumerate(list_1):
    print(files)
with open('3.txt', encoding='utf-8') as b:
  data_2=b.read()
  # print(type(data))
  list_2 = []
  for files in data_2.split("\n"):
    list_2.append(files.lstrip())
  # print(list)
  for files in enumerate(list_2):
    print(files)

def get_info_and_writing_to_list(file_names):
    '''Считывание содержимого файлов и запись информации в список'''
    my_data = []
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            lines = f.read().splitlines()
            my_data.append([file, len(lines)])
            my_data[len(my_data)-1] += lines
    my_data.sort(key=len)
    return my_data

def writing_info_to_file(my_data, my_file):
    '''Запись в файл информации (создание файла при условии отсутствия другого с таким же именем)'''
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in my_data:
            for elem in file:
                f.write(f'{elem}\n')
    file_path = os.path.join(os.getcwd(), my_file)
    return file_path

