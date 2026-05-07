"""GWA (General Weighted Average) calculator."""

import logging
import time
from typing import List, Dict, Union, TypedDict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Course(TypedDict):
    name: str
    units: float
    grade: float


def calculate_gwa(courses: List[Dict[str, Union[float, int]]]) -> float:
    start_time = time.time()
    logging.info(f"Starting GWA calculation for {len(courses)} courses.")

    for course in courses:
        if course['units'] < 0:
            raise ValueError("Units cannot be negative.")
        if course['grade'] < 0:
            raise ValueError("Grade cannot be negative.")

    total_units = 0.0
    total_weighted_points = 0.0

    for course in courses:
        total_units += course['units']
        total_weighted_points += (course['grade'] * course['units'])

    if total_units == 0:
        logging.warning("Zero total units encountered. Returning 0.0 to prevent division by zero.")
        return 0.0

    gwa = round(total_weighted_points / total_units, 2)

    calc_time = (time.time() - start_time) * 1000
    logging.info(f"Calculation successful: GWA={gwa}. Time taken: {calc_time:.4f} ms")

    return gwa
