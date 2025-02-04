# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 3: Access Visualization
Objective
Develop a visual representation of the company's access control system to identify patterns, overlaps, and security risks.
Scenario
The company’s security team is struggling to interpret raw access data. They need a clear way to see:
Employees who have access to financial records, technical documents, or both.
Employees with no access, who may need onboarding.
Any overlap that could indicate excessive privileges or security risks.
Instead of listing raw data, your task is to create a structured representation that makes these relationships intuitive and easy to understand.
Your Task
Using the provided employee access data, design a way to illustrate:
Who belongs where? Group employees based on their level of access.
Where is the overlap? Show employees who have access to both financial and technical records.
Who is left out? Identify employees without access.
Are there risks? Indicate employees who might be exposed to unnecessary data.
Your output should visually highlight these relationships without explicitly listing them in a simple table or list. Think beyond just printing data—use a format that helps detect patterns at a glance.
"""


# Define the sets of employees with access
finance_access = ["E0435", "E1021", "E3098", "E7642", "E8873", "E6590"]  # Financial access
tech_access = ["E7642", "E8873", "E6590", "E9812", "E4520"]  # Technical access

# Special cases
admin = ["E0001"]  # Admin has access to all data
new_employee = ["E9999"]  # New employee has no access yet

# Combine all employees in the system
all_employees = finance_access + tech_access + admin + new_employee

# Initialize empty lists for each category
exclusive_finance = []  # Only financial access
exclusive_tech = []  # Only technical access
both_access = []  # Both financial and technical access
no_access = []  # No access

# Categorize employees
for emp in all_employees:
  
    # Check for access on both fields
    if emp in finance_access and emp in tech_access:
        both_access.append(emp)
        
    # Check for exclusive access
    elif emp in finance_access:  # Only financial access
        exclusive_finance.append(emp)
        
    # Check for exclusive access
    elif emp in tech_access:  # Only technical access
        exclusive_tech.append(emp)
        
    # No access at all
    else:  # No access
        no_access.append(emp)

# Print a structured text-based table

print("\nSIMPLE TABLE")

print("-" * 50)
print(f"{'Category':<30} | {'Employee IDs'}")
print("-" * 50)
print(f"{'1. Financial Access Only':<30} | {exclusive_finance}")
print(f"{'2. Technical Access Only':<30} | {exclusive_tech}")
print(f"{'3. Both Financial & Technical Access':<30} | {both_access}")
print(f"{'4. No Access':<30} | {no_access}")
print("-" * 50)

# Highlight potential security risks
if both_access:
    print("\nSecurity Risk Alert:")
    print("The following employees have overlapping access (both financial and technical):")
    for emp in both_access:
        print(f"- {emp}")
else:
    print("\nNo overlapping access detected.")

# Recommendations
print("\nRecommendations:")
print("- Review overlapping access for employees:", both_access)
print("- Assign appropriate access to new employees (e.g., E9999).")
print("- Ensure admin access (E0001) is monitored closely.")
