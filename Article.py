import csv
from TextFromURL import TextFromURL

class Article:
    #TODO Create a Class for "PAGE"
    #TODO Class will include the following attributes:
    '''
    1. page address - link
    2. location of the scraped data file
    3. article's basic data:
        #date
        #name of writer/reporter
        #section 
        #Title
    '''
    '''
    def __init__(self,link , title = None, author = None, date = None, section = None):
        self.link = link
        self.title = title 
        self.author = author
        self.date = date
        self.section = section
        self.path_to_file = "/home/jonathan/Documents/Gathering Data Proj/webdata/"+str(self.title)+".csv"
        self.linked_articles = []
        
'''
    def __init__(self,link):
        self.link = link
        self.title = None 
        self.author = None
        self.date = None
        self.section = None
        self.path_to_file = None
        self.linked_articles = []
    

    def get_data(self):

        url= TextFromURL(self.link)
        raw_article_data = url.get_text_list(return_type = "list")
        self.title = raw_article_data[0]
        self.path_to_file = "/home/jonathan/Documents/Gathering Data Proj/webdata/"+str(self.title)+".csv" 
        self.set_section_date(raw_article_data[1:])
        return raw_article_data[1:]

    def create_dict(self):

        raw_article_data = self.get_data()
        dictionary = {"title":self.title ,"author":self.author, "date":self.date, "section":self.section,"article data":raw_article_data}
        return dictionary
    
    def create_file(self):
        
        dictionary = self.create_dict()
        with open(self.path_to_file, "w") as csv_file:
            writer = csv.writer(csv_file,delimiter=':')
            for key, value in dictionary.items():
                writer.writerow([key, value])
    
    def set_section_date(self,raw_article_data):

        section = None
        date = None
        for i in range(len(raw_article_data)) :
                if "אתר נגיש" in raw_article_data[i] and section == None:
                    section = i
                if "פורסם" in raw_article_data[i] and date == None:
                    date = i
                
        section = raw_article_data[section]
        section = section.split(" ")[1][4:]
        date = raw_article_data[date].split(" ")
        for i in range(len(date)):
            if "פורסם" in date[i]:
                pos = i
        for i in range(pos,len(date)):
            if "." in date[i]:
                self.date = date[i]
        self.section = section

    def get_data_as_dict(self):

        with open(self.path_to_file, 'r') as csv_file:
            reader = csv.reader(csv_file,delimiter=':')
            return dict(reader)

    def add_linked_article(self,linked_article):
        
        if type(linked_article) == "Article":
            self.linked_articles.append(linked_article)
        else:
            return "Error: given input type is NOT $Article$ "
    