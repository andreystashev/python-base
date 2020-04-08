# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1
import room_2

# lesson_005 не нужно было, просто каждый отдельный модуль импортируется с новой строки

first_room = ', '.join(room_1.folks)
print('В комнате room_1 живут: ', first_room,
      '\nВ комнате room_2 живут: ', room_2.folks.pop())

# зачет!
