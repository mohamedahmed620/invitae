#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 07:51:52 2021

@author: mohamed.ahmed
"""

import pandas as pd
import json
import os
#pip install requests
#conda install requests
import requests
length_test = False

barcode = ""
#os.chdir('/Users/RagwaElsayed/Documents/verso project/')
os.chdir('/Users/mohamed.ahmed/Documents/verso project/')

# Reading the json as a dict
with open("9_16_2021.json") as json_data:
    data = json.load(json_data)
# do while loop to confirm getting a good barcode  
while length_test == False :
    
    print("please pick up a tube from rack and enter barcode number")
    barcode = input()
    if  len(barcode) == 10:
        length_test = True
    
#print ("please pick up a tube from rack and enter barcode number")
#barcode = input()
#print (len(barcode))
#url = https://lims.locusdev.net/rd_tools/audit_trail/barcode/
#response = requests.get("url")
new = {}
new["verso_pickjob_id"]=''
new["task_batch_id"]=''
new["tube_rack_id"]=''
new["assay_id"]=''
new["assay_plate_id"]=''
new["batch_selection_workflow"]= 'null'
new["retrieve_and_stamp_workflow"]=''
new["scanfile_name"]=''
new["spec_name"]='null'
new["stamped_unp_1_id"]= 'null'
new["retrieve_and_stamp_request_id"]=''
new["retrieve_and_stamp_spec_type"]= 'Retrieve and Stamp'
new["retrieve_and_stamp_versioned_name"]= 'retrieve_and_stamp_v1.1'
new["dilution_worklist_name"]=''
new["timestamp_enter"]=''
new["timestamp_exit"]=''
new["purpose"]= 'null'
new["status"]='active1'





#df = pd.read_json("/Users/mohamed.ahmed/Documents/verso project/9_16_2021.json")
#print(df.length())

#my key is operation_data_stamp'

data['operation_data_stamp'].append(new)
#print (operation_data_stamp)

print (data["operation_data_stamp"][-1])
