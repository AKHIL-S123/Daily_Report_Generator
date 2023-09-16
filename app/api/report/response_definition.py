create_report_response= {
   401: {
        "description": "Unauthorized",
        "content": {"application/json": {"example": {"error": "Invaild user"}}},
    },
    403: {
        "description": "Forbidden",
        "content": {"application/json": {"example": {"error":"Onl user can create report"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}

get_report_response= {
    
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"error": " Report not Found"}}},
    },
    403: {
        "description": "Forbidden",
        "content": {"application/json": {"example": {"error": "You are not allowed to access this report"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}


update_report_response= {
    403: {
        "description": "Unauthorized",
        "content": {"application/json": {"example": {"error": "You are not allowed to access this report"}}},
    },
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"error": "Project Not Found"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}


delete_report_respose= {
    403: {
        "description": "Unauthorized",
        "content": {"application/json": {"example": {"error": "Only admin can delete  projects details"}}},
    },
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"error": " Project Not Found"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    }
}

get_all_report_response= {
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}

monthly_report_response= {
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"error": "User Not Found"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
    
}
total_hours_response= {
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"error": " User Not Found"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    }
}
get_today_report_response= {
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"error": " User Not Found"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
    
}
filter_report_response= {
    404: {
        "description": "Not Found",
        "content": {"application/json": {"example": {"error": " User Not Found"}}},
    },
    403: {
        "description": "Unauthorized",
        "content": {"application/json": {"example": {"error": "Only admin can filter report details"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}
