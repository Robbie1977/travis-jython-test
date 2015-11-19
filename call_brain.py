from uk.ac.ebi.brain.core import Brain

b = Brain()
b.learn("http://purl.obolibrary.org/obo/pato.owl")
b.getSubClasses('Thing', 0)
print "PATO has %s classes" % len(list(b))
