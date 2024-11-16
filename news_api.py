from gdeltdoc import GdeltDoc, Filters
from newspaper import Article

# GDELT API를 이용해보는 실습 파일

f = Filters(
    start_date = "2024-05-01",
    end_date = "2024-05-25",
    num_records = 10,
    keyword = "Microsoft",
    domain = "nytimes.com",
    country = "US",
)

gd = GdeltDoc()

# Search for articles matching the filters
articles = gd.article_search(f)

url = articles.loc[1, "url"]
print(articles.loc[1, "title"])
print("---------------------")

article = Article(url)
article.download()
article.parse()
print(article.text)