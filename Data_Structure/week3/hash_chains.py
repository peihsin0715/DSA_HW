class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.string = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]  # 使用桶來儲存字串

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == 'check':
            chain = self.buckets[query.ind]
            self.write_chain(chain)
        else:
            hash_value = self._hash_func(query.string)
            bucket = self.buckets[hash_value]

            if query.type == 'find':
                self.write_search_result(query.string in bucket)
            elif query.type == 'add':
                if query.string not in bucket:
                    bucket.insert(0, query.string)
            else:
                if query.string in bucket:
                    bucket.remove(query.string)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()