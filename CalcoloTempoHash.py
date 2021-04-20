#!/usr/bin/env python3
# coding: utf-8

# In[1]:


import logging
import sys
import numpy as np 
import pandas as pd
import hashlib
from timeit import default_timer as timer
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('LOGGER_NAME')
logger.info('Start Calcolo Tempo Trascorso')


# In[2]:

path = 'c:/Users/gam/Documents/GitHub/Cambium-Anomaly-Classificator/hash/'

dataMac = path+'XY_data_ctc_UMAC.csv'
colX = ['MAC']
dtypes = {'MAC':'str'}

X_data_MAC = pd.read_csv(dataMac, sep = ',', names= colX, dtype=dtypes, encoding='utf-8') 
#print(X_data_MAC.info())
#print(X_data_MAC.shape)
#print(X_data_MAC)

# DeviceName
dataDeviceName = path+'XY_data_ctc_UDeviceName.csv'
colX = ['Device Name']
dtypes = {'Device Name':'str'}

X_data_DeviceName = pd.read_csv(dataDeviceName, sep = ',', names= colX, dtype=dtypes, encoding='utf-8') 
#print(X_data_DeviceName.info())
#print(X_data_DeviceName.shape)
#print(X_data_DeviceName)

# CODCLIENTE
dataCODCLIENTE = path+'XY_data_ctc_UCODCLIENTE.csv'
colX = ['COD. CLIENTE']
dtypes = {'COD. CLIENTE':'str'}

X_data_CODCLIENTE = pd.read_csv(dataCODCLIENTE, sep = ',', names= colX, dtype=dtypes, encoding='utf-8') 
#print(X_data_CODCLIENTE.info())
#print(X_data_CODCLIENTE.shape)
#print(X_data_CODCLIENTE)

# COMUNEINSTALLAZIONE
dataCOMUNEINSTALLAZIONE = path+'XY_data_ctc_UCOMUNEINSTALLAZIONE.csv'
colX = ['COMUNE INSTALLAZIONE']
dtypes = {'COMUNE INSTALLAZIONE':'str'}

X_data_COMUNEINSTALLAZIONE = pd.read_csv(dataCOMUNEINSTALLAZIONE, sep = ',', names= colX, dtype=dtypes, encoding='utf-8') 
#print(X_data_COMUNEINSTALLAZIONE.info())
#print(X_data_COMUNEINSTALLAZIONE.shape)
#print(X_data_COMUNEINSTALLAZIONE)


# In[3]:


def encrypt_string(hash_string):
     sha_signature =          hashlib.sha256(hash_string.encode()).hexdigest()
     return sha_signature


# In[4]:


print("Start Tempo: ")
start = timer()
#
MACRIPTO = []

for row in X_data_MAC['MAC']:    
    temp = (str(row))
    #print("original string: ", temp)
    encMessage = encrypt_string(temp)
    #print("encrypted string: ", encMessage)    
    #MACRIPTO.append(encMessage)
    
#X_data_MAC['MAC_CRIPTO_HASH'] = MACRIPTO

#
DeviceNameCRIPTO = []

for row in X_data_DeviceName['Device Name']:    
    temp = (str(row))
    #print("original string: ", temp)
    encMessage = encrypt_string(temp)
    #print("encrypted string: ", encMessage)    
    #DeviceNameCRIPTO.append(encMessage)
    
#X_data_DeviceName['Device Name_HASH'] = DeviceNameCRIPTO

#
CODCLIENTECRIPTO = []

for row in X_data_CODCLIENTE['COD. CLIENTE']:    
    temp = (str(row))
    #print("original string: ", temp)
    encMessage = encrypt_string(temp)
    #print("encrypted string: ", encMessage)    
    #CODCLIENTECRIPTO.append(encMessage)
    
#X_data_CODCLIENTE['COD. CLIENTE_HASH'] = CODCLIENTECRIPTO

#
COMUNEINSTALLAZIONECRIPTO = []

for row in X_data_COMUNEINSTALLAZIONE['COMUNE INSTALLAZIONE']:    
    temp = (str(row))
    #print("original string: ", temp)
    encMessage = encrypt_string(temp)
    #print("encrypted string: ", encMessage)    
    #COMUNEINSTALLAZIONECRIPTO.append(encMessage)
    
#X_data_COMUNEINSTALLAZIONE['COMUNE INSTALLAZIONE_HASH'] = COMUNEINSTALLAZIONECRIPTO


end = timer()
print("Tempo Trascorso:", end - start)


# In[5]:

'''
print(X_data_MAC.info())
print(X_data_MAC.shape)
print(X_data_MAC)

print(X_data_DeviceName.info())
print(X_data_DeviceName.shape)
print(X_data_DeviceName)

print(X_data_CODCLIENTE.info())
print(X_data_CODCLIENTE.shape)
print(X_data_CODCLIENTE)

print(X_data_COMUNEINSTALLAZIONE.info())
print(X_data_COMUNEINSTALLAZIONE.shape)
print(X_data_COMUNEINSTALLAZIONE)
'''

# In[ ]:




