import time, random, requests
import DAN

ServerURL= 'http://140.114.77.90:9999'#with non-secure connection
Reg_addr= '7788'#if None, Reg_addr= MAC address

DAN.profile['dm_name']='109062599_DM'
DAN.profile['df_list']=[ 'str0','str1', 'str2']
#DAN.profile['d_name']= 'Assign a Device Name'

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister() #if you want to deregister this device, uncomment this line
# #exit() #if you want to deregister this device, uncomment this line

while True:
    try:
        a=input("input??")
        b = a.split(' ')
        if b[0]=="0":
            print("0")
            DAN.push('str0',b[1])
        if b[0]=="1":
            print("1")
            DAN.push('str1',b[1])
         #Push data to an input device feature "Status"
        #==================================
        ODF_data= DAN.pull('str2') #Pull data from an output device feature "Name-O"
        if ODF_data != None:
            print(ODF_data)
    except Exception as e:
        print(e)
        if str(e).find('mac_addrnot found:') != -1:
            print('Reg_addris not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknown reasons.')
            time.sleep(1)
    time.sleep(0.2)
