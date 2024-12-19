class TimeMap:

    def __init__(self):
        self.bucket = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.bucket:
            self.bucket[key] = []
        self.bucket[key].append([value, timestamp])
        
        

    def get(self, key: str, timestamp: int) -> str:
        #we have been given key and timestamp, we need to return value
        res = ""
        values = self.bucket.get(key, [])

        print("what we are looking for ", key, timestamp)
        print("what we have ", values)


        l, r = 0, len(values) - 1


        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

        