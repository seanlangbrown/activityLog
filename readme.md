service endpoints:

 POST activityLog(user_id, source, time, data<other parameters>)
 
 GET activityLogs(user_id, start_time, end_time, filters<filters on other parameters>) <- current renders a dummy event

Test run with:
 export FLASAPP=flaskr
 export FLASK_ENV=development
 flask run

View dummy event log at: http://127.0.0.1:5000/activityLogs
