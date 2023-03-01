Source : [[Utiliser Obsidian]]
Liens :
Auteur :
Date : 20 #août-2022
***
# Les callouts
> [!un callout]
> Se fait de cette manière

Mais, grâce à Admonition, un plugin complémentaires, un callout peut également se faire de cette manière
```ad-note
Un callout
```
Ce plugin permet de personnaliser ces callouts. (Mode Édition pour tout voir).
```ad-<type> # Admonition type. See below for a list of available types.
title:                  # Admonition title.
collapse:               # Create a collapsible admonition.
icon:                   # Override the icon.
color:                  # Override the color.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.
```
Ce qui donne ça :
```ad-note
title:Test
collapse:open
icon:map
color:116 0 255
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.

```
Pour ce code :

	```ad-note
	title:Test
	collapse:open
	icon:map
	color:116 0 255
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.```
![[Les différents types de callouts]]