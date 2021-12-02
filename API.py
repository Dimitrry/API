import requests
cities=["svo","London","Cherepovets"]
for city in cities:
    url="https://wttr.in/"+city+"?m?3?n"
    response=requests.get(url,headers={"Accept-Language":"ru"})
    print(response.text)












# https://vk.com/andreypiguzov
