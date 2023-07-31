from fastapi import APIRouter

router = APIRouter()


@router.get("/skills")
def list_skills():
    pass


@router.get("/locations")
def list_locations():
    pass


@router.get("/jobs")
def list_jobs():
    pass


@router.post("/jobs")
def post_job():
    pass


@router.get("/jobs/{id}")
def get_job():
    pass
