Une fonction peut renvoyé une Exception facilement :
```kotlin
private fun substractNumber(a: Int, b: Int) = if (a>=b) a-b else throw Exception("a is smaller than b !")
```
Grâce à cela, il est possible de créer une fonction pouvant renvoyer une Exception sans avoir à la vérifiée à chaque fois avec try/catch même si cela reste possible.
## Opérateur Elvis
`Throw` étant une expression, il est possible de l'utiliser pour récupérer l'Exception dans une valeur :
```kotlin
class User(val email: String?, val password: String?)
val user = User("toto@gmail.com", "azerty")
val password = user.password ?: throw IllegalArgumentException("Password required")
```
ou encore : 
```kotlin
private fun fail(message: String): Nothing = throw IllegalStateException(message)
```