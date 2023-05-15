from sqlalchemy.orm import Session
from backend.schemas.tags import TagCreate
from backend.db.models import Tag
from sqlalchemy.exc import IntegrityError
from sqlalchemy import exc
from fastapi import HTTPException

def create_new_tag(tag: TagCreate,db: Session):
    existing_tag = db.query(Tag).filter_by(name=tag.name).first()
    if existing_tag:
        raise HTTPException(status_code=409, detail="Tag with the same name already exists")
    try:
        new_tag = Tag(name=tag.name, description=tag.description)
        db.add(new_tag)
        db.commit()
        db.refresh(new_tag)
        return new_tag
    except exc.SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
def get_all_tags(db: Session):
    all_tags = db.query(Tag).all()
    return all_tags

def get_tag_id(db: Session, id: int):
    tag = db.query(Tag).filter(Tag.id == id).first()
    return tag