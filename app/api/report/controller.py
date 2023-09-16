from app.api.report.schemas import *
from app.api.report.service import *
from app.api.report.models import *
from app.api.user.models import *
from app.utils.handler import *
from app.utils.bearer import *
from fastapi import HTTPException
from sqlalchemy.orm import Session


"""
@param - db -  Database Session object
@param - info- Request body
@param - token - Verified token
@returns - Report data object
"""

def create_report_controller(data,token,db):
    db_info = create_report_service(data,token,db)
    
    return {"message": "Report created successfully", "record": db_info}

"""
@param - report_id - Id of the report
@param - db -  Database Session object
@param - token - Verified token
@returns - Specific report data object
"""

def get_report_controller(report_id: int, db: Session, token: str):
    try:
        report_info = get_report_service(report_id,db,token)
        return report_info
    except HTTPException as exception:
         raise exception
    
"""
@param - db -  Database Session object
@param - report_id - Id of the report
@param - info_update - Request body
@param - token - Verified token
@returns - Report specific data object
"""

def update_report_controller(db: Session, report_id: int, info_update: InfoBase, token: str):
    try:
        update_info=update_report_service(db,report_id,info_update,token)
        return {"message": "Report updated successfully", "record": update_info}
    except HTTPException as exception:
        raise exception

"""
@param - report_id - id of the report
@param - db -  database Session object
@param - token - verified token
@returns - successfully deleted
"""
def delete_report_controller(report_id: int, db: Session,token: str,):
    try:
        delete_info=delete_report_service(report_id,db,token)
        return delete_info
    except HTTPException as exception:
        raise exception



"""
@param - db -  database Session object
@param - keywords -search the specific report by keywords
@param - token - verified token
@returns - Total report object
"""

def get_all_report_controller(db:Session,keywords:str,token:str):
    try:
        all_report_info=get_all_report_service(db,keywords,token)
        return{ "All record": all_report_info}
    except HTTPException as exception:
        raise exception

"""
@param - month -  equired for month
@param - year -Search the specific report by keywords
@param - db -  Database Session object
@param - token - Verified token
@returns - Monthly report data object
"""

def monthly_report_controller(month: int, year: int,db: Session,token:str):
    try:
        monthly_report_info=monthly_report_service(month,year,db,token)
        return {"Monthly Report":monthly_report_info}
    except HTTPException as exception:
        raise exception
    
"""
@param - start_date -  required starting date
@param - end_date - required  ending date
@param - db -  database Session object
@param - token - verified token
@returns -total hours 
"""

def total_hours_by_date_range_controller(start_date, end_date, db, token):
    try:
        total_hours = total_hours_by_date_range_service(start_date, end_date, db, token)
        return {"Total hours": total_hours}
    except HTTPException as exception:
        raise exception
    


"""
@param - db -  database Session object
@param - token - verified token
@returns -today report 
"""

def get_today_reports_contoller(token,db):
    try:
        today_report=get_today_reports_service(token,db)
        return {"Today Report":today_report}
    except HTTPException as exception:
        raise exception

"""

@param - db -  database Session object
@param - token - verified token
@param - month - required month to fetch the report
@param- project_name - Project name to retrieve
@param - start_date -  required starting date to fetch the report
@param - end_date - required  ending date to fetch the report
@returns -filterd report data object
"""

def filter_reports_controller(db, user_id,token,month, project_name, start_date, end_date):
    try:
        filtered_report=filter_reports_service(db, user_id,token,month, project_name, start_date, end_date)
        return filtered_report
    except HTTPException as exception:
        raise exception
