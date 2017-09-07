from .extractlink import getlink
import ascii
def greet(name,speaker):
    nametitle = name.title()
    output = ascii.loadFromUrl(getlink(nametitle))
    print(output)
    print(speaker + ' says ' + nametitle +' is handsome')
