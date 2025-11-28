from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship

from ch4 import model


metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("qty", Integer, nullable=False),
    Column("orderid", String(255)),
)

batches = Table(
    "batches",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("reference", String(255)),
    Column("sku", String(255)),
    Column("_purchased_quantity", Integer, nullable=False),
    Column("eta", Date, nullable=True),
)

allocations = Table(
    "allocations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("orderline_id", ForeignKey("order_lines.id")),
    Column("batch_id", ForeignKey("batches.id")),
)


def start_mappers():
    # mapper: Python模型类绑定数据库表
    lines_mapper = mapper(model.OrderLine, order_lines)
    # relationship: 用于定义模型类之间的关联关系（让 ORM 能自动处理表间查询，比如查一个批次时，自动带出它关联的所有订单行）。
    mapper(
        model.Batch, # 要映射的 Python 模型类（批次模型）
        batches, # 要绑定的数据库表名（批次表）
        properties={ # 额外配置：定义模型的属性/表间关系
            "_allocations": relationship( # 给 Batch 模型添加 _allocations 属性，类型是“关联关系”
                lines_mapper, # 关联的另一方模型（即上面映射的 OrderLine 模型）
                secondary=allocations,  # 多对多关系的中间关联表（关键！）
                collection_class=set, # 关联数据的存储类型：用集合（去重）
            )
        },
    )