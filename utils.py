import random 
import datetime
from config import EVENT , DATETIME_FORMAT

def get_event(reporter_id):
    """Return a new event object according to configuration"""
    return {
        "reporterId": reporter_id,
        "timestamp": datetime.datetime.now().strftime(DATETIME_FORMAT),
        "metricId": random.randint(EVENT["METRIC_ID_MIN"], EVENT["METRIC_ID_MAX"]),
        "metricValue": random.randint(EVENT["METRIC_VALUE_MIN"], EVENT["METRIC_VALUE_MAX"]),
        "message": EVENT["MESSAGE"]
    }