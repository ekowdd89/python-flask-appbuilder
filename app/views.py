from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
# from wtforms import TextAreaField
from flask_appbuilder.forms import TextAreaField
from flask_appbuilder.fieldwidgets import BS3TextAreaFieldWidget
from . import appbuilder, db
from . import models

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""

class ContactModelView(ModelView):
    datamodel = SQLAInterface(models.Contact)

    label_columns = {"contact_group": "Contact Group"}
    list_columns = ["name", "personal_phone","brithday", "contact_group"]

    show_fieldsets = [
        (
            'Summary',
            {"fields": ["name", "email", "address", "contact_group"]}
        ),
        (
            'Personal Info',
            {'fields':["personal_phone", "personal_cellphone", "birthday"]}
        )
    ]



class GroupModelView(ModelView):
    datamodel = SQLAInterface(models.ContactGroup)
    related_views = [ContactModelView]


class PostModelView(ModelView):
    datamodel = SQLAInterface(models.Post)

    label_columns = {"post": "Post"}
    list_columns = ["title", "content"]

    show_fieldsets = [
        (
            'Summary',
            {"fields": ["title", "content"]}
        ),
    ]

    add_fieldsets = [
        (
            'Summary',
            {"fields": ["title", "content"]}
        ),
    ]



    add_form_extra_fields = {
        "content": TextAreaField(
            "Content",
            widget=BS3TextAreaFieldWidget(),
            render_kw={
                "rows": 10,
                "class": "form-control form-textarea tinymce"
            }
        )
    }


class CommentModelView(ModelView):
    datamodel = SQLAInterface(models.Comment)
    related_views = [PostModelView]


class ProvinceModelView(ModelView):
    datamodel = SQLAInterface(models.Province)
    label_columns = {"province": "Province"}
    list_columns = ["name"]

    show_fieldsets = [
        (
            "Summary",
            {"fields": ["name"]}
        )
    ]

class CityModelView(ModelView):
    datamodel = SQLAInterface(models.City)
    label_columns = {"city": "City"}
    list_columns = ["name", "province"]

    show_fieldsets = [
        (
            "Summary",
            {"fields": ["name", "province"]}
        )
    ]
    related_views = [ProvinceModelView]


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()

appbuilder.add_view(
    GroupModelView,
    "List Groups",
    icon="fa-folder-open-o",
    category="Contacts",
    category_icon='fa-envelope'
)

appbuilder.add_view(
    ContactModelView,
    "List Contacts",
    icon="fa-envelope",
    category="Contacts"
)

appbuilder.add_view(
    PostModelView,
    "List Posts",
    icon="fa-folder-open-o",
    category="Posts",
    category_icon='fa-envelope'
)

appbuilder.add_view(
    ProvinceModelView,
    "List Provinces",
    icon="fa-folder-open-o",
    category="Provinces",
    category_icon='fa-envelope'
)
appbuilder.add_view(
    CityModelView,
    "List Cities",
    icon="fa-folder-open-o",
    category="Cities",
    category_icon='fa-envelope'
)