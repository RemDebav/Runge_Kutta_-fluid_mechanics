# Runge-Kutta — Chute d'une sphère en fluide visqueux

Simulation numérique de la vitesse de chute d'une sphère dans un fluide visqueux (régime de Stokes), comparée à la solution analytique.

## Problème physique

On modélise la vitesse $v(t)$ d'une sphère soumise à :
- la **poussée d'Archimède**
- la **force de traînée visqueuse** (loi de Stokes)

Ce qui donne l'équation différentielle :

$$v'(t) = \frac{(\rho_f - \rho_s) \, g}{\rho_s} - \frac{9 \mu}{2 \rho_s r^2} \, v(t)$$

Dont la solution analytique est :

$$v(t) = v_\infty \left(1 - e^{-t/\tau}\right), \quad v_\infty = \frac{2r^2(\rho_f - \rho_s)g}{9\mu}, \quad \tau = \frac{2\rho_s r^2}{9\mu}$$

## Structure du projet

```
├── main.py              # Script principal — paramètres et tracé
├── probleme_boule.py    # Solutions analytique et numérique
└── runge_kutta.py       # Solveur RK4 générique
```

## Méthode numérique

Runge-Kutta d'ordre 4 (RK4) :

$$x_{n+1} = x_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

## Paramètres par défaut

| Paramètre | Valeur | Description |
|---|---|---|
| `r` | 0.1 m | Rayon de la sphère |
| `rho_s` | 500 kg/m³ | Masse volumique du solide |
| `rho_f` | 1025 kg/m³ | Masse volumique du fluide |
| `mu` | 1 Pa·s | Viscosité dynamique |
| `g` | 9.81 m/s² | Accélération gravitationnelle |
| `h_num` | 0.1 s | Pas RK4 |

## Utilisation

```bash
python main.py
```

## Dépendances

- Python 3.x
- `matplotlib`
