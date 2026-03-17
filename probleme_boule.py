from math import exp
from runge_kutta import runge_kutta


def solution_analytique(CI, a, b, h, r, rho_s, rho_f, mu, g):
    """
    Solution exacte de la vitesse de chute d'une sphère (loi de Stokes).

    v(t) = v_inf * (1 - exp(-t / tau))
    """
    v_inf = (2 * r**2 * (rho_f - rho_s) * g) / (9 * mu)
    tau   = (2 * rho_s * r**2) / (9 * mu)

    t_list = []
    v_list = []

    t = a
    while t <= b:
        t_list.append(t)
        v_list.append(v_inf * (1 - exp(-t / tau)))
        t += h

    return v_list, t_list


def solution_numerique(CI, a, b, h, r, rho_s, rho_f, mu, g):
    """
    Solution numérique par RK4 de v' = f(t, v).
    """
    def f(t, v):
        return ((rho_f - rho_s) * g / rho_s) - (9 * mu * v) / (2 * rho_s * r**2)

    return runge_kutta(f, CI, a, b, h)