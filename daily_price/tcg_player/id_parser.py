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
execfile("%s/%s_id.txt"%(set, set))

if os.path.exists('%s/html_database'%set) == False:
        print 'mkdir %s/html_database'%set
        os.mkdir('%s/html_database'%set)
        
if os.path.exists('%s/html_database/%s'%(set, date_string)) == False:
            print 'mkdir %s/html_database/%s'%(set, date_string)
            os.mkdir('%s/html_database/%s'%(set, date_string))
            
if os.path.exists('%s/price_database'%set) == False:
        print 'mkdir %s/price_database'%set
        os.mkdir('%s/price_database'%set)             

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    
name_list = info.keys()
name_list.sort()

date_string = time.strftime("%Y_%m_%d") 

out = open('%s/price_database/%s_price_%s.txt'%(set, set, date_string), 'w')
for name in name_list:
    if os.path.exists('%s/html_database/%s/%s.html'%(set, date_string, name)) == False:
        resp = opener.open('http://partner.tcgplayer.com/x2/mchl.ashx?pk=MAGCINFO&sid=%s'%card_id[name])
        respline = resp.read()
        w = open('%s/html_database/%s/%s.html'%(set, date_string, name), 'w')
        w.write(respline)
        w.close()

    f = open('%s/html_database/%s/%s.html'%(set, date_string, name), 'r')
    respline = f.read()
    
    print '%s/html_database/%s/%s.html'%(set, date_string, name)
        
    head = 0
    head = respline.find('M:', head)
    head = respline.find('$', head)
    tail = respline.find('<', head)
    
    price = respline[head+1:tail]
    
    print name + ':' + price
   
    output = name + '|' + info[name]['card_rarity'] + '|' + set + '|' + str(info[name]['card_number']) + '|' + price + '\n'
    out.write(output)
    
    # raw_input()