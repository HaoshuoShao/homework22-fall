import csv

import class_hw

with open('./docs/DATA.csv', mode='w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['goods', 'provider', 'time', 'amount', 'isChanged', 'des'])

with open('./docs/DATA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)

newLine = class_hw.GoodInformation('goods', 'provider', 'time', 'amount', 'False', 'des')

newLine.WriteGoodInfo()
