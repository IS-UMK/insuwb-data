#!/usr/bin/env python
import os, sys, glob, subprocess
path = '19.09.2017_16.20/'

def clean_dir(path):
    os.system('rm %s*.csv' % path)
    os.system('rm %s*.bin' % path)
    os.system('rm %s*.gz' % path)
    os.system('rm %s*.txt' % path)

def prepare_data(path):
    gz_names = glob.glob(path+'*.gz')
    txt_names = glob.glob(path+'*.txt')
    for each in gz_names:
        #subprocess.call(['zcat', each, '>', each.strip('.gz')])
        os.system("zcat %s > %s" % (each, each.strip('.gz')))
        each.strip('.gz')
        subprocess.call(['python', '../../recorder/recorder_ble/decode_bin.py', each.strip('.gz'), each.strip('_ins.bin.gz')+'.csv'])
        os.system("zip %s %s" %(each.strip('_ins.bin.gz')+'.csv.zip', each.strip('_ins.bin.gz')+'.csv'))
    for each in txt_names:
        os.system("zip %s %s" % (each + '.zip', each))
    clean_dir(path)
def do_for_all(path = '.'):
    dir_list = os.listdir(path)
    for each in dir_list:
        if os.path.isdir(each):
            prepare_data(each+'/')
if __name__ == '__main__':
    #do_for_all()
    prepare_data(path)
    pass
