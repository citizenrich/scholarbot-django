import re
import urllib
# import urlparse <- python2
import urllib.parse


class DOITools(object):

        def __init__(self, address):
            self.address = address

        def extract_from_url(self):
            """
            extract DOI from either url path or query params
            """
            w = urllib.unquote(self.address)
            x = urlparse.urlparse(w)
            regex = r"10.\d{4,9}/[^\s]+$"
            y = re.search(regex, x.path)
            z = re.search(regex, x.query)
            if y:
                doi = y.group(0)
                return doi
            elif z:
                doi = z.group(0)
                return doi
            else:
                doi = ''
                return doi

# tests
# c = DOITools('http://www.tandfonline.com/doi/full/10.1080/00472336.2016.1178796?ai=z4&mi=3fqos0&af=R')
# print c.extract_from_url()
# s = DOITools('http://www.tandfonline.com/doi/full/10.1080/1554477X.2016.1192435')
# print s.extract_from_url()
# h = DOITools('http://onlinelibrary.wiley.com/resolve/doi?DOI=10.1111%2Finr.12258')
# print h.extract_from_url()
