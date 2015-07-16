import json
D = json.load(open('necessary_dirtree.json'))
L = {s:D[s] for s in open('list').read().splitlines() if not s.startswith('#')}
#print(sep='\n', *sorted(L))
def get_src(D):
    for v in D.values():
        if isinstance(v, dict):
            yield from get_src(v)
        else:
            yield v
with open('Info.csv','w') as f:
    f.write('Source, Destination, Path\n')
    for s in sorted(get_src(L)):
        source = s
        destination = s.split('/',4)[4]
        path = destination.rsplit('/',1)[0]
        f.write('{source}, {destination}, {path}\n'.format(**locals()))
