sqlite> .open internship.db
sqlite> CREATE TABLE interns (
(x1...>     id INTEGER PRIMARY KEY,
(x1...>     name TEXT,
(x1...>     track TEXT,
(x1...>     stipend INTEGER
(x1...> );
sqlite> INSERT INTO interns (id, name, track, stipend) VALUES
   ...> (01,'Deepa', 'Data Science', 15000),
   ...> (02,'Rahul', 'Web Dev', 12000),
   ...> (03,'Anjali', 'Data Science', 18000),
   ...> (04,'Kiran', 'Cloud', 16000),
   ...> (05,'Meena', 'Web Dev', 14000);
sqlite> .mode column
sqlite> .headers on
sqlite> SELECT name, track FROM interns;
name    track
------  ------------
Deepa   Data Science
Rahul   Web Dev
Anjali  Data Science
Kiran   Cloud
Meena   Web Dev
sqlite> SELECT * FROM interns;
id  name    track         stipend
--  ------  ------------  -------
1   Deepa   Data Science  15000
2   Rahul   Web Dev       12000
3   Anjali  Data Science  18000
4   Kiran   Cloud         16000
5   Meena   Web Dev       14000
