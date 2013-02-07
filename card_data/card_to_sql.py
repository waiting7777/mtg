# -*- coding: utf-8 -*-

import urllib, urllib2, cookielib, time

execfile("/home/waiting/mtg/daily_price/common/config.py")

if len(sys.argv) != 2:
    print 'please input card_set'
    exit()
    
if sys.argv[1] not in card_set:
    print 'please input supportted card_set'
    print card_set
    exit()
    
set = sys.argv[1]

for lan in language:
    f = open("%s/%s_%s_all.html"%(set, set, lan), "r")

    line = f.read()

    block_num = line.count('<tr class="even">') + line.count('<tr class="odd">')

    cardinfo = {}
    head = 0
    tail = 0
    card_count = 0

    for i in range(total_num[set]):
        index = i + 1
        card_count += 1
        
        cardinfo[index] = {}
        
        if index == 70 and lan == 'tw' and set == 'gtc':
            cardinfo[index]['card_name'] = '致命逼視'
            cardinfo[index]['card_rarity'] = 'Uncommon'
            cardinfo[index]['card_language'] = 'Taiwan'
            cardinfo[index]['card_color'] = 'Black'
            cardinfo[index]['card_type'] = '瞬間'
            cardinfo[index]['card_subtype'] = ''
            cardinfo[index]['card_value'] = ''
            cardinfo[index]['card_mana'] = 'XB'
            cardinfo[index]['card_image'] = 'http://magiccards.info/scans/tw/gtc/70.jpg'
            cardinfo[index]['card_text'] = '<b>消滅力量小於或等於X的目標生物</b>'
            cardinfo[index]['card_flavor'] = '<i>往黑暗角落的隨意一督，有可能是你的最後一督</i>'
            cardinfo[index]['card_number'] = '70'
            cardinfo[index]['card_set'] = 'gtc'
            cardinfo[index]['card_painter'] = 'Peter Mohrbacher'
            card_count += 1
        
        else:
            if card_count % 2 == 1:
                # start
                head = line.find('<tr class="even">', head)
                
                # card number
                head = line.find('align="right">', head)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_number'] = line[head+len('align="right">'):tail]
                print line[head+len('align="right">'):tail]

                # card name
                head = line.find('html">', tail)
                tail = line.find('</a>', head)
                
                cardinfo[index]['card_name'] = line[head+len('html">'):tail]
                print line[head+len('html">'):tail]
                
                # card type
                head = line.find('<td>', tail)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_type'] = line[head+len('<td>'):tail]
                print line[head+len('<td>'):tail]
                
                # card mana
                head = line.find('<td>', tail)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_mana'] = line[head+len('<td>'):tail]
                print line[head+len('<td>'):tail]
                
                # card rarity
                head = line.find('<td>', tail)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_rarity'] = line[head+len('<td>'):tail]
                print line[head+len('<td>'):tail]
                
                # card painter
                head = line.find('<td>', tail)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_painter'] = line[head+len('<td>'):tail]
                print line[head+len('<td>'):tail]
            
            if card_count % 2 == 0:
                # start
                head = line.find('<tr class="odd">', head)
                
                # card number
                head = line.find('align="right">', head)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_number'] = line[head+len('align="right">'):tail]
                print line[head+len('align="right">'):tail]
                
                # card name
                head = line.find('html">', tail)
                tail = line.find('</a>', head)
                
                cardinfo[index]['card_name'] = line[head+len('html">'):tail]
                print line[head+len('html">'):tail]
                
                # card type
                head = line.find('<td>', tail)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_type'] = line[head+len('<td>'):tail]
                print line[head+len('<td>'):tail]
                
                # card mana
                head = line.find('<td>', tail)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_mana'] = line[head+len('<td>'):tail]
                print line[head+len('<td>'):tail]
                
                # card rarity
                head = line.find('<td>', tail)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_rarity'] = line[head+len('<td>'):tail]
                print line[head+len('<td>'):tail]
                
                # card painter
                head = line.find('<td>', tail)
                tail = line.find('</td>', head)
                
                cardinfo[index]['card_painter'] = line[head+len('<td>'):tail]
                print line[head+len('<td>'):tail]
            
            # card type subtype value
            cardinfo[index]['card_subtype'] = ""
            cardinfo[index]['card_value'] = ""
            if '\xe2\x80\x94' in cardinfo[index]['card_type']:
                temp = cardinfo[index]['card_type'].split('\xe2\x80\x94')
                cardinfo[index]['card_type'] = temp[0].strip()
                cardinfo[index]['card_subtype'] = temp[1].strip()
                
                if 'Creature' in cardinfo[index]['card_type']:
                    cutpoint = cardinfo[index]['card_subtype'].rindex(" ")
                    cardinfo[index]['card_value'] = cardinfo[index]['card_subtype'][cutpoint:].strip()
                    cardinfo[index]['card_subtype'] = cardinfo[index]['card_subtype'][:cutpoint].strip()
                
                if 'Planeswalker' in cardinfo[index]['card_type']:
                    cutpoint = cardinfo[index]['card_subtype'].index(" ")
                    cardinfo[index]['card_subtype'] = cardinfo[index]['card_subtype'][:cutpoint].strip()
                  
            # card language
            if 'en' in lan:
                cardinfo[index]['card_language'] = 'English'
                
            if 'tw' in lan:
                cardinfo[index]['card_language'] = 'Taiwan'
                  
            # card color            
            cardinfo[index]['card_color'] = ""
            if 'W' in cardinfo[index]['card_mana']:
                cardinfo[index]['card_color'] += 'White|'
            if 'U' in cardinfo[index]['card_mana']:
                cardinfo[index]['card_color'] += 'Blue|'
            if 'B' in cardinfo[index]['card_mana']:
                cardinfo[index]['card_color'] += 'Black|'
            if 'R' in cardinfo[index]['card_mana']:
                cardinfo[index]['card_color'] += 'Red|'
            if 'G' in cardinfo[index]['card_mana']:
                cardinfo[index]['card_color'] += 'Green|'
            if 'Artifact' in cardinfo[index]['card_type']:
                cardinfo[index]['card_color'] += 'Artifact|'
            if 'Land' in cardinfo[index]['card_type']:
                cardinfo[index]['card_color'] += 'Land|'
                
            cardinfo[index]['card_color'] = cardinfo[index]['card_color'][:-1]
            
            # card image
            cardinfo[index]['card_image'] = 'http://magiccards.info/scans/%s/%s/%d.jpg'%(lan, set, index)
            
            # card set
            cardinfo[index]['card_set'] = '%s'%set
            
            # card text
            t = open('%s/%s/%d.html'%(set, lan, index), 'r')
            text = t.read()
            t.close()
            
            thead = 0
            ttail = 0
            
            thead = text.find('<p class="ctext">', thead)
            ttail = text.find('</p>', thead)
            
            cardinfo[index]['card_text'] = text[thead+len('<p class="ctext">'):ttail].translate(None, "\r")
            
            # card flavor
            thead = text.find('<p>', ttail)
            ttail = text.find('</p>', thead)
            
            cardinfo[index]['card_flavor'] = text[thead+len('<p>'):ttail].translate(None, "\r")
            # raw_input()
    
    if card_count != total_num[set]:
        print 'card number problem'
        exit()
    
    output = ""    
    for key in cardinfo:
        print cardinfo[key]
        output += cardinfo[key]['card_name'] + '|'
        output += cardinfo[key]['card_rarity'] + '|'
        output += cardinfo[key]['card_language'] + '|'
        output += cardinfo[key]['card_color'] + '|'
        output += cardinfo[key]['card_type'] + '|'
        output += cardinfo[key]['card_subtype'] + '|'
        output += cardinfo[key]['card_value'] + '|'
        output += cardinfo[key]['card_mana'] + '|'
        output += cardinfo[key]['card_image'] + '|'
        output += cardinfo[key]['card_text'] + '|'
        output += cardinfo[key]['card_flavor'] + '|'
        output += cardinfo[key]['card_number'] + '|'
        output += cardinfo[key]['card_set'] + '|'
        output += cardinfo[key]['card_painter'] + '\n'
        
        # raw_input()
        
    w = open('%s/%s_%s.txt'%(set, set, lan), 'w')
    w.write(output)    
