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


@router.put("/jobs/{id}")
def update_job():
    pass


@router.post("/jobs/{id}/application")
def apply_for_job():
    pass


@router.get("/jobs/{id}/applications")
def list_job_applications_recruiter():
    pass


@router.get("/applications")
def list_applications_made_by_candidate():
    pass


@router.get("/applications/{id}")
def get_applications_made_by_candidate():
    pass


@router.post("/applications/{id}/cancel")
def cancel_an_application():
    pass


@router.get("/candidates")
def list_candidates():
    pass


@router.post("/candidates")
def register_candidate():
    pass


@router.get("/candidates/{id}")
def get_candidate():
    pass


@router.put("/candidates/{id}")
def update_candidate():
    pass


@router.delete("/candidates/{id}")
def delete_candidate():
    pass
