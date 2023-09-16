from app.api.report.schemas import *
from app.api.report.models import *
from app.api.user.models import *
from app.api.report.controller import *
from app.utils.handler import *
from app.utils.bearer import *
from sqlalchemy.orm import Session
from datetime import  datetime, timedelta,date
from fastapi import HTTPException
from sqlalchemy import extract,or_
import pytz
ist = pytz.timezone('Asia/Kolkata')

"""
@param - db -  database Session object
@param - info- request body
@param - token - verified token
@returns - Report data object
"""
def create_report_service(data: InfoBase,token,db):
    start = datetime.fromisoformat(f'{data.date}T{data.start_time}')
    end = datetime.fromisoformat(f'{data.date}T{data.end_time}')
    duration = end - start
    user = decode_token(token)
    user_data = db.query(User).filter(User.email == user["user_mail"]).first()
    
    if not user_data:
        raise HTTPException(status_code=401,detail="Invalid user")

    if user_data.role == "admin":
        raise HTTPException(status_code=403, detail="Admin cannot create a report")

    db_info = UserReport(
        created_date=datetime.now(ist),
        date=data.date,
        project=data.project,
        task_id=data.task_id,
        task=data.task,
        status=data.status,
        start_time=data.start_time,
        end_time=data.end_time,
        duration=duration,
        description=data.description,
        user_id=user_data.id,  
    )

    db.add(db_info)
    db.commit()
    db.refresh(db_info)
    return db_info

"""
@param - report_id - Id of the report
@param - db -  Database Session object
@param - token - Verified token
@returns - Specific report data object
"""

def get_report_service(report_id,db,token):
    user=decode_token(token)
    user_email=user.get("user_mail")
    user_role=user.get("user_role")
    user_data = db.query(User).filter(User.email == user_email).first()
    db_info = db.query(UserReport).filter(UserReport.id == report_id).first()
    if db_info is None:
        raise HTTPException(status_code=404, detail="Info not found")
    if user_role == "admin" or (user_role != "admin" and db_info.user_id == user_data.id):
        return db_info
    else:
        raise HTTPException(status_code=403, detail="You are not authorized to access this report")
    

"""
@param - db -  Database Session object
@param - report_id - Id of the report
@param - info_update - Request body
@param - token - Verified token
@returns - Report specific data object
"""

def update_report_service(db,report_id,info_update,token):
    ist = pytz.timezone('Asia/Kolkata')
    user = decode_token(token)
    user_email = user.get("user_mail")
    user_role =user.get('user_role')
    user_data = db.query(User).filter(User.email == user_email).first()
    db_info = db.query(UserReport).filter(UserReport.id == report_id).first()

    if db_info is None:
        raise HTTPException(status_code=404, detail="Info not found")
    
    if user_role == "admin" or user_role != "admin" and db_info.user_id == user_data.id:
        if "start_time" in info_update.__dict__ and "end_time" in info_update.__dict__:
            start_time_str = info_update.start_time
            end_time_str = info_update.end_time

            start_time = datetime.strptime(start_time_str, '%H:%M:%S')
            end_time = datetime.strptime(end_time_str, '%H:%M:%S')
            duration = end_time - start_time
            db_info.duration = duration

        # Update fields except duration, start_time, and end_time
        for field, value in info_update.__dict__.items():
            if field not in ("duration", "start_time", "end_time"):
                setattr(db_info, field, value)

        db_info.updated_date = datetime.now(ist)  
        db.commit()
        db.refresh(db_info)
        return db_info
    else:
        raise HTTPException(status_code=403, detail="You are not authorized to update this report")
    
"""
@param - report_id - id of the report
@param - db -  database Session object
@param - token - verified token
@returns - successfully deleted
"""
def delete_report_service(report_id: int, db: Session,token: str,):
    """To delete a progress report"""
    user_info = decode_token(token)
    user_email = user_info.get("user_mail")
    user_role = user_info.get("user_role")
    user = db.query(User).filter(User.email == user_email).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    report = db.query(UserReport).filter(UserReport.id == report_id).first()

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    if user_role == "user" and report.user_id != user.id:
        raise HTTPException(status_code=403, detail="You are not authorized to delete this report")

    if user_role == "admin":
        db.delete(report)
        db.commit()
        return {"message": "Report deleted successfully"}

    if user_role == "user" and report.user_id == user.id:
        db.delete(report)
        db.commit()
        return {"message": "Report deleted successfully"}

    raise HTTPException(status_code=403, detail="You are not authorized to delete this report")



"""
@param - db -  database Session object
@param - keywords -search the specific report by keywords
@param - token - verified token
@returns - Total report object
"""

