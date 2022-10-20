import spacy

nlp = spacy.load("en_core_web_lg")

w1 = "red"
w2 = "Red"  # "read" = -0.00014783155126171907 # "RED" = 0.1933490277053573
# "yellow" = 0.8282849235014055 # "color" = 0.5155265927314758  # "red" = 1.0  # "walking"= 0.18171407282352448

w1 = nlp(w1)  # w1 = nlp.vocab[w1]
w2 = nlp(w2)  # w2 = nlp.vocab[w2]

print(w1.similarity(w2))

s1 = nlp("how old are you?")
s2 = nlp("what is your age?")

print(s1.similarity(s2))  # 0.7114367972402682
print(s2.similarity(s1))

w3 = "old"
w4 = "age"

w3 = nlp(w3)  # w1 = nlp.vocab[w1]
w4 = nlp(w4)  # w2 = nlp.vocab[w2]

print(w3.similarity(w4))  # 0.47923737364079194

w3 = "how"
w4 = "what"

w3 = nlp(w3)  # w1 = nlp.vocab[w1]
w4 = nlp(w4)  # w2 = nlp.vocab[w2]

print(w3.similarity(w4))  # 0.7147836023901577

