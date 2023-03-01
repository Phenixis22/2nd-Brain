# Tant que
Exactement pareil qu'en [[Java]] :
```kotlin
while (condition) {
	expr
}

// ou

do {
	expr
} while (condition)
```
Do While rentre dans la boucle une fois avant de vérifier la condition tandis que While vérifie la condition avant même de rentrer dans la boucle.
# Pour
La boucle for s'utilise sous la forme `item in element` :
```kotlin
List<Boolean> rain = listOf(true, false, true, true, false)

for (bool in rain) {
	println("Is it raining ? $bool") 
}
```
Il est aussi possible d'utiliser un index dans la boucle :
```kotlin
for (i in rain.indices) {
	println("Did it rained the $i th day ? ${rain[i]}")
}
```
Un [[Les intervalles en kotlin|intervalle]] aussi :
```kotlin
for (i in 0..4) {
	println("Did it rained the $i th day ? ${rain[i]}")
}
```
Vous pouvez aussi utiliser des mots-clé pour faire ce que vous voulez avec votre boucle `for` :
```kotlin
for (i in 10 downTo 1 step 2) {
	println("Index is : $i")
} //10, 8, 6, 4, 2
```
Le mot-clé `downTo` permet de créer un intervalle qui descend jusqu'à la valeur.
Le mot-clé `step` permet de choisir le pas de notre intervalle.