def get_all_report_service(db,keywords,token):
    user_info = decode_token(token)
    email = user_info.get("user_mail")
    role = user_info.get("user_role")
    
    
    query = db.query(UserReport)
    
    if role == "admin" and keywords:   
        keyword_conditions = []
        for keyword in keywords.split():
            keyword= f"%{keyword}%"  
            keyword_conditions.extend([
                UserReport.description.ilike(keyword),
                UserReport.task.ilike(keyword),
                UserReport.project.ilike(keyword),
                UserReport.task_id.ilike(keyword),])
        or_condition = or_(*keyword_conditions)
        query = query.filter(or_condition)
        
    elif role == "admin" and not keywords:
        return query.all()

    elif role != "admin" and keywords:
        keyword_conditions = []
        for keyword in keywords.split():
            keyword = f"%{keyword}%"  
            keyword_conditions.extend([
                UserReport.description.ilike(keyword),
                UserReport.task.ilike(keyword),
                UserReport.project.ilike(keyword),
                UserReport.task_id.ilike(keyword),])
        or_condition = or_(*keyword_conditions)
        user = db.query(User).filter(User.email == email).first()
        query = query.filter(UserReport.user_id == user.id,or_condition)
    elif role != "admin" and not keywords:
        user = db.query(User).filter(User.email == email).first()
        return db.query(UserReport).filter(UserReport.user_id == user.id).all()
    return query.all()

"""
@param - month -  equired for month
@param - year -Search the specific report by keywords
@param - db -  Database Session object
@param - token - Verified token
@returns - Monthly report data object
"""

def monthly_report_service(month,year,db,token):
    user_info = decode_token(token)
    user_email = user_info.get("user_mail")
    user_role = user_info.get("user_role")
    if user_role == "admin":
        monthly_report = db.query(UserReport).filter(
        extract('month', UserReport.date) == month,extract('year', UserReport.date) == year).all()
        return monthly_report
    elif user_role == "user":
        user_data = db.query(User).filter(User.email == user_email).first()
        if user_data:
            monthly_report= db.query(UserReport).filter(
            extract('month', UserReport.date) == month,extract('year', UserReport.date) == year,
            UserReport.user_id == user_data.id).all()
            return monthly_report
    else:
        raise HTTPException(status_code=404, detail="user data not found")
    
"""
@param - start_date -  required starting date
@param - end_date - required  ending date
@param - db -  database Session object
@param - token - verified token
@returns -total hours 
"""


def total_hours_by_date_range_service(start_date: date, end_date: date, db: Session, token: str):
    user = decode_token(token)
    user_email = user.get("user_mail")
    user_role = user.get("user_role")

    user_data = db.query(User).filter(User.email == user_email).first()

    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")

    if user_role == "admin":
        total_duration = db.query(UserReport).filter(UserReport.date >= start_date,
            UserReport.date <= end_date).all()
    else:
        total_duration = db.query(UserReport).filter(UserReport.user_id == user_data.id,
            UserReport.date >= start_date,
            UserReport.date <= end_date).all()

    total = timedelta()
    for x in total_duration:
        y = str(x.duration)
        hours, minutes, seconds = map(int, y.split(":"))
        time_delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        total += time_delta

    total_hours = total.total_seconds() / 3600

    return total_hours


"""
@param - db -  database Session object
@param - token - verified token
@param - month - required month to fetch the report
@param- project_name - Project name to retrieve
@param - start_date -  required starting date to fetch the report
@param - end_date - required  ending date to fetch the report
@returns -filterd report data object
"""

def filter_reports_service(db, user_id,token,month, project_name, start_date, end_date):
    decoded_token=decode_token(token)
    role=decoded_token.get("user_role")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if role == "user":
        raise HTTPException(status_code=403, detail="Only admin users can access this endpoint")

    query = db.query(UserReport)

    if month:
        month_mapping = {
            "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
            "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12
        }
        month_number = month_mapping.get(month.upper())
        if month_number:
            query = query.filter(extract("month", UserReport.date) == month_number)

    if project_name:
        query = query.filter(UserReport.project.ilike(f"%{project_name}%"))

    if start_date:
        query = query.filter(UserReport.date >= start_date)

    if end_date:
        query = query.filter(UserReport.date <= end_date)

    filtered_reports = query.filter(UserReport.user_id == user_id).all()
    return filtered_reports


"""
@param - db -  database Session object
@param - token - verified token
@returns -today report 
"""

         
def get_today_reports_service(token,db):
    user_info = decode_token(token)
    user_email = user_info.get("user_mail")
    user_role = user_info.get("user_role")
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    today = date.today()

    if user_role == "admin":
        today_reports = db.query(UserReport).filter(
            extract('day', UserReport.date) == today.day,
            extract('month', UserReport.date) == today.month,
            extract('year', UserReport.date) == today.year
        ).all()
    else:
        today_reports = db.query(UserReport).filter(
            extract('day', UserReport.date) == today.day,
            extract('month', UserReport.date) == today.month,
            extract('year', UserReport.date) == today.year,
            UserReport.user_id == user.id
        ).all()

    return today_reports

