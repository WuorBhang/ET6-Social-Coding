# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 2: Digital Access Control
Objective
Use set operations to analyze and improve a company's digital access control system while identifying potential security risks in data access.
Scenario
A secure company vault stores sensitive data, where employees are granted access based on their roles:
Finance Team (F): Needs access to financial records.
Tech Team (T): Needs access to technical documents.
Some employees belong to both teams due to cross-departmental responsibilities.
Access Data (Given)
The security system tracks employee IDs (formatted as "E####").
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
Additionally, two special cases exist:
E0001 (Admin): Has access to all data but is not listed in specific access groups.
E9999 (New Employee): Has no assigned access yet.
Your Task
Analyze the current access structure and identify potential security risks by answering the following:
Who has access to at least one type of data?
Who has access to both financial and technical data?
Who has exclusive access to only one type of data?
Which employees currently lack access (but exist in the system)?
Are there unnecessary overlaps in access that could pose a security risk?
What changes would you recommend to enhance security and minimize excessive access?
# -*- coding: utf-8 -*-

"""

# Define the sets of employees with access
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}  # Employees with financial access
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}  # Employees with technical access

# Special cases
admin = {"E0001"}  # Admin has access to all data
new_employee = {"E9999"}  # New employee has no access yet

# Combine all employees in the system
all_employees = finance_access.union(tech_access).union(admin).union(new_employee)

# Question 1: Who has access to at least one type of data?
# Combine finance_access, tech_access, and admin

# Create an empty set
access_at_least_one = set()

# Add employees from finance_access
for emp in finance_access:
    access_at_least_one.add(emp) 
    
# Add employees from tech_access
for emp in tech_access:
    access_at_least_one.add(emp)
    
# Add admin
for emp in admin:
    access_at_least_one.add(emp)
    
# Print the result
print("Employees with access to at least one type of data:", access_at_least_one)

# Question 2: Who has access to both financial and technical data?

# Create an empty set
access_both = set()

# Check for employees with access to both financial and technical data  
for emp in finance_access:
    if emp in tech_access:
        access_both.add(emp)
        
# Print the result
print("Employees with access to both financial and technical data:", access_both)

# Question 3: Who has exclusive access to only one type of data?

# Create empty set
exclusive_finance = set()

# Employees with only finance access
for emp in finance_access:
    if emp not in tech_access:  # Check if the employee is NOT in tech_access
        exclusive_finance.add(emp)

# Create empty set
exclusive_tech = set()  

# Employees with only tech access
for emp in tech_access:
    if emp not in finance_access:  # Check if the employee is NOT in finance_access
        exclusive_tech.add(emp)

exclusive_access = exclusive_finance.union(exclusive_tech)
print("Employees with exclusive access to only one type of data:", exclusive_access)

# Question 4: Which employees currently lack access (but exist in the system)?

# Create an empty set
lack_access = set()  

# Employees who lack access
for emp in all_employees:
    if emp not in access_at_least_one:  # Check if the employee is NOT in the access list
        lack_access.add(emp)
        
# print the result
print("Employees who lack access:", lack_access)

# Question 5: Are there unnecessary overlaps in access that could pose a security risk?

# Create an empty set
overlap_risk = set()  

# Employees with overlapping access
for emp in finance_access:
    if emp in tech_access:  # Check if the employee is in both groups
        overlap_risk.add(emp)
        
# Print the result
print("Employees with overlapping access (potential security risk):", overlap_risk)

# Question 6: Recommendations to enhance security and minimize excessive access
print("\nRecommendations:")
print("- Ensure admin access (E0001) is monitored closely.")
print("- Review and remove unnecessary overlaps in access.")
print("- Regularly update access permissions based on employee roles.")
print("- Implement a system to track and manage access changes.")
print("- Provide training on data security and access control policies.")
print("- Conduct periodic security audits to identify vulnerabilities.")
print("- Consider role-based access control (RBAC) for better access management.")
print("- Implement multi-factor authentication for sensitive data access.")
print("- Encrypt sensitive data to protect against unauthorized access.")
print("- Establish clear guidelines for granting and revoking access.")
print("- Create a response plan for security incidents and data breaches.")
print("- Foster a culture of cybersecurity awareness among employees.")
print("- Collaborate with IT and security teams to enhance data protection.")
print("- Stay informed about the latest security threats and best practices.")
print("- Continuously improve security measures to adapt to evolving risks.")
print("- Prioritize data privacy and compliance with industry regulations.")
print("- Invest in cybersecurity tools and resources for enhanced protection.")
print("- Encourage reporting of security concerns and incidents.")
print("- Develop a robust incident response and recovery strategy.")

# End of challenge 2
