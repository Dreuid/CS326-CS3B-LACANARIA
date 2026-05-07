import os
import logging
import time
from typing import List, Dict, Union

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 1. Protected Sensitive Values: Pulling from environment instead of hardcoding
SECRET_API_KEY = os.getenv("GWA_API_KEY", "dev-secret-token-123")

# 2. Basic Authentication
def authenticate(token: str) -> bool:
    if token != SECRET_API_KEY:
        logging.error("Security Alert: Unauthorized access attempt.")
        return False
    return True

def calculate_gwa(courses: List[Dict[str, Union[float, int]]], auth_token: str) -> float:
    # Require authentication before processing
    if not authenticate(auth_token):
        return -1.0 # Or raise an Exception

    start_time = time.time()
    
    total_units = 0.0
    total_weighted_points = 0.0
    
    for course in courses:
        # 3. Input Validation #1: Prevent negative or impossibly high units
        if course['units'] < 0 or course['units'] > 10:
            logging.error(f"Validation Failed: Invalid unit count ({course['units']}).")
            return 0.0
            
        # 4. Input Validation #2: Ensure grades fall within the standard 1.0 to 5.0 range
        if not (1.0 <= course['grade'] <= 5.0):
            logging.error(f"Validation Failed: Grade {course['grade']} is out of bounds.")
            return 0.0

        total_units += course['units']
        total_weighted_points += (course['grade'] * course['units'])
    
    if total_units == 0:
        logging.warning("Zero total units encountered. Returning 0.0.")
        return 0.0
        
    gwa = round(total_weighted_points / total_units, 2)
    return gwa
