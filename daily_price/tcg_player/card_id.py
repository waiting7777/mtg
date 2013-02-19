# -*- coding: utf-8 -*-

import urllib, urllib2, cookielib, time, os

execfile("../../common/config.py")


if len(sys.argv) < 2:
    print 'please input card_set'
    exit()
    
if sys.argv[1] not in card_set:
    print 'please input supportted card_set'
    print card_set
    exit()
    
set = sys.argv[1]

execfile("../../common/card_name_table/%s.txt"%set)

if os.path.exists("%s"%(set)) == False:
    os.mkdir("%s"%(set))
    
idinfo = {}    
for i in range(total_num[set]):

    if os.path.exists('../../card_data/%s/en/%d.html'%(set, i+1)) == True:

        f = open('../../card_data/%s/en/%d.html'%(set, i+1), 'r')
        line = f.read()
        
        head = 0
        head = line.find('<title>', head)
        tail = line.find('(', head)
        
        name = line[head+len('<title>'):tail].strip()
        print line[head+len('<title>'):tail].strip()
        
        head = line.find('sid=', head)
        tail = line.find('>', head)
        
        sid = line[head+len('sid='):tail-1].strip()
        print line[head+len('sid='):tail-1].strip()
        
        if name == 'Plains' or name == 'Island' or name == 'Swamp' or name == 'Mountain' or name == 'Forest':
            name = name + ' (%d)'%(i+1)
        
        idinfo[name] = sid
        
    else:
    
        f = open('../../card_data/%s/en/%da.html'%(set, i+1), 'r')
        line = f.read()
        
        head = 0
        head = line.find('<title>', head)
        tail = line.find('(', head)
        
        name = line[head+len('<title>'):tail].strip()
        print line[head+len('<title>'):tail].strip()
        
        head = line.find('sid=', head)
        tail = line.find('>', head)
        
        sid = line[head+len('sid='):tail-1].strip()
        print line[head+len('sid='):tail-1].strip()
        
        idinfo[name] = sid
        
        f.close()
        
        f = open('../../card_data/%s/en/%db.html'%(set, i+1), 'r')
        line = f.read()
        
        head = 0
        head = line.find('<title>', head)
        tail = line.find('(', head)
        
        # name = name + ' | ' + line[head+len('<title>'):tail].strip()
        name = line[head+len('<title>'):tail].strip()
        print line[head+len('<title>'):tail].strip()
        
        head = line.find('sid=', head)
        tail = line.find('>', head)
        
        sid = line[head+len('sid='):tail-1].strip()
        print line[head+len('sid='):tail-1].strip()
        
        
        idinfo[name] = sid
    
name_list = idinfo.keys()
name_list.sort()

w = open('%s/%s_id.txt'%(set, set), 'w')

w.write('# -*- coding: utf-8 -*-\n')
w.write('card_id = {\n')
for name in name_list:
    output = '\"'+ name + '\" : \"' + idinfo[name] + '\",\n'
    w.write(output)
    
w.write('}')