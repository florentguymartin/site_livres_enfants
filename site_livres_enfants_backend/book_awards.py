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
    def get_award_name(self) -> str:
        return "Médaille Caldecott"

class PrixBolognaRagazzi(GenericBookAward):
    def get_award_name(self) -> str:
        return "Prix Bologna Ragazzi"

class PommeDorBratislava(GenericBookAward):
    def get_award_name(self) -> str:
        return "Pomme d'Or de Bratislava"

class PrixSorciere(GenericBookAward):
    def get_award_name(self) -> str:
        return "Prix Sorcière"


award_descriptions: dict[type[GenericBookAward], tuple[str, str, str]] = {
    MedailleCaldecott: (
        "Médaille Caldecott",
        "La médaille Caldecott est décernée chaque année par l'American Library Association à l'illustrateur du livre d'images pour enfants américain le plus distingué de l'année.",
        "medaille_caldecott",
    ),
    PrixBolognaRagazzi: (
        "Prix Bologna Ragazzi",
        "Le prix Bologna Ragazzi est l'un des prix littéraires les plus prestigieux pour la littérature jeunesse, décerné chaque année lors du Salon du livre de jeunesse de Bologne.",
        "prix_bologna_ragazzi",
    ),
    PommeDorBratislava: (
        "Pomme d'Or de Bratislava",
        "La Pomme d'Or de Bratislava est un prix international décerné lors du Biennale des illustrations de Bratislava pour récompenser l'excellence en illustration de livres pour enfants.",
        "pomme_d_or_de_bratislava",
    ),
    PrixSorciere: (
        "Prix Sorcière",
        "Le Prix Sorcière est un prix littéraire français décerné chaque année par les libraires spécialisés en littérature jeunesse pour récompenser les meilleurs livres pour enfants.",
        "prix_sorciere",
    ),
}
