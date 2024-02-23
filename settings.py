from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field, field_validator

def validate_threshold(value):
    if value < 0 or value > 1:
        return False
    
    return True


class MySettings(BaseModel):
    range: int = 30
    credentials: str
    token: str


@plugin
def settings_model():
    return MySettings
