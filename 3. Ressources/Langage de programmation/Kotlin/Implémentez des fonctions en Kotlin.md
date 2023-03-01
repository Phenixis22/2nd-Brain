```kotlin
fun nom(arg1, arg2, arg3, ...): typeRenvoyé {
	...
}
```
Les fonctions peuvent aussi se résumer seulement à une expression^[Voir [[La différence entre expression et instruction en Kotlin]]].
```kotlin
fun maxOf(a:Int, b:Int) = if (a>b) a else b

print(maxOf(12,16)) //affiche 16
```