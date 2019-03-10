class add(int):
    def __call__(self, v):
        return add(self + v)