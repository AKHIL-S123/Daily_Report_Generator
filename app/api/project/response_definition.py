create_project_response= {
    403: {
        "description": "Forbidden",
        "content": {"application/json": {"example": {"error": "User cannot create a project"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}

get_project_response= {
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}


update_project_response= {
    403: {
        "description": "Unauthorized",
        "content": {"application/json": {"example": {"error": "Only admin users can update projects"}}},
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


delete_project_respose= {
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
    },
}

