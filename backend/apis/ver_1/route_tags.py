from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import Depends, HTTPException,status
from backend.db.session import get_db
from backend.schemas.tags import TagCreate, TagView
from backend.db.repository.tags import create_new_tag, get_all_tags, get_tag_id

router = APIRouter()

@router.post("/create/", response_model=TagView)
def create_tag(tag: TagCreate,db: Session = Depends(get_db)):
        try:
            tag = create_new_tag(db=db,tag=tag)
            return tag
        finally:
            pass

@router.get("/all/")
def get_tags(db: Session = Depends(get_db)):
    all_tags = get_all_tags(db=db)
    if all_tags is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tags not found")
    return all_tags
@router.get("/get/{id}", response_model=TagView)
def get_tag_by_id(id:int, db: Session = Depends(get_db)):
    tag = get_tag_id(db=db, id=id)
    if tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    return tag