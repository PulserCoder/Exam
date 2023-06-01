from flask import request
from flask_restx import Resource, Namespace

from implemented import schedule_service

schedules_ns = Namespace('schedules')


@schedules_ns.route('/')
class SchedulesView(Resource):
    """
    Represents the view for schedules collection.
    """

    def get(self) -> tuple:
        """
        Retrieves all schedules.

        Returns:
            tuple: A tuple containing the result and status code.
        """
        result = schedule_service.get_all()
        return result, 200

    def post(self) -> tuple:
        """
        Creates a new schedule.

        Returns:
            tuple: A tuple containing the result and status code.
        """
        return schedule_service.create(request.json)

    def put(self):
        """
        Updates a schedule.

        Returns:
            tuple: A tuple containing the result and status code.
        """
        schedule_service.update(request.json), 200

    def patch(self) -> tuple:
        """
        Updates a schedule partially.

        Returns:
            tuple: A tuple containing the result and status code.
        """
        return schedule_service.update(request.json), 200


@schedules_ns.route('/<int:pk>')
class ScheduleView(Resource):
    """
    Represents the view for a single schedule.
    """

    def get(self, pk: int) -> tuple:
        """
        Retrieves a single schedule by its primary key.

        Args:
            pk (int): The primary key of the schedule.

        Returns:
            tuple: A tuple containing the result and status code.
        """
        result = schedule_service.get_one(pk)
        if result.get('message', 0) != "there is no such schedule":
            return result, 200
        return result, 404

    def delete(self, pk: int) -> tuple:
        """
        Deletes a single schedule by its primary key.

        Args:
            pk (int): The primary key of the schedule.

        Returns:
            tuple: A tuple containing the result and status code.
        """
        result = schedule_service.delete(pk)
        if result.get('message') == 'successfully':
            return result, 200
        return result, 404
