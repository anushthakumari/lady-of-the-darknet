import parsers.omega_p as omega_p
import parsers.threeam as threeam
import parsers.danon as danon

class __Tags():
    omega = omega_p.TAG
    threeam = threeam.TAG
    danon = danon.TAG

TAGS = __Tags()

def parse(tag="", res_text=""):
    if tag == omega_p.TAG:
        return omega_p.parse(res_text)
    
    if tag == threeam.TAG:
        return threeam.parse(res_text)
    
    if tag == danon.TAG:
        return danon.parse(res_text)