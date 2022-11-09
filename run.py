import os, platform
os.system('git pull')
try:
    import requests
except:
    os.system('pip2 install requests')
try:
    import futures
except:
    os.system('pip install futures')

import old_c
old_c.main()
