import pickle

def userLevel(tweets):
    pickle_in = open("modelbasic.pkl","rb")
    classifier=pickle.load(pickle_in)

    depression = classifier.predict(tweets)

    if(depression[0]>0.5):
        depression="Depressed"
    else:
        depression="Not Depressed"

    return depression