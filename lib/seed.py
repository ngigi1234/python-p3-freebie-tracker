# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Sample data
company1 = Company(name='Company1', founding_year=2000)
company2 = Company(name='Company2', founding_year=1995)

dev1 = Dev(name='Dev1')
dev2 = Dev(name='Dev2')

freebie1 = Freebie(item_name='T-shirt', value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name='Sticker', value=5, dev=dev2, company=company2)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()