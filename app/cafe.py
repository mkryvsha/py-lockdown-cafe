import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("no key == vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("vaccine Outdated -> shoot the bustard")
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("No mask gool")
        else:
            return f"Welcome to {self.name}"
