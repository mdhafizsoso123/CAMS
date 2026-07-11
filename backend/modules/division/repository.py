from uuid import UUID

from sqlalchemy.orm import Session

from modules.division.models import Division


class DivisionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, division: Division):
        self.db.add(division)
        self.db.commit()
        self.db.refresh(division)
        return division

    def get_all(self):
        return (
            self.db.query(Division)
            .order_by(Division.name)
            .all()
        )

    def get_by_id(self, division_id: UUID):
        return (
            self.db.query(Division)
            .filter(Division.id == division_id)
            .first()
        )

    def get_by_name(self, name: str):
        return (
            self.db.query(Division)
            .filter(Division.name == name)
            .first()
        )

    def get_by_code(self, code: str):
        return (
            self.db.query(Division)
            .filter(Division.code == code)
            .first()
        )

    def update(self):
        self.db.commit()

    def delete(self, division: Division):
        self.db.delete(division)
        self.db.commit()