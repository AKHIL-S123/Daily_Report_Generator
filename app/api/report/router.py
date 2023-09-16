from app.api.report.models import *
from app.api.report.schemas import *
from app.api.report.controller import *
from app.configuration.config import *
from app.utils.bearer import JWTBearer
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,Query
from .response_definition import *

report = APIRouter(tags=["Progress Report"])



@report.post('/progress',responses=create_report_response)
def create_progress(data: InfoBase, token: str = Depends(JWTBearer()), db: Session = Depends(get_db)
):
    """To create a progress report"""
    return create_report_controller(data,token,db)



@report.get('/get_report/{report_id}',responses=get_report_response)
def get_progress(report_id: int, db: Session = Depends(get_db),token: str = Depends(JWTBearer())
):
    """To get a progress report """
    db_info = get_report_controller(report_id,db,token)
    return db_info


@report.put('/update_report/{report_id}',responses=update_report_response)
def update_progress(report_id: int, info_update: InfoBase, token: str = Depends(JWTBearer()), db: Session = Depends(get_db)
):
    """To update a progress report"""
    updated_report = update_report_controller(db, report_id, info_update, token)
    return updated_report


@report.delete('/delete_report/{report_id}')
def delete_progress(report_id: int, db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    
    """To delete a progress report """
    db_info = delete_report_controller(report_id,db,token)
    return db_info

@report.get("/get_all_report",responses=get_all_report_response)
def get_all_report(
    db: Session=Depends(get_db),
    keywords: str = Query(None, title="Keywords to Search", description="Optional keywords for search"),
    token: str = Depends(JWTBearer())
):
    """To get total progress report of the user """
    all_report_info=get_all_report_controller(db,keywords,token)
    return all_report_info


@report.post("/monthly_report",responses=monthly_report_response)
def monthly_report(
    month: int = Query(description="Month (1-12)", ge=1, le=12),year: int = Query(description="Year (e.g., 2023)", ge=1900),
    db: Session = Depends(get_db),token: str = Depends(JWTBearer())
):
    """To get monthly report of the user """
    monthly_report_info =monthly_report_controller(month,year,db,token)
    return monthly_report_info


@report.get("/total-hours-by-date-range",responses=total_hours_response)
def total_hours_by_date_range(
    start_date: date=Query(description="Date (e.g.,2023-09-01)"),
    end_date: date=Query(description="Date (e.g.,2023-09-01)"), token: str = Depends(JWTBearer()), db: Session = Depends(get_db)
):
    """To get total hours by date range """
    total_hours = total_hours_by_date_range_controller(start_date, end_date, db, token)
    return {"total_hours": total_hours}


@report.get("/today-reports",responses=total_hours_response)
def get_today_reports(
    token: str = Depends(JWTBearer()),
    db: Session = Depends(get_db)
):
    """To get today report"""
    Today_report=get_today_reports_contoller(token,db)
    return  Today_report


@report.get("/Report-filter-ADMIN",summary="Only for admin")
def filter_reports_endpoint(
   user_id: int,
    token: str = Depends(JWTBearer()),
    month: str = Query(None, title="Month (JAN, FEB, MAR)", regex=r'^(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)$', description="Filter by month (optional)"),
    project_name: str = Query(None,  description="Filter by project name"),
    start_date: date = Query(None, description="Custom start date "),
    end_date: date = Query(None, description="Custom end date "),
    db: Session = Depends(get_db)
):
    """To filter the reports in db """
    
    filtered_reports = filter_reports_controller(db, user_id,token,month, project_name, start_date, end_date)
    return filtered_reports
