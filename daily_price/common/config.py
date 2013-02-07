
import os, sys, time, urllib

rarity = ['Mythic Rare', 'Rare', 'Uncommon', 'Common', 'Land']

language = ['en', 'tw']

star_city_set_number = {'isd' : 5215, 'dka' : 5221, 'avr' : 5228, 'm13': 5241, 'rtr' : 5243, 'gtc' : 5249}

card_set = ['isd', 'dka', 'avr', 'm13', 'rtr', 'gtc']

flip = {
    'isd' : 20,
    'dka' : 13
}

card_num = {
    'isd' : {'Mythic Rare' : 17, 'Rare' : 65, 'Uncommon' : 74, 'Common' : 113, 'Land' : 15, 'Token' : 12},
    'dka' : {'Mythic Rare' : 14, 'Rare' : 41, 'Uncommon' : 48, 'Common' :  68, 'Land' :  0, 'Token' :  3},
    'avr' : {'Mythic Rare' : 15, 'Rare' : 53, 'Uncommon' : 60, 'Common' : 101, 'Land' : 15, 'Token' :  8},
    'm13' : {'Mythic Rare' : 15, 'Rare' : 53, 'Uncommon' : 60, 'Common' : 101, 'Land' : 20, 'Token' : 11},
    'rtr' : {'Mythic Rare' : 15, 'Rare' : 53, 'Uncommon' : 80, 'Common' : 101, 'Land' : 25, 'Token' : 12},
    'gtc' : {'Mythic Rare' : 15, 'Rare' : 53, 'Uncommon' : 80, 'Common' : 101, 'Land' :  0, 'Token' : 12} 

}

total_num = {
    'isd' : 264,
    'dka' : 158,
    'avr' : 244,
    'm13' : 249,
    'rtr' : 274,
    'gtc' : 249,
}

tcg_set_string = {
    'isd' : 'innistrad',
    'dka' : 'dark-ascension',
    'avr' : 'avacyn-restored',
    'm13' : 'Magic-2013-(M13)',
    'rtr' : 'return-to-ravnica',
    'gtc' : 'gatecrash'
    
}

date_string = time.strftime("%Y_%m_%d")

def get_table(set):
    f = open('../common/card_name_table/%s.txt'%set, 'r')
    table = []
    for line in f:
        table.append(line.strip('\n'))
        
    return table
    
