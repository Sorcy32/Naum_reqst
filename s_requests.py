import requests, json 
import config               #Мой файл конфига
import sert                 #мой файл включения сертификата
import save_to_xlsx as stx  #Мой файл для сохранения xlsx

link1 = config.get_setting("Network","link")
access_key = config.get_setting('Network','AccessKey')
login = config.get_setting('Account','login')
Password = config.get_setting('Account','password')
input_data = []             #Загруженные из файла данные              
total_links  = 0             
working_data = []           #Наполнение данных для эскпорта

def get_typecode_by_lication(link, login, Password, location):

    with sert.pfx_to_pem(
            config.get_setting ("Network", "Certificate_name"),
            config.get_setting ("Network", "Certificate_pass")) as cert:
        r = requests.get(link, cert=cert, auth=(login, Password))
    if r.status_code == 200:
        j = json.dumps(r.json())
        resp = json.loads(j)
        temp_data = [location, resp['typeCode'], resp['title']]
        working_data.append(temp_data)
        print('\n Успешно! \n')
        return working_data        
    else:
        print('\nОтвет сервера отрицательный\n')
        temp_data = [location, 'Error', 'Сервер ответил отрицательно']
        working_data.append(temp_data)
        return working_data
        
'Получаем список запросов из файла links.txt  '
def get_input():
    global total_links
    with open(config.get_setting('Paths','InputFile'), 'r') as i_data:
        for row in i_data:
            input_data.append(row)
    print('Всего ссылок: ',  len(input_data))
'Запуск'
def start():
    get_input()
    current_link_num = 0
    for line in input_data:
        line = line.strip()
        linkk = str(link1+line+access_key)        
        print ('Работаю по ссылке' , linkk)
        current_link_num = current_link_num+1
        print('Ссылка №' , current_link_num, ' из ', total_links)
        get_typecode_by_lication(linkk, login, Password, line)        
    stx.save_to_xlsx(working_data)

if __name__ == "__main__":
    start()
