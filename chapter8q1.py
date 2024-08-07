import configparser

# be aware of the data type
def add_patient(config, file):
    section = int(input("enter the 健保號碼: "))
    if config.has_section(str(section)):
        print('this patient has already existed.')
    else: 
        name = input("enter the 姓名: ")
        age = int(input("enter the 年齡: "))
        gender = input("enter the 性別: ")
        tel = int(input("enter the tel: "))
        specialty = input('enter the specialty: ')
        config.add_section(str(section))
        print(config.sections())
        config.set(str(section), "name", name)
        config.set(str(section), "age", str(age))
        config.set(str(section), "gender", gender)
        config.set(str(section), "tel", str(tel))
        config.set(str(section), "specialty", specialty)
        with open(file, 'w') as configfile:
            config.write(configfile)

def modify_patient(config, file):
    section = str(int(input("enter the 健保號碼: ")))
    if config.has_section(section):
        name = input("enter the 姓名: ")
        age = int(input("enter the 年齡: "))
        gender = input("enter the 性別: ")
        tel = int(input("enter the tel: "))
        specialty = input('enter the specialty: ')
        print(config.sections())
        config.set(section, "name", name)
        config.set(section, "age", str(age))
        config.set(section, "gender", gender)
        config.set(section, "tel", str(tel))
        config.set(section, "specialty", specialty)
    else:
        print('this patient doesn\'t exist.')
    with open(file, 'w') as configfile:
            config.write(configfile)

def search_patient(config, file):
    section = str(int(input("enter the 健保號碼: ")))
    if config.has_section(section):
        print("Here are the information of the patient: ", section)
        print(config.get(section, "name"))
        print(config.get(section, "age"))
        print(config.get(section, "gender"))
        print(config.get(section, "tel"))
        print(config.get(section, "specialty"))
    else:
        print('this patient doesn\'t exist.')

def delete_patient(config, file):
    section = str(int(input("enter the 健保號碼: ")))
    if config.has_section(section):
        config.remove_section(section)
        print('this patient', section, ' has been deleted.')
    else:
        print('this patient doesn\'t exist.')
    with open(file, 'w') as configfile:
        config.write(configfile)

def print_female_patient(config, file):
    patients = config.sections()
    for i in patients:
        gender = config[i]['gender']
        if gender == 'f':
            print(i, config[i]['name'])
    with open(file, 'w') as configfile:
        config.write(configfile)

    
#main
config = configparser.ConfigParser()
f = 'patients.ini'
config.read(f)
# add_patient(config, f)
# print_female_patient(config, f)
# modify_patient(config, f)
# search_patient(config, f)
# delete_patient(config,f)
# print(config['543']['gender'])

while True:
    print('1. add patient')
    print('2. modify patient')
    print('3. search patient')
    print('4. delete patient')
    print('5. print female patient')
    print('6. quit')
    choice = int(input('enter your choice: '))
    if choice == 1:
        add_patient(config, f)
    elif choice == 2:
        modify_patient(config, f)
    elif choice == 3:
        search_patient(config, f)
    elif choice == 4:
        delete_patient(config, f)
    elif choice == 5:
        print_female_patient(config, f)
    elif choice == 6:
        break
