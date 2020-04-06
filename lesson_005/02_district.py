# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1, room2
from district.central_street.house2 import room2 as csr2
from district.soviet_street.house1 import room1 as ssh1r1, room2 as ssh1r2
from district.soviet_street.house2 import room1 as ssh2r1, room2 as ssh2r2

house1_1 = ', '.join(room1.folks)
house1_2 = ', '.join(room2.folks)
house2_2 = ', '.join(csr2.folks)
house3_1 = ', '.join(ssh1r1.folks)
house3_2 = ', '.join(ssh1r2.folks)
house4_1 = ', '.join(ssh2r1.folks)
house4_2 = ', '.join(ssh2r2.folks)
print('На районе живут: ', house1_1, ',', house1_2, ',', house2_2, ',', house3_1, ',', house3_2, ',', house4_1, ',',
      house4_2)
