signup= {
    400: {
        "description": "Bad Request",
        "content": {"application/json": {"example": {"error": "User with this email already exists"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}

login= {
    401: {
        "description": "Unauthorized",
        "content": {"application/json": {"example": {"error": "Unauthorized"}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}


refresh__token= {
    403: {
        "description": "Unauthorized",
        "content": {"application/json": {"example": {"error": "Invalid token or expired token."}}},
    },
    500: {
        "description": "Internal Server Error",
        "content": {"application/json": {"example": {"error": "Internal Server Error"}}},
    },
}



