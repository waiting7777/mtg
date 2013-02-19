# -*- coding: utf-8 -*- 

import urllib, urllib2, cookielib, time

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
        print 'mkdir star_city_game/%s/html_database'%set
        os.mkdir('%s/html_database'%set)
        
if os.path.exists('%s/html_database/%s'%(set, date_string)) == False:
            print 'mkdir %s/html_database/%s'%(set, date_string)
            os.mkdir('%s/html_database/%s'%(set, date_string))
            
if os.path.exists('%s/price_database'%set) == False:
        print 'mkdir star_city_game/%s/price_database'%set
        os.mkdir('%s/price_database'%set)            

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
date_string = time.strftime("%Y_%m_%d")
out = open('%s/price_database/%s_price_%s.txt'%(set, set, date_string), 'w')


name_list = info.keys()
name_list.sort()

for name in name_list: 
    
    if os.path.exists('%s/html_database/%s/%s.html'%(set, date_string, name)) == False:
        login_data = urllib.urlencode({'product' : card_id[name], 'qty' : '1', 'mode' : 'login'})
        resp = opener.open('http://sales.starcitygames.com/cart_product_ajax.php', login_data)
        respline = resp.read()
        w = open('%s/html_database/%s/%s.html'%(set, date_string, name), 'w')
        w.write(respline)
        w.close()
    
    resp_data = {}
    
    f = open('%s/html_database/%s/%s.html'%(set, date_string, name), 'r')
    respline = f.read()
    # print respline
    head = respline.find('success')
    tail = respline.find(',', head)
    resp_data['success'] = respline[head+9:tail]
    head = respline.find('fatal_error')
    tail = respline.find(',', head)
    resp_data['fatal_error'] = respline[head+13:tail]
    head = respline.find('productid')
    tail = respline.find(',', head)
    resp_data['productid'] = respline[head+12:tail-1]
    head = respline.find('feedback')
    tail = respline.find('.\",', head)
    resp_data['feedback'] = respline[head+11:tail]
    
    
    print resp_data
            
    if resp_data['success'] == 'true' and resp_data['fatal_error'] == 'false' and resp_data['productid'] == card_id[name]:
        tail = resp_data['feedback'].rfind('was')
        # if cardinfo['name'] != resp_data['feedback'][:tail-1]:
            # raise IOError
        head = resp_data['feedback'].find('$')
        price = resp_data['feedback'][head+1:]
    
    else:
        price = 'N/A'
    
    output = name + '|' + info[name]['card_rarity'] + '|' + set + '|' + str(info[name]['card_number']) + '|' + price + '\n'
    out.write(output)
        
