from firebase_admin import firestore,credentials,initialize_app
cred=credentials.Certificate('firebae-adminsdk.json')
db=initialize_app(cred)
db=firestore.client()
entrepreneurs=db.collection('Entrepreneurs').stream()
ens=[doc.to_dict() for doc in entrepreneurs]
print(ens)