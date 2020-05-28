class TinyStatistician:

    def mean(self, x):
        size = len(x)
        if size == 0:
            return None
        sum = 0
        for val in x:
            sum += val
        return float(sum / size)

    def median(self, x):
        size = len(x)
        if size == 0:
            return None
        mid = int(size / 2)
        x.sort()
        return float(x[mid])

    def quartile(self, x, percentile):
        size = len(x)
        if size == 0:
            return None
        x.sort()
        index = int(size * percentile / 100)
        return float(x[index])

    def var(self, x):
        size = len(x)
        if size == 0:
            return None
        m = self.mean(x)
        sum = 0
        for val in x:
            sum += (val - m) ** 2
        return float(sum / size)

    def std(self, x):
        size = len(x)
        if size == 0:
            return None
        return self.var(x) ** 0.5
