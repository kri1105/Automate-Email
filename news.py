#API key : 2baa915abd4c476abfa326fe5873ede0
import requests

class NewsFeed:

    """ Representing the news title and links as a single string
    """
    
    base_url="https://newsapi.org/v2/everything"
    api_key="2baa915abd4c476abfa326fe5873ede0"

    def __init__(self,intrest,from_date,to_date,language='en'):
        self.intrest=intrest
        self.from_date=from_date
        self.to_date=to_date
        self.language=language

    
    def get(self):   
        url = f"{self.base_url}?qInTitle={self.intrest}&from={self.from_date}&to={self.to_date}&sortBy={self.language}&apiKey={self.api_key}"

        response=requests.get(url)
        content = response.json()
        articles = content['articles']
        email_body=''

        for article in articles:
            email_body=email_body+ article['title']+"\n"+article['url']+"\n\n"
        
        return email_body


if __name__=='__main__':
    newsFeed = NewsFeed('nasa','2025-01-12','2025-01-13','en')
    print(newsFeed.get())


                             