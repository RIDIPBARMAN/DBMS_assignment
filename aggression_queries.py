import re

def nlq_to_sql(nl_query: str) -> str:
    nl_query = nl_query.lower().strip()

    # Default SQL (if no match found)
    sql = "SELECT * FROM students;"

    # Define mapping for aggregation keywords → SQL function
    agg_map = {
        "avg": ["average", "avg"],
        "max": ["maximum", "max", "highest"],
        "min": ["minimum", "min", "lowest"],
        "sum": ["sum", "total"],
        "count": ["count", "number of"]
    }

    # Detect which aggregation is requested
    agg_func = None
    for func, keywords in agg_map.items():
        if any(word in nl_query for word in keywords):
            agg_func = func
            break

    if not agg_func:
        return sql  # No aggregation found → default query

    # Handle COUNT separately
    if agg_func == "count":
        if "grade" in nl_query:
            match = re.search(r"grade\s+([a-z])", nl_query)
            if match:
                grade = match.group(1).upper()
                sql = f"SELECT COUNT(*) FROM students WHERE grade = '{grade}';"
            else:
                sql = "SELECT COUNT(*) FROM students;"
        else:
            sql = "SELECT COUNT(*) FROM students;"
        return sql

    # Handle numeric attributes (marks / age)
    if "marks" in nl_query:
        sql = f"SELECT {agg_func.upper()}(marks) FROM students;"
    elif "age" in nl_query:
        sql = f"SELECT {agg_func.upper()}(age) FROM students;"

    return sql


# Main program
if __name__ == "__main__":
    print("Natural Language to SQL Converter (Aggregation Queries)")
    print("Examples:")
    print("- Find average marks of students")
    print("- Show maximum age of students")
    print("- Count the number of students\n")

    user_query = input("Enter your query: ")
    sql_query = nlq_to_sql(user_query)

    print("\nGenerated SQL Query:")
    print(sql_query)
