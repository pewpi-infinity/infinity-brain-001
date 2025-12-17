import qutip as qt
import numpy as np

# Node-specific entangled state with phase from meaning
phase = 0.0283026
ket00 = qt.tensor(qt.basis(2, 0), qt.basis(2, 0))
ket11 = qt.tensor(qt.basis(2, 1), qt.basis(2, 1))
bell = (ket00 + np.exp(1j * phase) * ket11) / np.sqrt(2)
rho = bell * bell.dag()

print("Node 001 Entangled Density Matrix (influenced by 'single'):")
print(rho)

# Expectations and correlation (entanglement marker)
z1 = qt.tensor(qt.sigmaz(), qt.qeye(2))
z2 = qt.tensor(qt.qeye(2), qt.sigmaz())
zz = qt.tensor(qt.sigmaz(), qt.sigmaz())
print(f"<Z1>: {qt.expect(z1, rho)}")
print(f"<Z2>: {qt.expect(z2, rho)}")
print(f"<Z1 Z2>: {qt.expect(zz, rho)}")  # Close to 1 indicates entanglement
