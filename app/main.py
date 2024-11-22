from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for visitor in friends:
        try:
            try:
                cafe.visit_cafe(visitor)
            except NotWearingMaskError:
                masks_to_buy += 1
        except VaccineError:
            return "All friends should be vaccinated"
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
