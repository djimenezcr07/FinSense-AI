from pathlib import Path
import importlib.util
spec=importlib.util.spec_from_file_location('demo',Path(__file__).parents[1]/'scripts'/'generate_demo.py')
demo=importlib.util.module_from_spec(spec);spec.loader.exec_module(demo)
def test_generation(tmp_path):
    a=tmp_path/'a.csv';b=tmp_path/'b.csv'
    x=demo.generate(a);y=demo.generate(b)
    assert x==y and demo.validate(x)==30 and len(x)==150
    assert a.read_bytes()==b.read_bytes()
