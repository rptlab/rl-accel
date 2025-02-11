from sys import getrefcount
from _rl_accel import calcChecksum

cs = calcChecksum(b"Hello cruel world!")
print(f'calcChecksum(b"Hello cruel world!")={cs!r}')
