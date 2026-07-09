def verify_age(age_str: str) -> str:
    # 1. Convert the string to an integer
    age = int(age_str)
    
    # 2. Use the integer variable 'age' for the comparison
    return "Access Granted" if age >= 18 else "Access Denied"