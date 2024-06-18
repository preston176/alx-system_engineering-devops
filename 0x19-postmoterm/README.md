## Postmortem Report: Power Outage Reporting and Status Web App
### Issue Summary
### Outage Duration:

- Start Time: May 25, 2024, 02:00 AM (UTC)
- End Time: May 25, 2024, 05:30 AM (UTC)
- Total Duration: 3 hours and 30 minutes
### Impact:

- Service Impacted: Power Outage Reporting and Status Web App
- User Experience: Users were unable to report outages or view the outage map. Approximately 70% of users experienced service disruption.
- Root Cause: A bug in the database query logic caused a failure in retrieving outage reports, leading to server crashes.
### Timeline
- 02:00 AM: Issue detected via monitoring alert indicating high error rates and server downtime.
- 02:05 AM: Initial investigation started by the on-call engineer.
- 02:15 AM: Assumption that the issue was related to server resource limits.
- 02:30 AM: Increased server resources, but the issue persisted.
- 02:45 AM: Noticed errors related to database queries; suspected a database issue.
- 03:00 AM: Misleading path investigated: potential DDoS attack.
- 03:30 AM: Escalated to the database administration team.
- 04:00 AM: Identified the root cause as a bug in the SQL query for retrieving outage reports.
- 04:30 AM: Deployed a temporary fix by disabling the faulty query.
- 05:00 AM: Permanent fix implemented by correcting the SQL query logic.
- 05:30 AM: Services fully restored and operational.
### Root Cause and Resolution
#### Root Cause:

- The issue was caused by a bug in the SQL query used to retrieve outage reports from the database. Specifically, the query contained a join condition that resulted in a full table scan, which overwhelmed the database and caused server crashes.
### Resolution:

- The immediate response was to disable the faulty query to stabilize the server. A thorough review of the query was conducted, and the logic was corrected to use appropriate indexing and optimized join conditions. The updated query was tested and then deployed to production.
Corrective and Preventative Measures
### Improvements:

- Implement comprehensive query performance testing to catch inefficient queries before deployment.
Enhance monitoring to include specific alerts for database query performance issues.
Conduct regular code reviews focusing on database interactions.
Tasks:

- **Patch SQL Queries**: Review and optimize all existing database queries to prevent similar issues.
Add Monitoring: Implement detailed monitoring on database performance and query execution times.
Update Documentation: Document the incident and update the standard operating procedures to include steps for diagnosing database issues.
- **Training**: Conduct training sessions for developers on writing efficient SQL queries and identifying potential performance bottlenecks.
- Backup Strategy: Ensure a robust database backup strategy is in place to facilitate quick recovery from similar incidents.
### Conclusion
This incident highlighted the importance of efficient database query practices and the need for robust monitoring systems. By learning from this outage, we have taken significant steps to improve our processes and prevent similar issues in the future. Failing is part of the process, but with each failure, we grow stronger and more resilient.