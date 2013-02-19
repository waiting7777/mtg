# -*- coding: utf-8 -*- 

import os

execfile(os.getcwd() + "/common/config.py")

if len(sys.argv) < 2:
    print 'please input card_set'
    exit()
    
if sys.argv[1] not in card_set:
    print 'please input supportted card_set'
    print card_set
    exit()
    
set = sys.argv[1]

if os.path.exists("card_data") == False:
    os.mkdir("card_data")

if os.path.exists("card_data/%s"%(set)) == False:
    os.mkdir("card_data/%s"%(set))

for lan in language:    
    if os.path.exists("card_data/%s/%s"%(set, lan)) == False:    
        os.mkdir("card_data/%s/%s"%(set, lan))

    if os.path.exists("card_data/%s/%s_%s_all.html"%(set, set, lan)) == False:
    
        f = urllib.urlopen("http://magiccards.info/%s/%s.html"%(set, lan))
        line = f.read()
        
        w = open("card_data/%s/%s_%s_all.html"%(set, set, lan), "w")
        w.write(line)
        print "%s/%s_%s_all.html"%(set, set, lan)
        
        f.close()
        w.close()
        
    for i in range(total_num[set]):
    
        index = i + 1
        print index
        
        # isd dka
        if set == 'isd' or set == 'dka':
            
            if index in flip[set]:

                if os.path.exists("card_data/%s/%s/%da.html"% (set, lan, index)) == False:
            
                    fa = urllib.urlopen("http://magiccards.info/%s/%s/%da.html" % (set, lan, index))
                    fb = urllib.urlopen("http://magiccards.info/%s/%s/%db.html" % (set, lan, index))
                    
                    linea = fa.read()
                    lineb = fb.read()
                    
                    wa = open("card_data/%s/%s/%da.html"% (set, lan, index), "w")
                    wb = open("card_data/%s/%s/%db.html"% (set, lan, index), "w")
                    
                    wa.write(linea)
                    wb.write(lineb)
                
                    print 'save %s %d.html'%(set, index)
                    
                    fa.close()
                    fb.close()
                
                    wa.close()
                    wb.close()
                    
            else:
            
                if os.path.exists("card_data/%s/%s/%d.html"% (set, lan, index)) == False:
                
                    f = urllib.urlopen("http://magiccards.info/%s/%s/%d.html" % (set, lan, index))
                        
                    line = f.read()
                            
                    w = open("card_data/%s/%s/%d.html"% (set, lan, index), "w")
                    w.write(line)
                        
                    print 'save %s %d.html'%(set, index)
                                
                    f.close()
                    w.close()
                    
        else:
            if os.path.exists("card_data/%s/%s/%d.html"% (set, lan, index)) == False:
                
                f = urllib.urlopen("http://magiccards.info/%s/%s/%d.html" % (set, lan, index))
                    
                line = f.read()
                        
                w = open("card_data/%s/%s/%d.html"% (set, lan, index), "w")
                w.write(line)
                    
                print 'save %s %d.html'%(set, index)
                            
                f.close()
                w.close()
                # time.sleep(1)
                
        
        