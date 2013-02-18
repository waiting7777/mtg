# -*- coding: utf-8 -*- 

execfile("/home/waiting/mtg/daily_price/common/config.py")

if len(sys.argv) < 2:
    print 'please input card_set'
    exit()
    
if sys.argv[1] not in card_set:
    print 'please input supportted card_set'
    print card_set
    exit()
    
set = sys.argv[1]


if os.path.exists("%s"%(set)) == False:
    os.system("mkdir %s"%(set))

for lan in language:    
    if os.path.exists("%s/%s"%(set, lan)) == False:    
        os.system("mkdir %s/%s"%(set, lan))

    if os.path.exists("%s/%s_%s_all.html"%(set, set, lan)) == False:
    
        f = urllib.urlopen("http://magiccards.info/%s/%s.html"%(set, lan))
        line = f.read()
        
        w = open("%s/%s_%s_all.html"%(set, set, lan), "w")
        w.write(line)
        print "%s/%s_%s_all.html"%(set, set, lan)
        
        f.close()
        w.close()
        
    for i in range(total_num[set]):
    
        index = i + 1
        print index
        
        # dka
        if set == 'dka':
            if index == 8 or index == 38 or index == 47 or index == 51 or index == 64 or index == 90 or index == 114 or index == 145 or index == 149 or index == 152 or index == 159 or index == 165 or index == 168 or index == 176 or index == 181 or index == 182 or index == 185 or index == 193 or index == 208 or index == 209:

                if os.path.exists("%s/%s/%da.html"% (set, lan, index)) == False:
            
                    fa = urllib.urlopen("http://magiccards.info/%s/%s/%da.html" % (set, lan, index))
                    fb = urllib.urlopen("http://magiccards.info/%s/%s/%db.html" % (set, lan, index))
                    
                    linea = fa.read()
                    lineb = fb.read()
                    
                    wa = open("%s/%s/%da.html"% (set, lan, index), "w")
                    wb = open("%s/%s/%db.html"% (set, lan, index), "w")
                    
                    wa.write(linea)
                    wb.write(lineb)
                
                    print 'save %s %d.html'%(set, index)
                    
                    fa.close()
                    fb.close()
                
                    wa.close()
                    wb.close()
                    
        else:
            if os.path.exists("%s/%s/%d.html"% (set, lan, index)) == False:
                
                f = urllib.urlopen("http://magiccards.info/%s/%s/%d.html" % (set, lan, index))
                    
                line = f.read()
                        
                w = open("%s/%s/%d.html"% (set, lan, index), "w")
                w.write(line)
                    
                print 'save %s %d.html'%(set, index)
                            
                f.close()
                w.close()
                time.sleep(1)
                
        
        