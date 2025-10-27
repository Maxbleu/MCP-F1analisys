from typing import Dict, List
from pydantic import BaseModel

class DriversLapsRange(BaseModel):
    drivers_laps: Dict[str, List[int]]