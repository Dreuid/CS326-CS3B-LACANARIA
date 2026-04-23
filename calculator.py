# ==========================================
# 1. REFACTORED CALCULATOR LOGIC
# ==========================================
def calculate_gwa(courses: List[Dict[str, Union[float, int]]]) -> float:
    """
    Calculates the GWA in a single optimized O(N) pass.
    """
    total_units = 0.0
    total_weighted_points = 0.0
    
    # Optimized: Calculate both totals in a single loop instead of two
    for course in courses:
        total_units += course['units']
        total_weighted_points += (course['grade'] * course['units'])
    
    # Prevent ZeroDivisionError if user inputs 0 units
    if total_units == 0:
        return 0.0
        
    return round(total_weighted_points / total_units, 2)
