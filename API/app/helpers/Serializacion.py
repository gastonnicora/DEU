class Serializacion(object):

    @classmethod
    def dump(cls, obj,nombre="", paged=False, many=False):
        if paged and many:
            return cls._serialize_collection(obj,nombre)
        elif many:
            return cls._serialize_collection_all(obj,nombre)
        else:
            return cls._serialize(obj)

    @classmethod
    def _serialize_collection_all(cls, all,nombre):
        return {
            "Total": len(all),
            nombre: [cls._serialize(elem) for elem in all]
        }

    @classmethod
    def _serialize_collection(cls, pagination,nombre):
        return {
            "Total": pagination.total,
            "Pagina": pagination.page,
            "Paginas_totales":pagination.pages,
            nombre: [cls._serialize(elem) for elem in pagination.items]
        }


    @classmethod
    def _serialize(cls, obj):
        return  { attr.name: getattr(obj, attr.name) for attr in obj.__table__.columns }