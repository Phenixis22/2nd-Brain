10 #décembre-2022 #2022-W49
```C
typeDeLaSortie nomDeLaFonction(typeArg1 arg1, typeArg2 arg2, ...) 
{
	...
}
```

e.g : 
```C
int main()
{
    printf("Hello world!\n");
    return 0;
}
```
> Ce programme *main* renvoie un entier^[Pour le type de sortie, se référer à [[Les types en C]]] (0) et affiche dans la console "Hello world!"

L'ordre des fonctions est important. Une fonction *x* ne peut-être appelé par une autre fonction *y* avant d'être initialisée. Cela crée un problème d'organisation, c'est pour cela qu'il existe des ... et permettent de ne pas se soucier de l'ordre. Il est ainsi possible d'écrire la première ligne d'une fonction tout en haut de son fichier pour avoir accès à cette fonction n'importe quand. De cette manière :

```C
int add(int a, int b);

int main()
{
	int result = add(2, 3);
	return result;
}

int add(int a, int b)
{
	return a+b;
}
```
> Ce programme appelle la fonction *main*, qui appelle la fonction *add* même si elle est écrite après.