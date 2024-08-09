# 7. Scenario:
# Imagine you're managing a company's employee database where each department 
# has its own set of employees. Each employee has attributes such as 
# name, position, and salary. The database structure uses nested dictionaries.

# Question: 
# How can you find the salary of the employee with ID emp002 in the 
# Sales department?

emp_db = {

    "Sales" :{
        "emp101": {"name" : "name_101", "position" : "position_101", "salary" : 1000},
        "emp102": {"name" : "name_102", "position" : "position_102", "salary" : 2000},
        "emp103": {"name" : "name_103", "position" : "position_103", "salary" : 1500},
        "emp104": {"name" : "name_104", "position" : "position_104", "salary" : 500},
    },

    "IT" :{
        "emp201": {"name" : "name_201", "position" : "position_201", "salary" : 1000},
        "emp202": {"name" : "name_202", "position" : "position_202", "salary" : 2000},
        "emp203": {"name" : "name_203", "position" : "position_203", "salary" : 1500},
        "emp204": {"name" : "name_204", "position" : "position_204", "salary" : 500},
    },

    "Eng" :{
        "emp301": {"name" : "name_301", "position" : "position_301", "salary" : 1000},
        "emp302": {"name" : "name_302", "position" : "position_302", "salary" : 2000},
        "emp303": {"name" : "name_303","position" : "position_303", "salary" : 1500},
        "emp304": {"name" : "name_304", "position" : "position_304", "salary" : 500},
    },
}

count = 0
max_salary = 0
my_tuple = ()

for i in emp_db:
    if(i == "Sales"):
        for j in emp_db[i]:
            if(emp_db[i][j]["salary"] > max_salary):
                max_salary = emp_db[i][j]["salary"]
                my_tuple = tuple(emp_db[i][j].items())
    break

print("\n", my_tuple, "\n")


