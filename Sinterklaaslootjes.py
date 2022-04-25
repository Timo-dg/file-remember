import random,json,os.path

names = []
lootjes = [] 
counter = 0
x = len(names)
naamDic = {

}

print('\nSinterklaaslootjes generator\n')
print('Typ "stop" als je alle namen hebt ingevoerd.')

check = True
try:
    file = open("C:/Users/timo/Documents/GitHub/file-remember/data/logs.json","a")
    if check:
        print("File created 'logs.json'.")
        check = False
except:
    with open("C:/Users/timo/Documents/GitHub/file-remember/data/logs.json", "x") as file:
        print("using 'logs.json'.")


while True:
    names.append(input('\nInvoer van alle namen: \n'))
    if 'stop' in names:
        break
    else:
        counter += 1

names.remove('stop')
names = list(set(names))
print('\naantal namen: ' + str(counter))


for x in range(counter):
    print(random.choice(names)+ ' heeft ' + random.choice(names)) 
    naamDic = names
    

json.dump(naamDic,file, indent=2)