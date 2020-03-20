""" import blockchain Libraries. """
import hashlib
import random
import string
import json 
import binascii

"""I'll download these later"""
#import numpy as np 
#import pandas as pd 

import logging
import datetime 
import collections

""" the following are required by PKI. """

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

""" Creating a Client class. """
""" THIS IS THE CLIENT CLASS OF THE BLOCKCHAIN. """

"""GLOBAL VARIABLE FOR TRANSACTIONS"""
transactions = [] 

class Client:
    
    
    def __init__(self):
         random = Crypto.Random.new().read
         self._private_key = RSA.generate(1024, random)
         self._public_key = self._private_key.publickey()
         self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')


"""Dhey = Client()
print ('Dhey your I.d is '+ str(Dhey.identity))"""


""" THIS IS THE TRANSACTION CLASS. IT'S THE BLUEPRINT FOR THE 
    COMPLETE TRANSACTION PROCESS OF THE BLOCKCHAIN. """

class transaction:


    def __init__(self, sender , recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()


    def to_dict(self):

        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({'sender': identity,
                                        'recipient': self.recipient,
                                        'value': self.value,
                                        'time': self.time})

    def sign_transactions(self):
        
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
        
                
def display_transaction(self):

    #for the transaction in transactions
    dict = transaction.to_dict()
    print('sender: '+ dict['sender'])
    print('-'* 77)
    print('recipient: '+ dict['recipient'])
    print('-'*77)
    print('value: '+ str(dict['value']))
    print('-'*77)
    print('time: '+ str(dict['time']))
    print('-'*77)



""" Examples may be deleted later!. """
Dhey = Client()
Tochukwu = Client()
Prime = Client()
Onyi = Client()

""" First transaction """
t = transaction(Dhey,Tochukwu.identity,93.0)

t.sign_transactions()

transactions.append(t)

""" Second transaction"""
t2 = transaction(Dhey,Onyi.identity,35.0)

t2.sign_transactions()

transactions.append(t2)

""" Third transaction"""
t3 = transaction(Dhey,Prime.identity,51.0)

t3.sign_transactions()

transactions.append(t3)

""" Fourth transaction """
t4 = transaction(Tochukwu,Dhey.identity,56.0)

t4.sign_transactions()

transactions.append(t4)

"""Fifth transaction"""
t5 = transaction(Onyi,Tochukwu.identity,87.0)

t5.sign_transactions()

transactions.append(t5)

"""Sixth transaction"""
t6 = transaction(Prime,Onyi.identity,54.0)

t6.sign_transactions()

transactions.append(t6)

for transaction in transactions:
    display_transaction(transaction)
    print('----------')


print(transactions)

#signature = t.sign_transactions()

#print(signature)

""" It ends here. """
    


