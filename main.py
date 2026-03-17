import matplotlib.pyplot as plt
from probleme_boule import solution_analytique, solution_numerique

# Paramètres physiques
r     = 0.1      # rayon de la sphère (m)
rho_f = 1025     # masse volumique du fluide (kg/m³)
rho_s = 500      # masse volumique du solide (kg/m³)
mu    = 1        # viscosité dynamique (Pa·s)
g     = 9.81     # accélération gravitationnelle (m/s²)

# Paramètres numériques
CI  = 0
a, b = 0, 20
h_num = 0.1    # pas RK4
h_ref = 0.01     # pas solution de référence

v_th, t_th = solution_analytique(CI, a, b, h_ref, r, rho_s, rho_f, mu, g)
v_rk, t_rk = solution_numerique( CI, a, b, h_num, r, rho_s, rho_f, mu, g)

plt.figure()
plt.plot(t_th, v_th, label="Analytique")
plt.plot(t_rk, v_rk, '--', label=f"RK4 (h={h_num})")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse (m/s)")
plt.title("Vitesse de chute d'une sphère — Stokes")
plt.legend()
plt.tight_layout()
plt.show()