# Convertir automatiquement
Grâce au Smart Cast, il est possible de vérifier si une variable, de type Any à l'origine, est d'un "sous-"type (Any étant une classe contenant tous les types), donc de l'utiliser dans une expression comme condition, puis de la convertir "officiellement" en ce type ensuite : 
```kotlin
val anyObject: Any
if (anyObject is String) {
	...
} else if (anyObject is List<*>) {
	...
}
```
Si `anyObject` était un String à l'origine, elle a été convertie officiellement en String.
# Convertir manuellement
Voici un exemple de conversion manuelle :
```kotlin
val anyObject: Any = "Hello Kotlin students !"
val message = anyObject as String
print(message)
```
Cette conversion n'est pas du tout sécurisée, car si l'on remplace le `String` par un `Int` l'erreur `ClassCastException` sera levée.
## Deux solutions au problème
### Try/Catch
```kotlin
val anyObject: Any = "Hello Kotlin students !"

try{
    val message = anyObject as Int
    print(message)
    
} catch(excetpion: ClassCastException) {
    print("Error !")
}
```
### null
```kotlin
val anyObject: Any = "Hello Kotlin students !"
val message: Int? = anyObject as? Int
print(message)
```