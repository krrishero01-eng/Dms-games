from fastapi import APIRouter, HTTPException
from random import choice
from database.relation_database import relation_db

router = APIRouter()

@router.get("/")

