
import firebase_admin
from firebase_admin import firestore


def main():
    firebase = firebase_admin.initialize_app(options={ 'projectId': 'test1kharayo' })
    db = firestore.client()
    db.collection(u'featured_news').document(u'Onlinekhabar') \
            .set({'title':'ABC', 'excrept': 'abc', 'url':'abc'})

    ref = db.collection(u'featured_news')

    for doc in ref.stream():
        print(u'{} => {}'.format(doc.id, doc.to_dict()))

main()
