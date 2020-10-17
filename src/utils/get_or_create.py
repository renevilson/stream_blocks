from sqlalchemy.sql import ClauseElement

from src.settings import Session


def get_or_create(model, defaults=None, **kwargs):
    session = Session()
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        session.commit()
        return instance, True
