"""
=========================
run_tvb_smt_sims_main.py
=========================

Wrapper for Sim class in Runner.py.


Usage:
-----

python run_tvb_sims_main.py <parameter_file>

"""
import sys
from sumatra.parameters import build_parameters
from sumatra.decorators import capture

sys.path.append('/media/sf_SharedFolder/Code/git_repos_of_mine/tvb-scripting')
from tvb_scripting.Runner import Sim

@capture
def main(pset_smt):

 Ps = pset_smt.as_dict() 
 S = Sim(Ps)
 S.run()

# Read parameter file
parameter_file = sys.argv[1]
pset_smt  = build_parameters(parameter_file)

# Run
main(pset_smt)
