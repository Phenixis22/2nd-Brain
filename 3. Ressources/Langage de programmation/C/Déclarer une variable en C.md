10 #décembre-2022 #2022-W49
Chaque variable doit avoir un nom et un type. Pour le nom, il existe quelques contraintes :
- uniquement des minuscules, majuscules et chiffres
- le premier caractère doit être une lettre
- les espaces sont interdis mais le ``_`` est autorisé
- les accents et les symboles sont interdits

Il existe plusieurs paradigme d'écriture de nom de fonction, j'utilise celui qui consiste à donner la première lettre en minuscule, puis faire commencer chaque mot suivant par une majuscule. Voici comment initialiser une variable :

```C
typeDeLaVariable nomDeLaVariable;
```
Malheureusement, votre variabe n'a pas de valeur. Voici comment lui en affecter une :
```c
nomDeLaVariable = valeurDeLaVariable;
//ou
type var = val; //initialisaton d'une variable + affectation d'une valeur
```
Pour comprendre quels sont les types possibles, je vous renvoie à ce tableau : [[Les types en C]]

Il est aussi possible de donner une valeur à une variable et de faire en sorte qu'elle garde cette valeur durant tout le programme : c'est une constante. Je vous conseille de nommer vos constantes de manière à les reconnaitre, en majuscule par exemple :
```c
const type VAR = val; //cela crée une constante
/*Faites attention ! 
Une constante doit être initialisé à sa création, sinon ce sera trop tard, sa valeur ne pourra plus être modifiée.
*/
```