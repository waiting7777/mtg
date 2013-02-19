# -*- coding: utf-8 -*-

execfile("../../common/config.py")

if len(sys.argv) < 2:
    print 'please input card_set'
    exit()
    
if sys.argv[1] not in card_set:
    print 'please input supportted card_set'
    print card_set
    exit()

s = sys.argv[1]
    
os.mkdir('%s'%s)
for r in rarity:
    start = 0
    
    if r == 'Land':
        break
    
    while(1):
        link = 'http://sales.starcitygames.com/category.php?cat=%d&start=%d&rarity=%c'%(star_city_set_number[s], start, r[0])
        f = urllib.urlopen(link)
        print link
        page = f.read()
        if 'There are no items in that category.' in page:
            break
        else:
            w = open('%s/%s_%s_%d.html'%(s, s, r, start), 'w')
            w.write(page)
            start += 50
            f.close()
            w.close()
        
        time.sleep(1)
            