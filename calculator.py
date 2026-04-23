def calculate_gwa(courses):
    total_units = sum(course['units'] for course in courses)
    
    # Bug fix: Prevent ZeroDivisionError if user inputs 0 units
    if total_units == 0:
        return 0.0
        
    total_weighted_points = sum(course['grade'] * course['units'] for course in courses)
    return round(total_weighted_points / total_units, 2)
