import re

def nlq_to_sql(nl_query: str) -> str:
    nl_query = nl_query.lower()
    conditions = []

    # Extract numbers if any
    numbers = re.findall(r'\d+', nl_query)

    # Handle marks
    if "marks" in nl_query and numbers:
        if "above" in nl_query:
            conditions.append(f"marks > {numbers[0]}")
        elif "below" in nl_query:
            conditions.append(f"marks < {numbers[0]}")
        elif "equal" in nl_query or "equals" in nl_query:
            conditions.append(f"marks = {numbers[0]}")

    # Handle age
    if "age" in nl_query and numbers:
        if "above" in nl_query or "older than" in nl_query:
            conditions.append(f"age > {numbers[0]}")
        elif "below" in nl_query or "younger than" in nl_query:
            conditions.append(f"age < {numbers[0]}")
        elif "equal" in nl_query or "equals" in nl_query:
            conditions.append(f"age = {numbers[0]}")

    # Handle grade
    grade_match = re.search(r"grade\s*([a-z])", nl_query)
    if grade_match:
        grade_value = grade_match.group(1).upper()
        conditions.append(f"grade = '{grade_value}'")

    # Base SQL
    sql = "SELECT * FROM students"

    if conditions:
        if " and " in nl_query:
            sql += " WHERE " + " AND ".join(conditions)
        elif " or " in nl_query:
            sql += " WHERE " + " OR ".join(conditions)
        else:
            sql += " WHERE " + " AND ".join(conditions)
    else:
        sql += ";"

    return sql


if __name__ == "__main__":
    print("Natural Language to SQL Converter (V2: Multi-Condition Queries)")
    print("Examples:")
    print("- Show all students with marks above 80")
    print("- List students older than 20 and with grade A\n")

    user_query = input("Enter your query: ")
    sql_query = nlq_to_sql(user_query)

    print("\nGenerated SQL Query:")
    print(sql_query)
