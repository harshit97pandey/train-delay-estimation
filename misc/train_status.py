import requests
from requests.auth import HTTPBasicAuth
import json
import pickle
import time
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

################################################################################
train_list = pickle.load(open('train_list_MGS.p','rb'))

i=0
train_list = train_list[i:]

################################################################################
for train_num in train_list:

    url="http://api.railwayapi.com/live/train/"+str(train_num)+"/doj/20160328/apikey/<api_key>/"
    response = requests.get(url,headers=header,proxies=None)
    if response.status_code == 200:
        #print response.text
        status = json.loads(response.text)
        stat = status['response_code']
        if stat == 200:
            f = open('/home/zerone/python/ogd/train_running_status/Train'+str(train_num)+'.txt','a')
            f.write(response.text)
            f.write('\n')
            print 'Success',train_num, 'index', i
        else:
            print 'Fail',train_num, 'index', i

    else:
        print response.status_code,'Error',train_num, 'index', i

    time.sleep(2)
    i=i+1
