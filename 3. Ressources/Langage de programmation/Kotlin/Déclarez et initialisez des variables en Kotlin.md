
```kotlin
val question = ...
val question: type = ...
var question: type = ...
```
``val`` permet de créer une variable immuable (toujours vers la même référence mémoire) tandis que ``var`` permet de créer une variable muable (vers une référence mémoire qui pourra être remplacée). ``val`` a privilégié et type de variable aussi (+ de performance)
# Quelques infos pratiques
## Déclaration // initialisation
Une variable, même déclarée avec ``val``, peut être initialisé après avoir été déclarée :
```kotlin
val message: String 

if (isUserHappy()){
    message = "Glad you're so happy ! :D"
} else {
    message = "What's going on ? :("
}
```
## la compléxité de ``null``
Permettre à ``null`` d'exister n'est pas ce que nous souhaitons.
Les variables ne peuvent recevoir la valeur "null", sauf si on indique que c'est possible avec un ? après le type de variable.
```kotlin
var message : String? = "My message can be null !"
print(message.toUpperCase())
```
Mais, sachant que la variable peut être nulle, une erreur peut être levée si vous essayez d'appeler une fonction comme dans l'exemple. Voici ce qui vous est donné comme erreur:
<center><em>"Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type String?"</em></center>
Ainsi, voici ce que vous pouvez faire : 
```kotlin
var message: String? = "My message can be null !"
if (message != null) message.toUpperCase()
```
## Déclarer une constante
```kotlin
const var/val NOMDELAVARIABLE: type = ...
```
Avec le mot clé ``const`` avant le mot-clé ``val``.

## Problème *résolu* de déclaration de variable mutable
```kotlin
var maVariable:type

//...

maVariable = ...
```
Kotlin refusera de compiler. Vous devez initialiser votre variable muable à sa déclaration... sauf si vous utilisez le mot-clé ``lateinit`` avant 
Ce problème n'est plus en 1.7.2 sur le site [kotlin](https://play.kotlinlang.org)
## Visibilité par défaut
La visibilité par défaut de n'importe quel élément de votre code est public. Il est pourtant possible de lui assigner une autre visibilité en ajoutant le mot-clé correspondant avant le ``var`` ou ``val``. ^[ voir [[Les visibilités en Kotlin]]]