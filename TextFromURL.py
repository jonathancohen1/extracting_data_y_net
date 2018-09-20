from urllib.request import urlopen
from bs4 import BeautifulSoup
class TextFromURL:
    
   
    def __init__(self,mainURL):
        self.mainURL = mainURL
    
    def get_text_list(self,return_type):

        # create the BS element from the desired url
        html = urlopen(self.mainURL).read()
        soup = BeautifulSoup(html)

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        raw_text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in raw_text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        if return_type == 'string':
            text = '\n'.join(chunk for chunk in chunks if chunk)
            return text
        else:
            text = []
            for chunk in chunks:
                if chunk:
                    text.append(chunk)
            
            return text
