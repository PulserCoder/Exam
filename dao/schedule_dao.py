from typing import Optional, List, Dict, Union
import datetime
from sqlalchemy.orm.scoping import Session

from dao.models.schedule import Schedule, ScheduleSchema
from setup_dp import db

schedule_schema = ScheduleSchema()
schedules_schema = ScheduleSchema(many=True)


class ScheduleDAO:
    """Data Access Object for Schedule model."""

    def __init__(self, session: Session):
        """
        Initialize a new instance of ScheduleDAO.

        Args:
            session (Session): The database session to use.
        """
        self.session = session

    def get_one(self, pk: int) -> Dict[str, Union[int, str]]:
        """
        Get a single Schedule record by primary key.

        Args:
            pk (int): The primary key of the Schedule record.

        Returns:
            dict: A dictionary containing Schedule record data.
        """
        return schedule_schema.dump(self.session.query(Schedule).get(pk))

    def get_all(self) -> List[Dict[str, Union[int, str]]]:
        """
        Get all Schedule records.

        Returns:
            list: A list of dictionaries, each containing Schedule record data.
        """
        return schedules_schema.dump(self.session.query(Schedule).all())

    def delete(self, pk: int) -> None:
        """
        Delete a single Schedule record by primary key.

        Args:
            pk (int): The primary key of the Schedule record.
        """
        schedule = self.get_one(pk)
        if schedule is None:
            raise Exception
        self.session.delete(schedule)
        self.session.commit()

    def create(self, schedule_d: Dict[str, Union[int, str]]) -> Dict[str, Union[int, str]]:
        """
        Create a new Schedule record.

        Args:
            schedule_d (dict): A dictionary containing Schedule data.

        Returns:
            dict: A dictionary containing the created Schedule record data.
        """
        new_schedule = Schedule(**schedule_d)
        self.session.add(new_schedule)
        self.session.commit()
        return schedule_schema.dump(new_schedule)

    def update_schedule(self, schedule_d: Dict[str, Union[int, str]]) -> Optional[Dict[str, Union[int, str]]]:
        """
        Update an existing Schedule record.

        Args:
            schedule_d (dict): A dictionary containing updated Schedule data.

        Returns:
            dict: A dictionary containing the updated Schedule record data,
                  or None if the record could not be found.
        """
        schedule = Schedule.query.get(schedule_d.get('id'))
        if schedule is None:
            return None
        name = schedule_d.get('name')
        if schedule_d.get('name', None) is not None:
            schedule.name = name
        if schedule_d.get('date', None) is not None:
            schedule.date = schedule_d.get('date')

        if schedule_d.get('name_of_teacher', None) is not None:
            schedule.name_of_teacher = schedule_d.get('name_of_teacher')
        if schedule_d.get('class_number', None) is not None:
            schedule.class_number = schedule_d.get('class_number')
        db.session.commit()
