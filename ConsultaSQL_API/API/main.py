from fastapi import FastAPI, HTTPException, Depends  
from sqlalchemy.orm import Session  
from typing import List, Optional  
from database import SessionLocal, get_db  
import models  
  
app = FastAPI()  
  
@app.get("/data/", response_model=List[models.DataRead])  
def read_data(  
    UNIDAD_NEGOCIO: Optional[str] = None,  
    REGIONAL: Optional[str] = None,  
    TIPO_OPORTUNIDAD: Optional[str] = None,  
    SEGMENTO: Optional[str] = None,  
    GERENTE_CUENTA: Optional[str] = None,  
    LINEA_NEGOCIO: Optional[str] = None,  
    PRODUCTO: Optional[str] = None,  
    CANTIDAD: Optional[str] = None,  
    TOTAL_ANTES_IVA: Optional[str] = None,  
    FECHA_CIERRE_ESTIMADO: Optional[str] = None,  
    TIPO_ORIGEN: Optional[str] = None,  
    FECHA_CREACION: Optional[str] = None,  
    ESTADO: Optional[str] = None,  
    INDUSTRIA: Optional[str] = None,  
    TIPO_EMPRESA: Optional[str] = None,  
    FABRICANTE_COEM: Optional[str] = None,  
    skip: int = 0,  
    limit: int = 10,  
    db: Session = Depends(get_db)  
):  
    query = db.query(models.Data)  
      
    if UNIDAD_NEGOCIO:  
        query = query.filter(models.Data.UNIDAD_NEGOCIO == UNIDAD_NEGOCIO)  
    if REGIONAL:  
        query = query.filter(models.Data.REGIONAL == REGIONAL)  
    if TIPO_OPORTUNIDAD:  
        query = query.filter(models.Data.TIPO_OPORTUNIDAD == TIPO_OPORTUNIDAD)  
    if SEGMENTO:  
        query = query.filter(models.Data.SEGMENTO == SEGMENTO)  
    if GERENTE_CUENTA:  
        query = query.filter(models.Data.GERENTE_CUENTA == GERENTE_CUENTA)  
    if LINEA_NEGOCIO:  
        query = query.filter(models.Data.LINEA_NEGOCIO == LINEA_NEGOCIO)  
    if PRODUCTO:  
        query = query.filter(models.Data.PRODUCTO == PRODUCTO)  
    if CANTIDAD:  
        query = query.filter(models.Data.CANTIDAD == CANTIDAD)  
    if TOTAL_ANTES_IVA:  
        query = query.filter(models.Data.TOTAL_ANTES_IVA == TOTAL_ANTES_IVA)  
    if FECHA_CIERRE_ESTIMADO:  
        query = query.filter(models.Data.FECHA_CIERRE_ESTIMADO == FECHA_CIERRE_ESTIMADO)  
    if TIPO_ORIGEN:  
        query = query.filter(models.Data.TIPO_ORIGEN == TIPO_ORIGEN)  
    if FECHA_CREACION:  
        query = query.filter(models.Data.FECHA_CREACION == FECHA_CREACION)  
    if ESTADO:  
        query = query.filter(models.Data.ESTADO == ESTADO)  
    if INDUSTRIA:  
        query = query.filter(models.Data.INDUSTRIA == INDUSTRIA)  
    if TIPO_EMPRESA:  
        query = query.filter(models.Data.TIPO_EMPRESA == TIPO_EMPRESA)  
    if FABRICANTE_COEM:  
        query = query.filter(models.Data.FABRICANTE_COEM == FABRICANTE_COEM)  
      
    items = query.offset(skip).limit(limit).all()  
    return items  
  
@app.get("/data/{data_id}", response_model=models.DataRead)  
def read_data_by_id(data_id: int, db: Session = Depends(get_db)):  
    item = db.query(models.Data).filter(models.Data.id == data_id).first()  
    if item is None:  
        raise HTTPException(status_code=404, detail="Data not found")  
    return item  