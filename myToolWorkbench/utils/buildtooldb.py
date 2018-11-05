import csv
from myToolWorkbench.models import Tool

# if __name__ == '__main__':


lol = list(csv.reader(open('myToolWorkbench/utils/tools.txt', 'r'), delimiter='\t'))
i = 0;
for line in lol:
    i = i + 1
    if line[0] == 'ISN Part Number':
        pass
    else:
        str = ''
        for l in line:
            str += l + "\t"
        print(str)
        if line[8] == '':
            line[8] = 0
        Tool.objects.create(
            part_number=line[0],
            description=line[1],
            cost=float(line[2]),
            upc_code=int(line[8]),
            special_retail=float(line[3]),
            regular_retail=float(line[4]),
            weight=float(line[9]),
            length=float(line[10]),
            width=float(line[11]),
            height=float(line[12]),
            origin_country=line[13]
        ).save()
        if i > 10:
            break



"""

 [0] ISN Part Number
 [1] Description
 [2] Cost
 [3] Special Retail
 [4] Regular Retail
 [5] Catalog Page
 [6] TW Page
 [7] UOM
 [8] UPC Code
 [9] Weight
 [10] Length
 [11] Width
 [12] Height
 [13] Country of Origin

part_number = models.CharField(max_length=30)
description = models.TextField()
cost = models.DecimalField(max_digits=7, decimal_places=2)
special_retail = models.DecimalField(max_digits=7, decimal_places=2)
regular_retail = models.DecimalField(max_digits=7, decimal_places=2)
upc_code = models.IntegerField()
weight = models.DecimalField(max_digits=7, decimal_places=2)
length = models.DecimalField(max_digits=7, decimal_places=2)
width = models.DecimalField(max_digits=7, decimal_places=2)
height = models.DecimalField(max_digits=7, decimal_places=2)

"""