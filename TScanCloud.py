import time, numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os, sys

cred = credentials.Certificate(os.getcwd()+"/bentenk-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

for i in range(1,4):
	data = {
		u'name':u'Khosyi{}'.format(i*i),
		u'count':10/i
	}
	docRef = db.collection(u'coswar').document(u'invitation{}'.format(i)).set(data)

def pingTest(r=20):
	pings = []
	pingStr = []
	docRef = db.collection(u'players').document(u'red3')
	for i in range(r):
		t0 = time.perf_counter()
		docRef.update({'hp': 1000})
		# print(docRef.get())
		t1 = time.perf_counter()
		ping1 = round((t1 - t0) * 1000, 2)
		pings.append(ping1)
		pingStr.append(str(int(ping1)) + 'ms')
		print('iter:', i)
	print("Average Ping:", np.average(pings), 'ms')
	print("Max:", max(pings), 'ms')
	print("Min:", min(pings), 'ms')

def createCloud(cname, doc, data):
	dbase = db.collection(u'{}'.format(cname)).document(u'{}'.format(doc)).set(data)
	print(f'Cloud Database Created!\n collection\t: {cname}\n Document\t: {doc}')

def updateCloud(cname, doc):
	dbase = db.collection(u'coswar').document(u'{}'.format(doc))
	dbase.update()