
from enum import Enum,unique

@unique
class RandomDataTypeEnum(Enum):

    BOOLEAN = '$BOOLEAN$'
    INTEGER = '$INTEGER$'
    FLOAT = '$FLOAT$'
    STRING = '$STRING$'
    RANDOM_ID = '$UUID$'
    EMAIL = '$EMAIL$'
    DATE = '$DATE$'
    DATETIME = '$DATETIME$'
    PHONE = '$PHONE$'
    GENDER = '$GENDER$'
    ID_CARD = '$ID_CARD$'
