import numpy as np
from math import sqrt, sin, cos

# Initialize |0> and |1> Ket-Vectors
Ket0 = np.array([[1],[0]])
Ket1 = np.array([[0],[1]])

# Input Components and Create State Vector |X>
print("--- Initializing State Vector |X> ---")
CompX = complex(input("Enter C1 (Amplitude for |0>): "))
CompY = complex(input("Enter C2 (Amplitude for |1>): "))
KetX = CompX*Ket0 + CompY*Ket1

print("\nOriginal State Vector |X>:")
print(KetX)

# Initialize Pauli's Matrices
PauliI = np.array([[1,0],[0,1]])
PauliX = np.array([[0,1],[1,0]])
PauliY = np.array([[0,-1j],[1j,0]])
PauliZ = np.array([[1,0],[0,-1]])

# Initialize Hadamard Matrix
H = np.array([[1,1],[1,-1]])/sqrt(2)

# Input Required Phase Angle
print("\n--- Phase Shift Parameters ---")
r = float(input("Enter Phase Angle (in radians): "))
P = np.array([[1,0],[0,complex(cos(r),sin(r))]])

# Creating A Sample ROOT(NOT) Gate
RootNOT = np.array([[1+1j,1-1j],[1-1j,1+1j]])/2

# --- Applying Gates on State Vector |X> ---

print("\n--- Pauli-X (NOT) Gate ---")
print(np.matmul(PauliX, KetX))

print("\n--- Pauli-Z (Phase Flip) Gate ---")
print(np.matmul(PauliZ, KetX))

print("\n--- Hadamard (H) Gate ---")
print(np.matmul(H, KetX))

print(f"\n--- Phase Shift Gate (Angle: {r}) ---")
print(np.matmul(P, KetX))

print("\n--- RootNOT Gate (Applied Twice) ---")
print(np.matmul(RootNOT, np.matmul(RootNOT, KetX)))