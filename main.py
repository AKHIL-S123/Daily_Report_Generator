import uvicorn
from app.configuration.config import *
from app.api.report.router import report
from app.api.user.router import user
from app.api.project.router import project


Base.metadata.create_all(engine)


app.include_router(user)
app.include_router(report)    
app.include_router(project)

if __name__ == "__main__":
    uvicorn.run("main:app",port = 8000,reload=True)
    # uvicorn.run("main:app", host="192.168.29.93", port = 8000,reload=True)
    