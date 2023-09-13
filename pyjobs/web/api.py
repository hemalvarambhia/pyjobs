from enum import Enum
from uuid import UUID

from fastapi import APIRouter, Query
from pydantic import BaseModel
from starlette import status

router = APIRouter()


class SortEnum(Enum):
    ASC = "asc"
    DESC = "desc"


class Pagination(BaseModel):
    pass


def pagination_params(
    page: int = Query(ge=1, required=False, default=1),
    perPage: int = Query(ge=1, le=100, required=False, default=100),
    order: SortEnum = SortEnum.DESC,
):
    pass


@router.get("/skills")
def list_skills(
    page: int = Query(ge=1, required=False, default=1),
    perPage: int = Query(ge=1, le=100, required=False, default=100),
    order: SortEnum = SortEnum.DESC,
):
    pass


@router.get("/locations")
def list_locations():
    pass


@router.get("/jobs")
def list_jobs():
    pass


@router.post("/jobs", status_code=status.HTTP_201_created)
def post_job():
    pass


@router.get("/jobs/{id}")
def get_job(id: UUID):
    pass


@router.put("/jobs/{id}")
def update_job(id: UUID):
    pass


@router.post("/jobs/{id}/application", status_code=status.HTTP_201_CREATED)
def apply_for_job(id: UUID):
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


@router.get("/candidates/{id}/cv")
def download_cv():
    pass


@router.put("/candidates/{id}/cv")
def upload_cv():
    pass
