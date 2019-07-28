import datetime
import pytz
from models import Person, Manager, Worker

for i in range(200):
      birthday = datetime.datetime(year=1980 + i % 20, month=1 + i % 12, day=1 + i % 28, tzinfo=pytz.timezone('Asia/Tokyo'))
      Person.objects.create(name="person{}".format(i), birthday=birthday, sex=Person.MAN, address_from=Person.TOKYO, current_address=Person.TOKYO, email="person{}@gmail.com".format(i))

dep_list  = [Manager.DEP_ACCOUNTING, Manager.DEP_SALES, Manager.DEP_PRODUCTION, Manager.DEP_DEVELOPMENT, Manager.DEP_HR, Manager.DEP_FIN, Manager.DEP_AFFAIRS, Manager.DEP_PLANNING, Manager.DEP_BUSINESS, Manager.DEP_DISTR, Manager.DEP_IS]

for i in range(1, 201):
    p = Person.objects.get(id=i)
    joined_date = datetime.datetime(year=2005 + i % 10, month=1 + i % 12, day=1 + i % 28, tzinfo=pytz.timezone('Asia/Tokyo'))
    Manager.objects.create(person=p, department=dep_list[i % 11], joined_at=joined_date)

for i in range(201, 1201):
    p = Person.objects.get(id=i)
    m = Manager.objects.get(id=1 + i % 200)
    joined_date = datetime.datetime(year=2005 + i % 10, month=1 + i % 12, day=1 + i % 28, tzinfo=pytz.timezone('Asia/Tokyo'))
    Worker.objects.create(person=p, manager=m, joined_at=joined_date)
