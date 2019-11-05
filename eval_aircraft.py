import numpy as np
from models.aircraft import *
from definitions import *

# Which weight estimation do we want to use?
from errikos import *

defs = Definitions()

aircraft = Aircraft(defs)

print(aircraft)

W0 = 17987 * u.kg

