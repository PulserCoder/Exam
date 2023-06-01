from dao.schedule_dao import ScheduleDAO


class ScheduleService:
    def __init__(self, ScheduleDAO: ScheduleDAO) -> None:
        """
        Initializes the ScheduleService.

        Args:
            ScheduleDAO (ScheduleDAO): An instance of ScheduleDAO for data access.
        """
        self.ScheduleDAO = ScheduleDAO

    def get_one(self, pk: int) -> dict:
        """
        Retrieves a single schedule by its primary key.

        Args:
            pk (int): The primary key of the schedule.

        Returns:
            dict: The retrieved schedule or a message indicating that the schedule doesn't exist.
        """
        schedule = self.ScheduleDAO.get_one(pk)
        if len(schedule) == 0:
            return {'message': "there is no such schedule"}
        return schedule

    def get_all(self) -> list:
        """
        Retrieves all schedules.

        Returns:
            list: A list of all schedules.
        """
        return self.ScheduleDAO.get_all()

    def create(self, schedule_d: dict) -> dict:
        """
        Creates a new schedule.

        Args:
            schedule_d (dict): The schedule data.

        Returns:
            dict: The created schedule or an error message.
        """
        try:
            return self.ScheduleDAO.create(schedule_d)
        except Exception as e:
            return {'message': "Your data isn't valid JSON", "message_terminal": e}

    def delete(self, pk: int) -> dict:
        """
        Deletes a single schedule by its primary key.

        Args:
            pk (int): The primary key of the schedule.

        Returns:
            dict: A message indicating the deletion status or an error message.
        """
        try:
            self.ScheduleDAO.delete(pk)
            return {'message': "successfully"}
        except Exception as e:
            return {'message': "there is no such schedule", "message_terminal": e}

    def update(self, schedule_d: dict) -> dict:
        """
        Updates a schedule.

        Args:
            schedule_d (dict): The updated schedule data.

        Returns:
            dict: The updated schedule or an error message.
        """
        return self.ScheduleDAO.update_schedule(schedule_d)
