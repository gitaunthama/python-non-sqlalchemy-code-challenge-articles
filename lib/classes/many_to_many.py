class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        Article.all.append(self)

# without decorators
    def get_title(self):
        return self._title

    def set_title(self, title):
         if isinstance(title,str):
             return ;self._title = title
         else:
            "Title musy be a string"


    title = property(get_title, set_title)
        
       
    
        
class Author:
    def __init__(self, name):
        self._name = name
# with decorator
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        return self._name

    def articles(self):
        
            return [article for article in Article.all if article.author == self]

    def magazines(self):
       
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article
        

    def topic_areas(self):
        topic_areas = list(set([article.magazine.category for article in self.articles()]))
        return topic_areas if topic_areas else None


class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category
        


    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @name.setter
    def name (self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
    


    def articles(self):
        
        return [article for article in Article.all if article.magazine == self]

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None


    def contributors(self):
        unique_authors = set()
        for article in self.articles():
         unique_authors.add(article.author)
        return list(unique_authors)
    
    def contributing_authors(self):
        authors_count = {}
        for article in self.articles():
            author = article.author
            if author in authors_count:
                authors_count[author] += 1
            else:
                authors_count[author] = 1
        contributing_authors = [author for author, count in authors_count.items() if count > 2]
        return contributing_authors if contributing_authors else None