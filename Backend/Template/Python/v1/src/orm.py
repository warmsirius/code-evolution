from sqlalchemy import MetaData, Column, Table, Integer, String
from sqlalchemy.orm import mapper, relationship

from . import model


metadata = MetaData()

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(50)),
    Column('qty', Integer, nullable=False),
    Column('order_id', String(50)),
)



def start_mappers():
    """启动ORM映射"""
    lines_mapper = mapper(model.OrderLine, order_lines)

