# -*- coding: utf-8 -*-

execfile("../../common/config.py")

if len(sys.argv) < 2:
    print 'please input card_set'
    exit()
    
if sys.argv[1] not in card_set:
    print 'please input supportted card_set'
    print card_set
    exit()

set = sys.argv[1]
   
idinfo = {}    
for r in rarity:    

    num = card_num[set][r]
    if r == 'Common':
        num += card_num[set]['Land']
    elif r == 'Land':
        break
    
    i = 0
    while(1):
        print '%s/%s_%s_%d.html'%(set, set, r, i*50)
        if os.path.exists('%s/%s_%s_%d.html'%(set, set, r, i*50)) == False:
            break
            
        f = open('%s/%s_%s_%d.html'%(set, set, r, i*50), 'r')
        line = f.read()
        head = 0
        head = line.find('<td class="deckdbheader">Name</td>', head)
        
        for j in range(line.count('class="card_popup"' )):
        
            head = line.find('carddisplay.php?product=', head)
            tail = line.find('\"', head)
            print line[head+len('carddisplay.php?product='):tail].strip()
            sid = line[head+len('carddisplay.php?product='):tail].strip()
            
            head = line.find('tooltip', head)
            head = line.find('>', head)
            tail = line.find('<', head)
            print line[head+1:tail].strip().translate(None, '#')
            name = line[head+1:tail].strip().translate(None, '#')
            
            if '|' in name:
                token = name.split('|')
                name = token[0].strip()
            elif 'Flip' in name:
                temp_head = name.find('Flip')
                name = name[:temp_head-1].strip()
            elif 'Pre-Order' in name:
                temp_head = name.find('Pre-Order')
                name = name[:temp_head-1].strip()
            
            idinfo[name] = sid
            
        i += 1
            
name_list = idinfo.keys()
name_list.sort()

w = open('%s/%s_id.txt'%(set, set), 'w')

w.write('card_id = {\n')
for name in name_list:
    output = '\"'+ name + '\" : \"' + idinfo[name] + '\",\n'
    w.write(output)
    
w.write('}')        