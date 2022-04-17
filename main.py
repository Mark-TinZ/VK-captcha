import requests
import time
import random as rd
from time import sleep
 
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
 
 
# 3 4 5 11 14 15 17 18 19 20 21 22 24 27 30 31 35 38 39 40 42 43
sid = (3, 4, 5, 11, 14, 15, 17, 18, 19, 20, 21, 22, 24, 27, 30, 31, 35, 38, 39, 40, 42, 43)
starttime = time.time()
printProgressBar(0, 10000, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i in range(10000):
    id = rd.randint(1, len(sid)-1)
    response = requests.get(f"https://vk.com/captcha.php?sid={sid[id]}&s=1")
 
    file = open(f"img/{i}.png", "wb")
    file.write(response.content)
    file.close()
    Time = "{:02}:{:02}".format(int((time.time()-starttime)//60), int(time.time()-starttime)-(int(time.time()-starttime)//60)*60)
    printProgressBar(i + 1, 10000, prefix='Progress:', suffix=f'Complete {Time} File: img/{i}.png', length=50)
