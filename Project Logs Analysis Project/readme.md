# Log Analysis Project
Reporting tool that prints out reports (in plain text) based on the data in the database

Command Line tool prints out three reports for the following:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Getting Started
This project used the FSND-Virtual-Machine provided by Udacity for Back-End development.
### Software Requirements
Python 2.6.X
PostgreSQL 9.5.8

## Data
Download and unzip [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
Load the data by using the command ```psql -d news -f newsdata.sql```

## Views
- The Python code relies on the following views to be created.
- Connect to the database '''psql -d news'''

'''
CREATE VIEW popular_articles AS
SELECT articles.title,
COUNT(log.path) AS views
FROM articles
LEFT JOIN log ON '/article/' || articles.slug = log.path
GROUP BY articles.title

CREATE VIEW authors_articles AS
select articles.title, authors.name
from articles, authors
where articles.author = authors.id;

CREATE view error_pageloads as
SELECT date(TIME) AS day,
count(status) as totals
FROM log
WHERE status = '404 NOT FOUND'
GROUP by day;

CREATE view total_pageloads as
SELECT date(TIME) AS day,
count(status) as totals
FROM log
GROUP by day;
'''

## Run Python Code
From the terminal '''python LogAnalysisProject.py'''

### Expected output ###
'''
What are the most popular three articles of all time?
Article - Candidate is jerk, alleges rival | Views - 338647
Article - Bears love berries, alleges bear | Views - 253801
Article - Bad things gone, say good people | Views - 170098


Who are the most popular article authors of all time?
Author - Ursula La Multa | Views - 507594
Author - Rudolf von Treppenwitz | Views - 423457
Author - Anonymous Contributor | Views - 170098
Author - Markoff Chaney | Views - 84557


On which days did more than 1% of requests lead to errors?
2016-07-17 | 2.3
'''
