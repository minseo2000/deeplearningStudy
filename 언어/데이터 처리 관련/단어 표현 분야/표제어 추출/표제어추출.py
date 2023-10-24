import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u"he was running late")
for token in doc:
    print('{} --> {}'.format(token, token.lemma_))

