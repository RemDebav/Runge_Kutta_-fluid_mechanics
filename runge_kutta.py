def runge_kutta(f, CI, a, b, h):
    """
    Résolution de x' = f(t, x) par la méthode de Runge-Kutta d'ordre 4.

    Paramètres
    ----------
    f   : callable(t, x) -> float
    CI  : condition initiale x(a)
    a,b : intervalle d'intégration
    h   : pas

    Retourne
    --------
    x_list, t_list : listes des valeurs de x et t
    """
    t, x = a, CI
    t_list = [t]
    x_list = [x]

    while t < b:
        k1 = f(t,         x)
        k2 = f(t + h/2,   x + h/2 * k1)
        k3 = f(t + h/2,   x + h/2 * k2)
        k4 = f(t + h,     x + h   * k3)

        x += h / 6 * (k1 + 2*k2 + 2*k3 + k4)
        t += h

        t_list.append(t)
        x_list.append(x)

    return x_list, t_list