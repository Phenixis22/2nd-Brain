Il existe 2 principales possibilités de liste, ayant chacune 2 sous-possibilités : `listOF` et `setOf`. La différence entre les deux est simple. `listOf` peut contenir plusieurs fois le même élément et ces éléments sont accessibles grâce à un index, tandis que `setOf` non. Chaque élément dans ces listes sont distincts les uns des autres et uniques, même ceux qui sont "égaux". 

Pour chacune de ces listes, il existe une sous-liste mutable grâce au mot-clé `mutable` accolé au nom de la list : `mutableListOf` et `mutableSetOf`.
```kotlin
// listOf
val listOfNames = listOf("Jake Wharton", "Joe Birch", "Robert Martin")
listOfNames[0] // => Jake Wharton
listOfNames[0] = "Mathieu Nebra" // => ERROR ! List is immutable

// mutableListOf
val listOfNames = mutableListOf("Jake Wharton", "Joe Birch", "Robert Martin")
listOfNames[0] // => Jake Wharton
listOfNames[0] = "Mathieu Nebra" // => SUCCESS !

// setOf
val setOfNames = setOf("Jake Wharton", "Joe Birch", "Robert Martin")
listOfNames.first() // => Jake Wharton
listOfNames.add("Mathieu Nebra") // => ERROR ! Set is immutable

// mutableSetOf
val setOfNames = mutableSetOf("Jake Wharton", "Joe Birch", "Robert Martin")
listOfNames.first() // => Jake Wharton
listOfNames.add("Mathieu Nebra") // => SUCCESS !
```
Il existe également `arrayOf`pour créer un tableau de valeurs et `mapOf` pour créer un dictionnaire.