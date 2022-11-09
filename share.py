import requests,threading
from time import sleep
class Main_Share:
    def __init__(self,token,id) -> None:
        self.token = token
        self.id = id
    def share(self,x):
        
        response = requests.post(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{self.id}&published=0&access_token={self.token}').json()
        try:
            ID = response['id']
            print(response)
        except:
            print(f'Share EROR!',end = '\r')
list_token = open('D:\\token.txt').read().split('\n')
a = len(list_token)
id = '129631559891013'
x = 0
while True:
    for token in list_token:
        
        p = Main_Share(token, id).share
        chay = threading.Thread(target=p,args=(a,)).start()
       
        
    