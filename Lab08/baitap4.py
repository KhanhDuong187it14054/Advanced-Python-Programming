import urllib.request

import re

with urllib.request.urlopen('https://ananas.vn/') as response:
  html = response.readlines()

type = ['jpg','png','svg']

for i in html:
    txt = i.decode('utf-8')
    for j in type:
      x = re.findall('src.*'+j, txt)
      if(x != []):
        y = "".join(x)
        
        if(y.find('http') != -1):
            y = y.split('://')
            y = "".join(y[-1])
            if(y != 'ananas.vn/wp-content/uploads/banner-phụ_2m-600x320.jpg'):
                n = "https://"+ y
                m = "Lab08/images/" + y.split('/')[-1] 
                urllib.request.urlretrieve(n, m)
        
        else:          
            z = re.findall('/.*g', y)
            if( z != []):
                j = "".join(z) 
                if (j != "/icon_login.png") and (j != "wp-content/uploads/banner-phụ_2m-600x320.jpg"):
                    urllib.request.urlretrieve("https://ananas.vn"+ j, "Lab08/images/" + j.split('/')[-1])
          

        
    
        
        
        
        
        
