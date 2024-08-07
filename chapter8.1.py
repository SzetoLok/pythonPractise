import configparser

def create_config():
    studentdata = configparser.ConfigParser()
    print(studentdata)
    return studentdata

def define_and_add_student(studentdata, section, maths, chin, eng):
    studentdata.add_section(section)
    studentdata.set(section, 'maths', maths)
    studentdata.set(section, 'chin', chin)
    studentdata.set(section, 'eng', eng)

def input_students(studentdata):
    numOfStudent = int(input('number of students: '))
    for i in range(numOfStudent):
        name = input('name: ')
        if studentdata.has_section(name):
            print('student already exists')
        else:
            maths = input('maths: ')
            chin = input('chin: ')
            eng = input('eng: ')
            define_and_add_student(studentdata, name, maths, chin, eng)

        f = open('students_score.txt', 'w')
        studentdata.write(f)
        f.close()

studentdata = create_config()
# input_students(studentdata)
studentdata.read('students_score.txt')
print(studentdata['lok']['maths'])
print(studentdata['lok']['chin'])

eng = studentdata['lok']['eng']
print(type(eng))
print(eng)
eng = int(eng)
print(type(eng))
print(eng)
studentarray = studentdata.sections()
print(studentarray)

