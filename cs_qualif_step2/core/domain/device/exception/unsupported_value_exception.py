from cs_qualif_step2.core.domain.exception.Invalid_input_exception import InvalidInputException

class UnsupportedValueException(InvalidInputException):
    def __init__(self, field_name: str, value):
        self.field_name = field_name
        self.value = value
        super().__init__(f"Valeur non supportée pour '{field_name}': {value}")
