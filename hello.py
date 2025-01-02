from pyquil import get_qc, Program
from pyquil.gates import CNOT, Z, MEASURE
from pyquil.api import local_forest_runtime
from pyquil.quilbase import Declare

prog = Program(
    Declare("ro", "BIT", 2),
    Z(0),
    CNOT(0, 1),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1)),
).wrap_in_numshots_loop(10)

with local_forest_runtime():
    qvm = get_qc('9q-square-qvm')
    bitstrings = qvm.run(qvm.compile(prog)).get_register_map().get("ro")