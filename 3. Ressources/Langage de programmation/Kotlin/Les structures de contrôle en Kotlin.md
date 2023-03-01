# If
La condition ``if``, étant une expression, renvoie une valeur. Ainsi, on peut retrouver une forme comme celle ci :
```kotlin
val result = if (a > b) {
	a++
	a
} else {
	b++
	b
}
```
La variable result prend la valeur la plus grande entre `a` et `b` à qui on a ajouté 1. 
Sachez que la dernière expresion du bloc est la valeur retournée.
# Switch
Le switch prend une toute autre forme an kotlin :
```kotlin
when (...) {
	val1 -> expr1
	val2 -> expr2
	val3, val4, val5 -> expr3
	else -> exprElse
}
```
Cette structure est aussi une expression, elle renverra donc une valeur.

La structure de contrôle `when` est très utilisée pour manipuler des intervalles de nombres.
# Énumération
Pour rendre notre code plus lisible, vous pouvez créer des énumérations afin de créer des types personnalisés.
```kotlin
enum class nomDelEnum(val arg1, val arg2) {
	TYPE1(qqch1)
	TYPE2(qqch2)
	...
}
```
Cette structure s'associe très bien avec when : 
```kotlin
val var1: nomDelEnum = nomDelEnum.TYPE1

when (var1) {
	nomDelEnum.TYPE1 -> expr1
	nomDelEnum.TYPE2 -> expr2
	...
}
```

