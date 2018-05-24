import filecmp

import Takuzu

def compare_solutions(fname1, fname2):
    return filecmp.cmp(fname1, fname2, shallow=False)

tak = Takuzu.Takuzo("petit_binero")
tak.solve()
