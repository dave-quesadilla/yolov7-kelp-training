import pandas as pd
from io import StringIO


base_results = """
                 all         267         796       0.448       0.501       0.447       0.219
      Attached_Alive         267          67       0.368       0.358       0.242      0.0936
       Attached_Dead         267          37       0.347        0.27       0.266       0.093
      Detached_Alive         267         107       0.501       0.879       0.705       0.444
       Detached_Dead         267          49       0.353       0.327       0.345        0.18
             Embryo         267         159        0.42       0.484       0.395       0.157
          Sporophyte         267         377       0.696       0.686       0.731       0.349
"""

names = "Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95".split()
res = pd.read_csv(StringIO(base_results), sep = "\s+", names=names, header = None).set_index("Class")

print(res.to_latex(float_format="%.2f"))