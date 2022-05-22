# College-s-Residential-Options
1. Objective of Project 
To find out the frequency of students commenting on the 
subreddit: r/nus on Reddit on the different Residential Options 
that are available in campus from 1 May – 1 June 2021.

2. Target Audience
Incoming freshmen and Seniors whom are interested in applying 
for campus residences in AY21/22.

3. Background
Due to COVID-19, it has been difficult for incoming freshman or 
current undergraduates to find out about the popularity of the 
different residential options among students as there are limited 
social interactions to find out a rough estimate for it. Even though 
polls can be easily conducted, the sample size may be small and 
several students might not be truthful while reporting the 
numbers.

4. Goals and Benefits
Students will be better informed of the popularity of the various 
residential options and may consider alternative options (Less 
popular Residential Options, Off-campus residences etc.) in the 
case of their unsuccessful application due to high demand, based 
on the findings.

5. Methodology
a. Using the period of 1 May – 1 June 2021 as there is a 
huge influx of new and current Undergraduates
discussing/commenting on the residential options as it is 
during the 1st round of Application for freshmen.
b. (casmida_p1.py) Using Pushshift API to gather large 
amount of Reddit comments and create a dataset from 
the period of time that was mentioned above for the 
subreddit r/nus. Pushshift is a service that take in 
comments from Redit, stores them in a database, and 
making them available for use via an API endpoint.
c. While using Python 3.7.8, importing the pandas and 
pmaw library, search_comments were used to request 
Reddit comments from Pushshift within the date range
and pandas to retrieve the comments data.
d. The Reddit data will then be stored locally and will be 
saved as a CSV file named “nus_comments.csv”
e. (casmida_p2.py) Counting the number of word frequency 
from the column “body” in “nus_comments.csv” which is 
the column with the comments. Thereafter, making use of
matplotlib library that was imported to plot a pie chart to 
represent the figures such that it is easier to interpret the 
results by the reader.
