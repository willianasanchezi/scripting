from sqlalchemy import Column, String, DateTime, Integer  # Asegúrate de importar Integer  
from database import Base  
from pydantic import BaseModel  
from typing import Optional  
  
class Data(Base):  
    __tablename__ = "data"  
  
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    UNIDAD_NEGOCIO = Column(String(255), index=True)  
    REGIONAL = Column(String(255), index=True)  
    TIPO_OPORTUNIDAD = Column(String(255), index=True)  
    SEGMENTO = Column(String(255), index=True)  
    GERENTE_CUENTA = Column(String(255), index=True)  
    LINEA_NEGOCIO = Column(String(255), index=True)  
    PRODUCTO = Column(String(255), index=True)  
    CANTIDAD = Column(String(255), index=True)  
    TOTAL_ANTES_IVA = Column(String(255), index=True)  
    FECHA_CIERRE_ESTIMADO = Column(DateTime, index=True)  
    TIPO_ORIGEN = Column(String(255), index=True)  
    FECHA_CREACION = Column(DateTime, index=True)  
    ESTADO = Column(String(255), index=True)  
    INDUSTRIA = Column(String(255), index=True)  
    TIPO_EMPRESA = Column(String(255), index=True)  
    FABRICANTE_COEM = Column(String(255), index=True)  
  
class DataRead(BaseModel):  
    id: Optional[int]  
    UNIDAD_NEGOCIO: Optional[str]  
    REGIONAL: Optional[str]  
    TIPO_OPORTUNIDAD: Optional[str]  
    SEGMENTO: Optional[str]  
    GERENTE_CUENTA: Optional[str]  
    LINEA_NEGOCIO: Optional[str]  
    PRODUCTO: Optional[str]  
    CANTIDAD: Optional[str]  
    TOTAL_ANTES_IVA: Optional[str]  
    FECHA_CIERRE_ESTIMADO: Optional[str]  
    TIPO_ORIGEN: Optional[str]  
    FECHA_CREACION: Optional[str]  
    ESTADO: Optional[str]  
    INDUSTRIA: Optional[str]  
    TIPO_EMPRESA: Optional[str]  
    FABRICANTE_COEM: Optional[str]  
  
    class Config:  
        orm_mode = True  