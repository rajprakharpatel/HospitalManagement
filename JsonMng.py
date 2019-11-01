import json as j


def dumps(fn, ls):
    j_file_ = open(fn, "w")
    j_file_.write(j.dumps(ls, indent=4))
    j_file_.close()


def loads(fn):
    with open(fn) as j_file_:
        return j.loads(j_file_.read())
