#Task-1
sqlite> .open internship.db
sqlite> SELECT *
   ...> FROM interns
   ...> WHERE track = 'Data Science'
   ...> AND stipend > 5000;
1|Deepa|Data Science|15000
3|Anjali|Data Science|18000
sqlite> .mode column
sqlite> .headers on
sqlite> SELECT *
   ...> FROM interns
   ...> WHERE track = 'Data Science'
   ...> AND stipend > 5000;
id  name    track         stipend
--  ------  ------------  -------
1   Deepa   Data Science  15000
3   Anjali  Data Science  18000
sqlite> SELECT track, AVG(stipend) AS avg_stipend
   ...> FROM interns
   ...> GROUP BY track;
track         avg_stipend
------------  -----------
Cloud         16000.0
Data Science  16500.0
Web Dev       13000.0
sqlite> SELECT track, COUNT(*) AS total_interns
   ...> FROM interns
   ...> GROUP BY track;
track         total_interns
------------  -------------
Cloud         1
Data Science  2
Web Dev       2

#Task-2
sqlite> .open internship.db
sqlite> CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
);
sqlite> INSERT INTO mentors (mentor_name, track) VALUES
('Dr. Sharma', 'Data Science'),
('Ms. Priya', 'Web Dev'),
('Mr. Arjun', 'Cloud');
sqlite> SELECT * FROM mentors;
1|Dr. Sharma|Data Science
2|Ms. Priya|Web Dev
3|Mr. Arjun|Cloud
sqlite> .mode column
sqlite> .headers on
sqlite> SELECT * FROM mentors;
mentor_id  mentor_name  track
---------  -----------  ------------
1          Dr. Sharma   Data Science
2          Ms. Priya    Web Dev
3          Mr. Arjun    Cloud
sqlite> SELECT interns.name,
   ...>        interns.track,
   ...>        mentors.mentor_name
   ...> FROM interns
   ...> INNER JOIN mentors
   ...> ON interns.track = mentors.track;
name    track         mentor_name
------  ------------  -----------
Deepa   Data Science  Dr. Sharma
Rahul   Web Dev       Ms. Priya
Anjali  Data Science  Dr. Sharma
Kiran   Cloud         Mr. Arjun
Meena   Web Dev       Ms. Priya

#Jupyter notebook
import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")

query = """
SELECT interns.name,
       interns.track,
       mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

df = pd.read_sql_query(query, conn)

df
