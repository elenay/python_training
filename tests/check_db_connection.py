__author__ = 'eya'
from fixture.orm import OrmFixture
from model.group import Group

db = OrmFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    i = []
    groups = db.get_group_list()
    print(groups)
    for g in groups:
        # group = groups[g]
        # group_id = group[:3]
        group_id = Group.id
        i.append(group_id)
    print (i)
    # for item in db.get_group_list:
    #     i.append(db.get_group_list[0])
    # l = []
    # for ids in i:
    #     l = db.get_contacts_in_any_group(Group(id=i))
    # for item in l:
    #     print(item)
    # print (len(l))
finally:
    pass #db.destroy()
