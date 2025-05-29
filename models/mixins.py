# models/mixins.py
class SerializableMixin:
    def to_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                data[key] = value
        return data

    @classmethod
    def from_dict(cls, data):
        raise NotImplementedError("O método 'from_dict' deve ser implementado pela classe filha.")