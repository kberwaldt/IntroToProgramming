import psycopg2

DBNAME = 'news'


def popular_articles():
    """Prints What are the most popular three articles of all time?"""

    print "What are the most popular three articles of all time?"

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        SELECT *
        FROM popular_articles
        ORDER BY Views DESC
        LIMIT 3;
    """)
    articles = c.fetchall()
    db.close()

    for result in articles:
        print "Article - %s | Views - %s" % (result[0], result[1])


def popular_articles_authors():
    """Prints Who are the most popular article authors of all time?"""

    print "Who are the most popular article authors of all time?"

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        SELECT authors_articles.name, SUM(popular_articles.views) AS views
        FROM authors_articles, popular_articles
        WHERE authors_articles.title = popular_articles.title
        GROUP BY authors_articles.name
        ORDER BY views DESC;
    """)

    authors = c.fetchall()
    db.close()

    for result in authors:
        print "Author - %s | Views - %s" % (result[0], result[1])


def error_requests():
    """Prints On which days did more than 1% of requests lead to errors?"""

    print "On which days did more than 1% of requests lead to errors?"

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        SELECT total_pageloads.day,
            ROUND(((error_pageloads.totals*1.0
                / total_pageloads.totals*1.0)
                    * 100),
                        1) AS errors
        FROM total_pageloads, error_pageloads
        WHERE total_pageloads.day = error_pageloads.day
        AND ((error_pageloads.totals*1.0
            / total_pageloads.totals*1.0)
                * 100) > 1;
    """)

    errors = c.fetchall()
    db.close()

    for result in errors:
        print "%s | %s" % (result[0], result[1])

if __name__ == '__main__':
    popular_articles()
    print "\n"
    popular_articles_authors()
    print "\n"
    error_requests()
