from uk.ac.ebi.core.brain import Brain

b = Brain()
b.learn("http:purl.obo.obolibrary.org/obo/pato.owl")
b.getSubClasses("Thing", 0)
print len(b)
