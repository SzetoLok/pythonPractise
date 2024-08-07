import configparser

def configReadAndWriteSection_withConfigParser(config, file, section):
   config.read(file)
   # config['Section 12'] = {}
   print('Before add section: ',config.sections())
   if config.has_section(section):
      print('this section has already existed.')
   else:
         config.add_section(section)
         print('After add section: ',config.sections())
         with open(file, 'w') as configfile:
            config.write(configfile)

def configRead_withConfigParser(config, file):
   config.read(file)

def configReadAndWriteOptions_withConfigParser(config, file, section, key, value):
   config.set(section, key, value)
   print(config[section],': ')
   with open(file, 'w') as configfile:
      config.write(configfile)

def configopen(config, file):
   config = open(file, 'r')
   # config['Section 12'] = {}
   # print(config.sections())
   # print(config)
   for line in config:
      print(line)
   config.close()
   return config

def configwrite_withoutconfigparser(file, str):
   # with open(file, 'w') as configfile:
   configfile = open(file,'w')
   configfile.write(str + '\n')

config = configparser.ConfigParser()
# configread(config, 'test_config.ini')
# configopen(config, 'test_config.ini')
f = 'test_config.ini'
# configwrite_withoutconfigparser(f, 'i am lucas1')
# configReadAndWriteSection_withConfigParser(config, f , 'I am lucas 151')
# configReadAndWriteSection_withConfigParser(config, f , 'I am lucas 17')
configRead_withConfigParser(config, f )

print(config.sections())
configReadAndWriteOptions_withConfigParser(config, f, 'i am lucas3', 'name', 'lucas3')
configReadAndWriteOptions_withConfigParser(config, f, 'I am lucas 151', 'name', 'lucas1')
configReadAndWriteOptions_withConfigParser(config, f, 'I am lucas 61', 'name', 'lucas2')

# configReadAndWriteSection_withConfigParser(config, f , 'I am lucas 61')
# configopen(config, f)
# configwrite_withoutconfigparser(f, '[i am lucas2]')
# configopen(config, f)
# configwrite_withoutconfigparser(f, '[i am lucas3]')
# configopen(config, f)
# configwrite_withoutconfigparser(f, '[i am lucas4]')
# configContent = configopen(config, f)
# print(configContent)
# configfile = open(f,'w')
# configfile.write(str(configContent) + '\n')

# configfile.write('1' + '\n')
# configfile.close()
# configfile = open(f,'w')
# configfile.write('2' + '\n')
# configfile.close()
# configfile = open(f,'w')
# configfile.write('1' + '\n')
# configfile.write('3' + '\n')
# configfile.close()

# config['Section 1'] = {'key1': 'value1', 'key2': 'value2'}
# f =config.read('test_config.ini')
# config = open('test_config.ini', 'r')
# config['Section 1'] = {}
# print(config.sections())
# print(config)
# print(f)
# config['Section 2'] = {}
# print(config.sections())
# print(config['Section 1']['key1'])


# config['Section 2']['key3'] = 'value3'
# config['Section 2']['key4'] = 'value4'
# config['Student1'] = {'name': 'lucas', 'gender': 'male'}
# config['Student2'] = {}
# config['Student2']['name'] = 'carol'
# config['Student2']['gender'] = 'female'
 
 
# a = config['Section 1']['key2']
# print(a)
# config.add_section('student4')
# config.set('Section 1', 'name', 'nike1')
# nike = config.has_section('student3')
# print(nike)
# configArrays = config.sections()
# print(configArrays)
# student = config.get('student3', 'name')
# print(student)
# config.remove_section('Section 1')
# config.remove_option('Student2','gender')
# config.remove_option('Section 1','key1')
# config.remove_option(['Section 1'],['key1'])
# config['Student2']['gender'] = 'female'

# with open('test_config.ini', 'w') as configfile:
#    config.write(configfile)