import requests

x = input("Lutfen domain listesinin bulundugu dosyayi giriniz : ")
print('***************************************************************')
with open(x,'r') as file:
    words = []
    for item in file:
        words.append(item.strip())

for w in words:
    url = 'https://'+w+''
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print('[',r.status_code,']',url)
            with open('200.txt','a') as file1:
                file1.write(url+'\n')
        else:
            print('[',r.status_code,']',url)
            y = ''+str(r.status_code)+'.txt'
            with open(y,'a') as file1:
                file1.write(url+'\n')

    except requests.exceptions.ConnectionError:
        print('[  !  ]',url)
        with open('hata.txt','a') as file1:
            file1.write(url+'\n')
