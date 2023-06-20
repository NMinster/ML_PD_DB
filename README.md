# ML_PD_DB
**Machine Learning Parkinson's Disease Database**

There is a need for an up-to-date database with genes identified in machine-learning studies. This repository is in progress. 

**Steps Needed**
1. Set up an Amazon RDS instance

2. Design your database schema:
One table for the genes themselves and another for the studies where they were associated with Parkinson's disease. Other information that may be included:

-gene identifier, the associated study, association details (e.g. effect size, p-value, or any other measure of statistical significance), gene description, protein information, and variants. 

5. Create a Web Application: Python (Flask or Django) maybe JavaScript (Node.js). 

6. Implement a Search Feature.

7. Host the Web Application on Amazon EC2.
   
9. Connect Web Application to the RDS Instance: use the AWS SDK library to connect to your RDS instance.

9. Use Amazon Route 53 to set up a domain or request university permission. 
