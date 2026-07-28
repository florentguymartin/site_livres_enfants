# import ABC
from abc import ABC, abstractmethod

class BookAward(ABC):

    @abstractmethod
    def to_str(self) -> str:
        """String representation of the book award."""
        pass


class GenericBookAward(BookAward):

    def __init__(self, year: int, additional_comment: str | None = None):
        self._year = year
        self._additional_comment = additional_comment

    @abstractmethod
    def get_award_name(self) -> str:
        """Return the name of the book award."""
        pass

    def to_str(self) -> str:
        award_as_str = f"{self.get_award_name()} {self._year}"
        if self._additional_comment:
            award_as_str += f" ({self._additional_comment})"
        return award_as_str

class MedailleCaldecott(GenericBookAward):
    # def __init__(self, year: int, additional_comment: str | None = None):
    #     super().__init__(year, additional_comment)

    def get_award_name(self) -> str:
        return "Médaille Caldecott"