import requests

# Function to solve a single problem
def solve_problem(problem):
    l=problem.split(" ")
    num1=int(l[0])
    num2=int(l[2])
    operator=l[1] 
    result =0
    # Solve the problem based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    # Print the problem and the answer
    print("num1 "+str(operator)+" num2 = ",result,"\n")

# URL to fetch the problems
url = 'https://www.michaelgathara.com/api/python-challenge'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    #problems = data.get('problem', [])
    for i in data:
        solve_problem(i["problem"][0:-1])
else:
    print(f"Error: Failed to fetch problems. Status code: {response.status_code}")
