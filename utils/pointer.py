class ptr:
    def __get__(self, obj, obj_type=None):
        return obj._data

    def __set__(self, obj, d):
        obj._data = d

    def __getitem__(self, obj, item):
        return obj._data[item]

    def __setitem__(self, obj, index, value):
        obj._data[index] = value