import csv

with open('/Users/szetolok/Desktop/Coding/pythonPractise/webscrape/names.csv','r') as csv_file:
    # csv_reader = csv.reader(csv_file)
    # for row in csv_reader:
    #     print(row)
    csv_dictReader = csv.DictReader(csv_file)
    with open('new_names.csv','w') as new_file:
        fieldnames= ['first_name','last_name','email']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for row in csv_dictReader:
            # del row['email']
            csv_writer.writerow({'first_name':row['first_name'],'last_name':row['last_name'], 'email':row['email']})
    # print(csv_dictReader.fieldnames)
    # for row in csv_dictReader:
    #     print(row)