import re

def nlq_to_sql(nl_query: str) -> str:
    nl_query = nl_query.lower().strip()

    # Default SQL
    sql = "SELECT * FROM students"

    # Extract first number from query (if any)
    match = re.search(r'\d+', nl_query)
    number = int(match.group()) if match else None

    # Build conditions
    if number is not None:
        if "above" in nl_query:
            sql += f" WHERE marks > {number};"
        elif "below" in nl_query:
            sql += f" WHERE marks < {number};"
        elif "equal" in nl_query or "equals" in nl_query:
            sql += f" WHERE marks = {number};"
        else:
            sql += ";"
    else:
        sql += ";"

    return sql


# Main program
if __name__ == "__main__":
    print("Natural Language to SQL Converter (Basic Rule-Based)")
    print("Example: 'Show all students with marks above 80'\n")

    user_query = input("Enter your query: ")
    sql_query = nlq_to_sql(user_query)

    print("\nGenerated SQL Query:")
    print(sql_query)
