```kotlin
class nomDeLaClasse(arg1, arg2, arg3)
```
Les assesseurs et les mutateurs seront créés automatiquement par Kotlin selon le mot-cllé que vous utiliserez, ``val`` ou ``var``
Il est aussi possible de donner à un argument une valeur muable ou immuable en utilisant ces même mots clés:
```kotlin
class nomDeLaClasse(val arg1, var arg2, ...)
```
## Améliorer la class
Pour personnaliser l'assesseur ou le mutateur, voici ce qui est possible de faire :
```kotlin
class nom(arg1, val arg2){
	var arg1: String = arg1
		get() {
			...
			return field
		}
		set(value) {
			...
			field = value
		}
}
```
Voici les étapes de codage :
- on enlève le ``var``/``val`` avant le paramètre de la fonction
- on le déclare et l'initialise
- la fonction get est l'assesseur de l'argument et la fonction set est son mutateur, sachant cela vous pouvez rajouter des lignes de code à la place des ``...`` pour afficher quelque chose, rajouter quelque chose au champ(``field``), etc...