from dao.schedule_dao import ScheduleDAO
from services.schedule import ScheduleService
from setup_dp import db

schedule_dao = ScheduleDAO(db.session)
schedule_service = ScheduleService(schedule_dao)