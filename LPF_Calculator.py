import math
import numpy as np

# Given constants
M = 2**7
omega_ref = 2 * np.pi * 50e6
KVCO = 190e6 * 2 * np.pi

IP = 0.1869e-3
# obtained by sweeping the output of the charge pump and finding where the 
# two current matches, ideally at 0.9V (or VCTRL such that VCO output at M*VREF)
# The larger the L the harder it is to match at a desired voltage, but it also
# reduces the ripple if tuned successfully

# Constraints
theorem_factor = 10
#increase this means less bandwidth, but could see an improvement in VQ ripple
zeta = 1
# You may increase zeta for a better response
damping_factor = np.sqrt(2*zeta**2 + np.sqrt(4*zeta**4+1));
print(damping_factor)
omega_target = omega_ref / (theorem_factor * damping_factor)
print(omega_target)
print(f"Solved that at {IP} A, omega_n should be around {omega_target}")

#omega_n = ((IP_choosen * KVCO) / (2 * np.pi * M * C1)) ** 0.5
C1_solved = (IP * KVCO) / (2 * np.pi * M * omega_target**2)
C1_result = C1_solved / 1e-15
print(f"Solved that at {IP} A, C1={C1_result}f, C2={0.2*C1_result}f")

# Solve for R1 using the zeta equation
R1_solved = 2 * zeta / (((IP * KVCO * C1_solved) / (2 * np.pi * M)) ** 0.5)
print(f"Solved that at {IP} A, zeta=1, R1={R1_solved}")

pm = np.arctan(2*zeta*np.sqrt(2*zeta+np.sqrt(4*np.power(zeta, 4) + 1)))
print(f"Solved that at {IP} A, PM={pm* 180/np.pi}")
