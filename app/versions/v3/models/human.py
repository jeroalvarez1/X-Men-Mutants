from sqlalchemy import Column, Integer, Boolean, ARRAY, String
from app.database import Base
from app.database import SessionLocal

class Human(Base):
    __tablename__ = 'human'

    id = Column(Integer, primary_key=True)
    dna = Column(ARRAY(String))
    is_mutant = Column(Boolean)

    def save_human(self, dna, is_mutant):
        """
        Save the human
        :return:
        """
        session = SessionLocal()
        try:
            human = Human(dna=dna, is_mutant=is_mutant)
            session.add(human)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def get_stats(self):
        """
        Get the stats of the humans
        :return:
        """
        session = SessionLocal()
        mutants = session.query(Human).filter(Human.is_mutant == True).count()
        humans = session.query(Human).filter().count()
        session.close()
        return {"count_mutant_dna": mutants, "count_human_dna": humans, "ratio": mutants / humans}