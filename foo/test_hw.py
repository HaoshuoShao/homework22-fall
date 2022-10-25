# import csv

# import function_hw as F

# F.ClearItem()

# F.AddItem('Bad', 'NONE', '2022/9/12', '5KG', 'False', 'Haha')
# F.AddItem('ilala', 'NONE', '2022/9/12', '5KG', 'False', 'Haha')
# F.AddItem('notBad', 'NONE', '2022/9/12', '5KG', 'False', 'Haha')
# F.AddItem('stupid', 'NONE', '2022/9/12', '5KG', 'False', 'Haha')
# F.AddItem('huaji', 'NONE', '2022/9/12', '5KG', 'False', 'Haha')

# F.DeleteItem(4)
# F.ShowItems()
# F.queryItem('h')

import time

getTime = time.localtime(time.time())
print(str(getTime.tm_year) + '/' + str(getTime.tm_mon) + '/' + str(getTime.tm_mday)
)
