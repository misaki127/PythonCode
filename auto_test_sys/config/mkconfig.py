#encoding:utf-8

import configparser

def read_config(filename):
    config_data = {}
    cf = configparser.ConfigParser()
    cf.read(filename)
    sec_list = cf.sections()
    for i in sec_list:
        item_list = cf.items(i)
        config_data[i]=item_list

    return config_data

def write_config(filename,config_data):
    cf = configparser.ConfigParser()
    for a in config_data.keys():
        cf.add_section(a)
        for b in config_data[a]:
            cf.set(a,b[0],b[1])

    with open(filename,'w+') as f:
        cf.write(f)

