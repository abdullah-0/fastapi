from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.dependency import get_db, get_auth_user
from models import Entity, User
from schemas.entity import EntityCreate, EntityUpdate, EntityDetail, EntityList

router = APIRouter()



def get_entity(db: Session, user_id: int, entity_id: int | None = None):
    query = db.query(Entity).filter(Entity.user_id == user_id)
    if entity_id:
        return query.filter(Entity.id == entity_id).first()
    return query.all()

@router.post("/", response_model=EntityDetail)
def create_entity(entity_data: EntityCreate, db: Session = Depends(get_db), user: User = Depends(get_auth_user)):
    new_entity = Entity(**entity_data.model_dump(), user_id=user.id)
    db.add(new_entity)
    db.commit()
    db.refresh(new_entity)
    return new_entity

@router.get("/", response_model=list[EntityList])
def list_entity(db: Session = Depends(get_db), user: User = Depends(get_auth_user)):
    return get_entity(db,user.id)

@router.get("/{entity_id}", response_model=EntityDetail)
def detail_entity(entity_id: int, db: Session = Depends(get_db), user: User = Depends(get_auth_user)):
    entity = get_entity(db,user.id,entity_id)
    if not entity:
        raise HTTPException(status_code=404, detail="Entity not found")
    return entity

@router.put("/{entity_id}", response_model=EntityDetail)
def update_entity(entity_id: int, update_data: EntityUpdate, db: Session = Depends(get_db), user: User = Depends(get_auth_user)):
    entity = get_entity(db,user.id,entity_id)
    if not entity:
        raise HTTPException(status_code=404, detail="Entity not found")
    for key, value in update_data.model_dump().items():
        setattr(entity, key, value)
    db.commit()
    db.refresh(entity)
    return entity

@router.delete("/{entity_id}", status_code=204)
def delete_entity(entity_id: int, db: Session = Depends(get_db), user: User = Depends(get_auth_user)):
    entity = get_entity(db,user.id,entity_id)
    if not entity:
        raise HTTPException(status_code=404, detail="Entity not found")
    db.delete(entity)
    db.commit()
