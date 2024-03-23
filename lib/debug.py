# debug.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Sample query to test relationships
dev1 = session.query(Dev).filter_by(name='Dev1').first()
print(dev1.companies)  # Should print the companies associated with Dev1

company1 = session.query(Company).filter_by(name='Company1').first()
print(company1.freebies)  # Should print the freebies associated with Company1

# Test Company methods
new_dev = Dev(name='NewDev')
new_freebie = company1.give_freebie(new_dev, 'Hat', 15)
session.add(new_dev)
session.add(new_freebie)
session.commit()

# Print the details of the new freebie
print(new_freebie.print_details())

# Test Dev methods
print(dev1.received_one('T-shirt'))  # Should return True

Dev.give_away(dev1, Freebie)
session.commit()
print(Freebie.dev.name)  