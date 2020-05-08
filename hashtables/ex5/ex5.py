import os

def finder(files, queries):
    path = {}

    hashtable = {}
    q = {}
    result = []
    for i in queries:
        q[i] = []
    for f in files:
        hashtable[f] = os.path.basename(f)
    for key in hashtable:
        if hashtable[key] in q:
            result.append(key)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
