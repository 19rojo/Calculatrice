# Calculatrice

Application de calculatrice développée en **Python**, conçue pour offrir une interface simple, rapide et facile à exécuter en local.

## Fonctionnalités

- Opérations arithmétiques de base (addition, soustraction, multiplication, division)
- Gestion des erreurs courantes (division par zéro, expressions invalides)
- Interface claire et réactive

## Stack technique

- **Langage :** Python 3.12+
- **Backend / Serveur :** Flask
- **Frontend / Styles :** HTML5, Tailwind CSS

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/19rojo/Calculatrice.git](https://github.com/19rojo/Calculatrice.git)
   cd Calculatrice 
   ```

2. **Créer et activer un environnement virtuel :**
   - Sur  Windows (Powershell/ Terminal)
   ```powershell
   python3 -m venv .venv
   .venv\Scripts\activate
   ```

   - Sur  Linux/ MacOS
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```
## Utilisation

1. **Lancez l'application depuis la racine du projet :**
   ```bash
   python3 app.py
   ```

2. **Ouvrez ensuite l'adresse indiquée dans le terminal** (par exemple http://127.0.0.1:5000)

## Structure du projet

```Plaintext
Calculatrice/
├── app.py              # Lanceur de l'application Flask
├── calculatrice.py     # Classes d'opérations arithmétiques
├── requirements.txt    # Dépendances Python
├── static/             # Fichiers statiques (CSS)
├── templates/          # Templates HTML (si application web)
└── README.md           # Documentation du projet
```

## Améliorations prévues
- [ ] Améliorer l'interface utilisateur pour la rendre plus intuitive et facile à utiliser
- [ ] Ajouter l'historique des calculs récents
- [ ] Ajouter des opérations avancées (puissance, racine carrée, pourcentages)
- [ ] Ajouter la prise en charge du clavier et un thème sombre
- [ ] Ajouter des tests unitaires avec pytest

## Auteur
**Rojo Ny Aina Rakotondramanana — GitHub : @19rojo**
