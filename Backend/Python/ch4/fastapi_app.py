from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, Field

import config
from ch4 import model
import orm
import repository
import services


orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = FastAPI()


class AllocateRequest(BaseModel):
    """分配请求的请求体模型，自动验证数据格式"""
    orderid: str = Field(description="订单 ID")
    sku: str = Field(description="商品 SKU（库存编码）")
    qty: int = Field(ge=1, description="请求分配的数量（必须大于 0）")


@app.post("/allocate")
def allocate_endpoint(data: AllocateRequest):
    session = get_session()
    batches = repository.SqlAlchemyRepository(session).list()
    line = model.OrderLine(
        data.orderid, 
        data.sku, 
        data.qty,
    )
    
    batchref = model.allocate(line, batches)
    return {"batchref": batchref}, 201