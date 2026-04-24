import zipfile, pathlib, json
base = pathlib.Path('outputs/problem3/colabfold_predictions')
for z in sorted(base.glob('chain*.result.zip')):
    with zipfile.ZipFile(z) as zz:
        top = [n for n in zz.namelist() if '_scores_rank_001_' in n and n.endswith('.json')]
        if not top:
            print(z.name, 'NO rank001 json')
            continue
        name = top[0]
        data = json.loads(zz.read(name).decode('utf-8'))
        keys = sorted(data.keys())
        plddt = data.get('plddt')
        ptm = data.get('ptm')
        iptm = data.get('iptm')
        pae = data.get('pae')
        mean_plddt = sum(plddt)/len(plddt) if isinstance(plddt,list) and plddt else None
        mean_pae = sum(sum(r) for r in pae)/sum(len(r) for r in pae) if isinstance(pae,list) and pae and isinstance(pae[0],list) else None
        print(f"{z.name}: file={name}")
        print('  keys=', keys)
        print('  mean_plddt=', round(mean_plddt,2) if mean_plddt is not None else None, 'ptm=', ptm, 'iptm=', iptm, 'mean_pae=', round(mean_pae,2) if mean_pae is not None else None)
