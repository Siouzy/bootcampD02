class CsvReader():

    def __init__(
            self,
            filename=None,
            sep=',',
            header=False,
            skip_top=0,
            skip_bottom=0
            ):
        self.filename = filename
        self.sep = sep
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.error = False
        try:
            f = open(filename)
            content = f.read().splitlines()
            if header:
                self.header = content[0].split(sep)
                content = content[1:]
            else:
                self.header = None
            content = content[skip_top:len(content) - skip_bottom]
            self.data = []
            line_size = 0
            if header:
                keys = self.header
                line_size = len(keys)
                for line in content:
                    new_dic = {}
                    new_line = line.split(sep)
                    if len(new_line) != line_size:
                        self.error = True
                        return None
                    for key, val in zip(keys, new_line):
                        new_dic[key] = val
                    self.data.append(new_dic)
            else:
                first = True
                for line in content:
                    new_line = line.split(sep)
                    if first:
                        line_size = len(new_line)
                        first = False
                    elif len(new_line) != line_size:
                        self.error = True
                        return None
                    self.data.append(new_line)
        except FileNotFoundError:
            self.error = True
            return None

    def __enter__(self):
        if self.error:
            return None
        else:
            return self

    def __exit__(self, exc_type, exc_value, tb):
        return None

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header
