class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.cache_dict = {}
        self.capacity = capacity

    def get(self, key: str) -> str:
        if key in self.cache_dict: # чтобы неявно хранить порядок использования в структуре словаря
			res = self.cache_dict[key]
            self.cache_dict.pop(key)
			self.cache_dict[key] = res # ставим значение в конец
            return res
        else:
            return ''

    def set(self, key: str, value: str) -> None:
        if key in self.cache_dict: # чтобы неявно хранить порядок использования в структуре словаря
            self.cache_dict.pop(key)
        self.cache_dict[key] = value
        if len(self.cache_dict) > self.capacity:
            self.cache_dict = dict(list(self.cache_dict.items())[-self.capacity : ])


    def rem(self, key: str) -> None:
        try:
            self.cache_dict.pop(key)
        except KeyError:
            pass
