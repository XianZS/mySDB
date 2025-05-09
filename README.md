# 1.mySDB

&emsp;&emsp;mySDB(My Simple DataBase)

&emsp;&emsp;Developed in python, a simple database based on sqlite. You can quickly get started after downloading with pip. It is aimed at beginners.

# 2.Meaning

&emsp;&emsp;In mySDB, my stands for user, S stands for simple, and DB stands for database.

# 3.Develop a narrative

## (1).Why should I develop this project?

&emsp;&emsp;In a traditional project, if you call the database through python code (MySQL is used as an example), you need to install some third-party libraries, but in this process, the call may not be successful due to problems such as version mismatch and feature loss, and the time for debugging errors may be much greater than the time consumed in developing a small project.

&emsp;&emsp;I don't think it's appropriate to spend a lot of time debugging when developing a small project, which will slow down the efficiency and even affect the motivation of beginners to learn the project. When a beginner builds the root of the project, and then spends time configuring the MySQL database on the local computer, and wants to call the MySQL database through python, he downloads the relevant third-party package, but the call cannot be successfully made due to problems such as version mismatch, which will reduce the beginner's interest in learning.

## (2).The underlying architecture of the project

&emsp;&emsp;This project is developed based on the 'Python' language, and the underlying implementation is mainly 'sqlite3'.

## (3)Design Ideas & Highlights

* You can download this package through pip and use it directly, without any configuration and setting of environment variables

* You can customize the storage path settings for each database

* The design pattern is 'DBUT(Database-User-Table)', which is detached from the traditional database design pattern, and uses Database as the main body to completely divide Users into Databases, and does not completely divide Tables into Users, which is convenient for permission management and data search.

# 4.Design patterns[`DBUT`]

\- DataBase-1

&emsp;- User-1

&emsp;&emsp;- Table-1.1

&emsp;&emsp;- Table-1.2

&emsp;&emsp;- Table-1.3

&emsp;- User-2

&emsp;&emsp;- Table-2.3

&emsp;&emsp;- Table-2.3

&emsp;&emsp;- Table-2.3

&emsp;- User-3

\- DataBase-2

\- DataBase-3


&emsp;&emsp;In the above structure, I have created three databases named 'Database-1', 'Database-2', 'Database-3', under 'Database-1' there are three users 'User-1', 'User-2', 'User-3', and under 'User-1' there are three tables 'Table-1.1', 'Table-1.2', 'Table-1.3', and the same goes for 'User-2' There are also several tables under it, and in this design mode, the database, users, and tables are clearly divided, which is convenient for the rapid development of small projects.