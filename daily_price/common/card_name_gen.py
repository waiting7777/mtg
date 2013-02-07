
execfile("/home/waiting/mtg/daily_price/common/config.py")

if len(sys.argv) < 2:
    print 'please input card_set'
    exit()
    
if sys.argv[1] not in card_set:
    print 'please input supportted card_set'
    print card_set
    exit()

set = sys.argv[1]

# if os.path.exists('%s.html'%set) == False:
    
    # f = urllib.urlopen('http://magiccards.info/%s/en.html'%set)
    # page = f.read()
    # f.close()
    # w = open('%s.html'%set, 'w')
    # w.write(page)
    # w.close()
    
f = open('/home/waiting/mtg/card_data/%s/%s_en_all.html'%(set, set), 'r')    

head = 0
card_count = 0
cardinfo = {}

page = f.read()

head = page.find('<td width="25%" align="right">', head)
head = page.find('\n', head)
tail = page.find('cards', head)
total = page[head:tail].strip()

while(card_count != int(total)):
    
    
    head = page.find('<a href="/%s/en/'%set, head)
    tail = page.find('.html', head)
    
    num = page[head+len('<a href="/%s/en/')+1:tail]
    
    cardinfo[card_count] = {}
    cardinfo[card_count]['card_number'] = num
    
    head = page.find('html\">', head)
    tail = page.find('</a>', head)
    
    cardinfo[card_count]['card_name'] = page[head+len('html">'):tail]
    cardinfo[card_count]['card_image'] = 'http://www.waiting4u.org/mtg/images/card_images/%s/English/%s.jpg'%(set, cardinfo[card_count]['card_number'])
    
    head = page.find('<td>', head)
    head = page.find('\n', head)
    head = page.find('<td>', head)
    head = page.find('\n', head)
    
    head = page.find('<td>', head)
    tail = page.find('</td>', head)
    
    cardinfo[card_count]['card_rarity'] = page[head+len('<td>'):tail]
    
    if 'Plains' in cardinfo[card_count]['card_name']:
        cardinfo[card_count]['card_name'] = cardinfo[card_count]['card_name'] + ' (%s)'%cardinfo[card_count]['card_number'] 
        
    if 'Island' in cardinfo[card_count]['card_name']:
        cardinfo[card_count]['card_name'] = cardinfo[card_count]['card_name'] + ' (%s)'%cardinfo[card_count]['card_number'] 
        
    if 'Swamp' in cardinfo[card_count]['card_name']:
        cardinfo[card_count]['card_name'] = cardinfo[card_count]['card_name'] + ' (%s)'%cardinfo[card_count]['card_number'] 
        
    if 'Mountain' in cardinfo[card_count]['card_name']:
        cardinfo[card_count]['card_name'] = cardinfo[card_count]['card_name'] + ' (%s)'%cardinfo[card_count]['card_number'] 
        
    if 'Forest' in cardinfo[card_count]['card_name']:
        cardinfo[card_count]['card_name'] = cardinfo[card_count]['card_name'] + ' (%s)'%cardinfo[card_count]['card_number'] 
        
    card_count += 1

output = '# -*- coding: utf-8 -*- \n'    
output += 'info = {\n'
for key in cardinfo:
    output += '\"' + cardinfo[key]['card_name'] + '\" : { \"card_rarity\" : \"' + cardinfo[key]['card_rarity'] + '\", \"card_number\" : \"' + cardinfo[key]['card_number'] + '\", \"card_image\" : \"' + cardinfo[key]['card_image'] + '\"},\n'
    
output += '}\n'
w = open ('card_name_table/%s.txt'%set, 'w')    
w.write(output)
f.close()
w.close()
    
    
    
    # output = '\"' + cardinfo['card_name'] + '\" : { \"card_number\" : ' + str(cardinfo['card_number']) + ', \"card_image\" : \"' + cardinfo['card_image'] + '\"},\n'
    
    # w.write(output)
    # for i in range(10):
        # f.readline()
print cardinfo