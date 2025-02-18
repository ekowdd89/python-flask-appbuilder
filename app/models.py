from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Contact(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    address =  Column(String(564), default='Street ')
    birthday = Column(Date)
    personal_phone = Column(String(20))
    personal_cellphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey('contact_group.id'))
    contact_group = relationship("ContactGroup")

    def __repr__(self):
        return self.name

class Post(Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(564), nullable=False)
    def __str__(self):
        return self.title

class Comment(Model):
    id = Column(Integer, primary_key=True)
    content = Column(String(564), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post")

class Province(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    def __repr__(self):
        return self.name
class City(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    province_id = Column(Integer, ForeignKey('province.id'))
    province = relationship("Province")
    def __repr__(self):
        return self.name