# Une application mobile pour smartphone pour Python 1/2

## le framework kivy

1. installation dans un environnement virtuel

python -m venv .venv

.venv/Scripts/activate

2. installation du package kivy

python -m pip install kivy

3. **hello_kivy.py** affiche un text dans une widget Label

4. **affiche_aldrin.py** affiche une image dans une widget Image

5. **mise_en_page.py** test les mises en pages
    - BoxLayout : arrange les enfants horizontalement (par defaut) ou verticalement
    - FloatLayout
    - GridLayout

#### le padding

- c'est l'espace entre le parent et l'enfant en pixel
- un argument simple : **padding=10**
- une liste de 2 arguments: **[padding_horizontal, padding_vertical]**
- une liste de 4 arguments: **[padding_left, padding_top, padding_right, padding_bottom]**

#### le spacing

- c'est lespace entre les widgets enfants

#### l'orientation

- par defaut le BoxLayout est horizontal
- 

