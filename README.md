
# Patient Care Record

# Search Details of Patient from SAR_Incident_No:
1.	Based on the SAR_Incident_No, currently we can retrieve:
	Symptoms
	Allergies
	Past History
	Medications
	Last Meals
 Login and Logout is made available.


# Remaining Features:

# 2.	Alert for delay in Assessment.
1.	Whenever a patient record is reviewed an alert timer is started waiting for Rescue specialist to mention if immediate assistance is provided. 
2.	For simplicity, he can add atleast the medication given for first time. 
3.	If the timer goes out and no assistance is provided and rescue specialist is unable to update the medication details within alert time limit then that record of patient will get added to list of unattended patients for future review. 
4.	This way the list can be reviewed and the patient could be attended. 

# Code Implementation:
1.	For alert timer, we have implemented using javascript. 
2.	A post form is provided to submit and update our database. 
3.	In case the timer goes out a warning is provided stating that you have crossed the alert time limit to attend the patient. 
4.	There is an Alert list link provided to see all the unattended patients. 
5.	Even though rescue specialist updates the patient record still he can view Alert list to see if there are patients unattended.
6.	The entire code can be found on github link provided.

# 3.	Data Tracking
1.	Based on the added patient records we are currently supporting graphs for tracking some vital signs so that it could be analyzed visually.
2.	Currently, we have implemented the graph generation for blood pressure monitoring.
3.	For each value of systolic and diastolic we are generating line chart. 
4.	From the chart, it could be easily figured the fluctuations for blood pressure.

# Code Implementation:
1.	To generate graphs in python we have used reportlabs http://www.reportlab.com/. 
2.	This is opensource and supports building various charts. We choose Line charts. 
3.	Once the rescue specialist submits the details of the Blood pressure for a patient. 
4.	He can click View Graphs to see the Line chart representation of Systolic and Diastolic.
5.	The entire code can be viewed in github link provided.






