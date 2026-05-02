from dataclasses import dataclass
from typing import Optional

@dataclass
class PersonSearchCriteria:

    name: Optional[str] = None
    email: Optional[str] = None
    age_from: Optional[int] = None
    age_to: Optional[int] = None


class PersonSearcher:

    def search(self, criteria: PersonSearchCriteria) -> list[Person]:
        """Search persons based on criteria."""
