B# Base de données
| MCD                     | Modèle relationnel |
| ----------------------- | ------------------ |
| Entités et associations | Relations          |
| identifiants            | Clés primaires     |

Entités "Pays" avec nom_pays, population, superficie
\donne/
**Pays**(nom_pays TEXT, population INTEGER, superficie INTEGER)
## Relation
### À unicité :
**Pays**(==PK nom_pays TEXT==, population INTEGER, superficie INTEGER)
**Auteur**(id_auteur TEXT, ==FK nom_pays TEXT==, nom TEXT, prénom TEXT, date_naissance DATE)
Car 1 pays par auteur

### Non unique
**LIVRE**(==PK num_isbn==, titre TEXT, année DATE)
**Écrire**(==PK FK id_auteur TEXT==, ==PK FK num_isbn INTEGER==, nb_chapitres INTEGER)
**Auteur**(==PK id_auteur TEXT==, FK nom_pays TEXT, nom TEXT, prénom TEXT, date_naissance DATE)

### Au final
**Pays**(PK nom_pays TEXT, population INTEGER, superficie INTEGER)
**Livre**(PK num_isbn, titre TEXT, année DATE)
**Écrire**(PK FK id_auteur TEXT, PK FK num_isbn INTEGER, nb_chapitres INTEGER)
**Auteur**(PK id_auteur TEXT, FKnom_pays TEXT, nom TEXT, prénom TEXT, date_naissance DATE)

## Contraintes
Contrainte de domaine : TEXT, ...
Contrainte d'entité : clés primaires
Contrainte de référence : clés étrangères
Contraintes utilisateurs : contraintes sur les valeurs des tables
Ces contraintes garantissent l'intégrité et la cohérence logique:
- À tout instant
- dans le cas d'une mise à jour des données
Valeur nulle= très dérangeante
Car si recherche d'une condition, la valeur logique (true, false) n'existe pas
# Niveau physique - SQL
LMD = langage de manipulation de données
SQLite pour NSI
-> logiciel qui permet de modifier la BDD en local

***

SQL = structured query langage
1974 et dernière version en 2011
SQL est ensemble de langages

Requête générale SQL :
Commencer par SELECT
Suivi d'un FROM pour regarder dans une table
JOIN = lien entre deux relations
WHERE = recherche dans quelque chose
En SQL, relation = table et les éléments de ces table = tuples
Mot SQL en maj, commence par une majuscule = table, nom colonne en minuscule
Espaces et tabulations = esthétique
Fin requête = point virgule

## Création BDD
CREATE DATABASE Nombdd; *créer une base de données*
USE Nombdd;
*Rarement utilisé pour le bac*
DROP DATABASE Nombdd; *supprimer le base de données*
DROP TABLE IF EXISTS Nombdd;
CREATE TABLE Nombdd; *recréer le table de 0*

*Création des colonnes :*
> colonne TYPE
> colonne TYPE
> UNIQUE (*contrainte d'unicité*)
> PRIMARY KEY (colonne)
> FOREIGN KEY (colonne) REFERENCES Nombdd (colonne)
> CHECK (*contrainte utilisateur*)

Autres mot clés:
ON DELETE CASCADE = supprimer automatiquement dans la table (supprimer la France = supprimer **tous** les auteurs français)
ON UPDATE CASCADE = changement automatique dans la table (si France devient République Démocratique Française, alors tous les auteurs français deviennent des auteurs Démocratiques français)

Insérer :
> INSERT INTO Nombdd VALUES (..., ..., ..., ...)