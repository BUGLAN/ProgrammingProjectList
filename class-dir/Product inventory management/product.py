from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Product(Base):
    """
    产品类: 记录产品的价格, 名字, 库存
    id: 主键
    price: 价格
    stock: 库存
    """
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    nums = Column(Integer)
    stock_id = Column(Integer, ForeignKey('stock.id'))

    def __str__(self):
        return f'<Product {self.name}>'

    def __repr__(self):
        return f'<Product {self.name}>'


class Stock(Base):
    """
    库存类: 记录各种产品并能计算库存的总价值。
    """
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    # product_id = Column(Integer, ForeignKey('product.id'))
    procuts = relationship('Product', backref='stock', lazy='dynamic')

    def __str__(self):
        return f'<Stock {str(p.name for p in self.procuts)}>'
    
    def list_all_product(self):
        return [p for p in self.procuts]

    def total_money(self):
        return sum(p.price for p in self.procuts)


engine = create_engine('sqlite:///product.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# define product
product = Product()
product.id = 1
product.name = "高考试卷"
product.price = 400
product.nums = 500

session.add(product)
session.commit()

# define stock

stock = Stock()
stock.id = 1
stock.procuts = [product]
session.add(stock)
session.commit()

print(stock.list_all_product())
print(stock.total_money())