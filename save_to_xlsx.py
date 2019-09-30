from openpyxl import Workbook
from datetime import datetime, date, time
import openpyxl
'''Настройка. Создаем лист и готовим название выходного файла, 
    имя которого будет текущим временем'''
wb = Workbook()
ws = wb.create_sheet("Output", 0)
dt_now =(str(datetime.strftime(datetime.now(),
                "%d.%m.%y %H.%M.%S")) + '.xlsx')
#data_set = [] 

def save_to_xlsx(working_data):
    data_set = working_data
    ws.append(['Location','typeCode','title'])
    for row in data_set:
        ws.append(row)
    wb.save(dt_now)
    print('Сохранено в файл: ', dt_now)




if __name__ == "__main__":
    pass
