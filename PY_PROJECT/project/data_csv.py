import csv

def information_from_csv(path):
    with open(path,'r') as csv_data:
        reader = csv.reader(csv_data,delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)                              
            country_dict = {key:value for (key,value) in iterable}  
            data.append(country_dict)
        return data

