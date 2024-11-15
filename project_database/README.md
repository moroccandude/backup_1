# 📊 Projet de Base de Données pour Annonces Immobilières 🏠

Ce projet consiste à créer une base de données relationnelle pour organiser des informations sur les annonces immobilières, en utilisant PostgreSQL, Docker et SQLAlchemy.

---

## 🎯 Objectifs du Projet

1. **Modélisation des données** 🗂️ : Identifier les entités principales et leurs relations.
2. **Configuration Docker** 🐳 : Déployer PostgreSQL dans un conteneur Docker.
3. **Modèles SQLAlchemy** 🛠️ : Modéliser les données en Python avec SQLAlchemy.
4. **Requêtes SQL** 🔍 : Interroger la base pour extraire des informations pertinentes.
5. **Documentation et reproductibilité** 📄 : Fournir des livrables professionnels et réutilisables.

---

## 🚀 Fonctionnalités

### 📂 Modélisation de la Base de Données
- **Entités** :
  - **Annonce** : titre, prix, date, pièces, surface, etc.
  - **Ville** : nom des villes uniques.
  - **Équipement** : équipements liés aux annonces (*Ascenseur*, *Balcon*).
- **Relations** :
  - *Plusieurs-à-un* entre **Annonce** et **Ville**.
  - *Plusieurs-à-plusieurs* entre **Annonce** et **Équipement** via une table associative.

### 🐳 Configuration PostgreSQL avec Docker
- Utilisation d’un conteneur Docker pour PostgreSQL.
- Définition des tables et initialisation avec SQLAlchemy.

### 🛠️ Modélisation SQLAlchemy
- Modèles Python définis avec SQLAlchemy pour :
  - **Annonce**
  - **Ville**
  - **Équipement**
  - **AnnonceÉquipement** (table intermédiaire).

### 🔍 Exemples de Requêtes SQL
- **Filtrer par ville** : Obtenir toutes les annonces pour une ville donnée.
- **Recherche avancée** :
  - Annonces par nombre de pièces/salles de bain.
  - Annonces dans une plage de prix.
  - Annonces avec équipements spécifiques.
- **Statistiques** :
  - Compter le nombre d'annonces par ville.
  - Rechercher des annonces par date ou par surface.

---

## 🛠️ Installation et Configuration

### 📦 Prérequis
- **Docker** et **Docker Compose** 🐳
- **Python 3.8+** 🐍
- **SQLAlchemy**

### 📥 Étapes

1. **Clonez le dépôt** 📂 :
   ```bash
   git clone https://github.com/votre-repo/projet-immobilier.git
   cd projet-immobilier
