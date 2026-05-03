# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Professor": 100,
    "Starbucks barista": 12 }

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {
    "company_name": "Beta Theta Pi",
    "contact_person": "Jackson Smith",
    "email": "Smith@Beta.com",
    "phone": "555-1234" }
customer2 = {
"company_name": "Alpha Consulting",
"contact_person": "David Hilemen",
"email": "David@alpha.com",
"phone": "555-2345"}

customer3 = {
"company_name": "Gamma Financial",
"contact_person": "Hudson Khan",
"email": "Khan@gamma.com",
"phone": "555-3456"}

customer4 = {
"company_name": "Delta Innovations",
"contact_person": "Maria Garcia",
"email": "maria@delta.com",
"phone": "555-4567"} 
# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {
"C001": customer1,
"C002": customer2,
"C003": customer3,
"C004": customer4 } 
# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
for cid, info in customers.items():
    print("Customer ID:", cid)
    print("Company:", info["company_name"])
    print("Contact:", info["contact_person"])
    print("Email:", info["email"])
    print("Phone:", info["phone"])
    print()
# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
c002_info = customers["C002"]
print("C002 Info:", c002_info)

c003_contact = customers["C003"]["contact_person"]
print("C003 Contact:", c003_contact)

c999_info = customers.get("C999", "Customer not found")
print("C999 Info:", c999_info)
# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
customers["C001"]["phone"] = "555-9999"
customers["C002"]["industry"] = "Consulting"

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])
# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}
project1 = {"name": "Website Revamp", "service": "Web Development", "hours": 120, "budget": 18000}
project2 = {"name": "Security Audit", "service": "Cybersecurity", "hours": 60, "budget": 13200}
project3 = {"name": "Sales Dashboard", "service": "Data Analysis", "hours": 80, "budget": 14000}
project4 = {"name": "Tech Support", "service": "Starbucks barista", "hours": 50, "budget": 600}
project5 = {"name": "Research Consulting", "service": "Professor", "hours": 40, "budget": 4000}

projects = {
"C001": [project1, project2],
"C002": [project3],
"C003": [project4],
"C004": [project5]
}
print("\n\nProject Information:")
print("-" * 60)
# Add your code here
for cid, plist in projects.items():
    print(cid, plist)
# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for cid, plist in projects.items():
  for p in plist:
    rate = services[p["service"]]
    cost = rate * p["hours"]
    print(p["name"], "Cost:", cost)
# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print("Customer IDs:", customers.keys())

companies = [c["company_name"] for c in customers.values()]
print("Customer Companies:", companies)

print("Total Customers:", len(customers))
# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
service_counts = {}

for project_list in projects.values():
    for project in project_list:

        service = project["service"]

        if service in service_counts:
            service_counts[service] += 1
        else:
            service_counts[service] = 1

print(service_counts)
# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
all_projects = []

for project_list in projects.values():
    for project in project_list:
        all_projects.append(project)

total_hours = sum(p["hours"] for p in all_projects)

total_budget = sum(p["budget"] for p in all_projects)

avg_budget = total_budget / len(all_projects)

max_budget = max(all_projects, key=lambda x: x["budget"])

min_budget = min(all_projects, key=lambda x: x["budget"])

print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Most Expensive Project:", max_budget)
print("Least Expensive Project:", min_budget)
# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for cid, info in customers.items():

    project_list = projects.get(cid, [])

    total_hours = sum(p["hours"] for p in project_list)
    total_budget = sum(p["budget"] for p in project_list)

    print("Customer ID:", cid)
    print("Company:", info["company_name"])
    print("Contact:", info["contact_person"])
    print("Projects:", len(project_list))
    print("Total Hours:", total_hours)
    print("Total Budget:", total_budget)
    print()
# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print(adjusted_rates)
# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
active_customers = {cid: customers[cid] for cid in customers if cid in projects}

print(active_customers)
# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}

print(customer_budgets)
# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}

print(service_tiers)
# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
def validate_customer(customer_dict):

    required = ["company_name", "contact_person", "email", "phone"]

    for field in required:
        if field not in customer_dict:
            return False

    return True


for cid, info in customers.items():
    print(cid, validate_customer(info))
# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
status_counts = {"active": 0, "completed": 0, "pending": 0}

for plist in projects.values():
    for p in plist:
        p["status"] = "active"

for plist in projects.values():
    for p in plist:
        status_counts[p["status"]] += 1

print(status_counts)
# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
def analyze_customer_budgets(projects_dict):

    results = {}

    for cid, plist in projects_dict.items():

        total = sum(p["budget"] for p in plist)
        count = len(plist)
        avg = total / count if count > 0 else 0

        results[cid] = {
            "total": total,
            "average": avg,
            "count": count
        }

    return results


budget_analysis = analyze_customer_budgets(projects)

print(budget_analysis)
# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
def recommend_services(customer_id, customers, projects, services):

    used = set()

    for p in projects.get(customer_id, []):
        used.add(p["service"])

    recommendations = []

    for service in services:
        if service not in used:
            recommendations.append(service)

    return recommendations


for cid in customers:

    recs = recommend_services(cid, customers, projects, services)

    print(cid, recs)