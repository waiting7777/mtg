# -*- coding: utf-8 -*- 

execfile("card_name_table/rtr.txt")

f = open('template.html', 'r')

page = f.read()

f.close()

for key in info:
    
    w = open('html/rtr/%d.html'%(info[key]['card_number']), 'w')
    w.write(page.replace('fqfrank', '\"'+key.replace("'", "@")+'\"'))
    w.close()