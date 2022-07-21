# Design patterns with Python

Most popular design patterns, its short descriptions and examples.

## Creational

They are used to implement more elastic mechanisms of creating objects, and they allow multiple use of a code:
* abstract factory - to create a family of classes and objects,
* builder - to separate creating objects from its representation,
* factory method - allows creating families of related objects without defining its classes,
* prototype - allows copying existing objects without creating relations between code and objects' classes,
* singleton - to ensure that there is only one object of a class. In this repo there was implemented thread-safe singleton.

## Structural

They explain how to compose classes and objects into the bigger structures, without losing flexibility and efficiency:
* adapter - to adapt the interface to the customer's needs,
* decorator - to add a new functionality to an object,
* facade - to provide a simplified API of our system to a client.

## Behavioral

To ensure effective communication and separation of duties between objects:
* command - to turn a command into an object with all information about the command, 
* iterator - allows scrolling subsequent elements of different collections in similar way, through only one interface,
* observer - to define a subscription mechanism to notify some objects about incidents connected to observed object,
* state - allows changing an object's  behaviour, depending on its internal state,
* strategy - encapsulates a family of algorithms and selects one from the pool for use during runtime,
* template method - defines core of an algorithm in a parent class, but it is possible to overwrite some stages of this 
algorithm, without knowing its structure.