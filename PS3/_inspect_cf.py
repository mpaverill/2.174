import zipfile, pathlib, re
base = pathlib.Path('outputs/problem3/colabfold_predictions')
zips = sorted(base.glob('chain*.result.zip'))
print('found', len(zips))
for z in zips:
    print('\n==', z.name, '==')
    with zipfile.ZipFile(z) as zz:
        for n in zz.namelist():
            if re.search(r'(ranking|scores|result.*json|confidence).*\.json$', n):
                print('json', n)
