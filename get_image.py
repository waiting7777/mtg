# -*- coding: utf-8 -*-

import urllib, urllib2, cookielib, time

execfile("/home/waiting/mtg/daily_price/common/config.py")

if len(sys.argv) < 2:
    print 'please input card_set'
    exit()
    
if sys.argv[1] not in card_set:
    print 'please input supportted card_set'
    print card_set
    exit()
    
set = sys.argv[1]

if os.path.exists("%s"%set) == False:
    os.system("mkdir %s"%set)

if os.path.exists("%s/images"%set) == False:
    os.system("mkdir %s/images"%set)
    
if os.path.exists("%s/images/English"%set) == False:
    os.system("mkdir %s/images/English"%set)

if os.path.exists("%s/images/Taiwan"%set) == False:
    os.system("mkdir %s/images/Taiwan"%set)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))    

for i in range(total_num[set]):    
    index = i + 1
        
    if os.path.exists("%s/images/Taiwan/%d.jpg"%(set, index)) == False:
        
        resp = opener.open('http://magiccards.info/scans/tw/%s/%d.jpg'%(set, index))
        line = resp.read()
        w = open("%s/images/Taiwan/%d.jpg"%(set, index), "w")
        w.write(line)
        w.close()
        print "Save %s %d tw"%(set, index)
        
    time.sleep(1)
    
    if os.path.exists("%s/images/English/%d.jpg"%(set, index)) == False:
        
        resp = opener.open('http://magiccards.info/scans/en/%s/%d.jpg'%(set, index))
        line = resp.read()
        w = open("%s/images/English/%d.jpg"%(set, index), "w")
        w.write(line)
        w.close()
        print "Save %s %d en"%(set, index)
        
    time.sleep(1)
        
    

# http://magiccards.info/scans/en/gtc/1.jpg
