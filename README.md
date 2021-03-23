# Little-Search-Engine
A simple search engine based on python 3.7.

The whole picture of this project:

![](https://github.com/chaihuoa/Little-Search-Engine/blob/main/LittleSearchEngine.png?raw=true)

This project aims to learn python step by step by implementing a simple search engine. From the UML diagram above, we can see that we have one base class `SearchEngineBase` and four subclasses
respectly corresponds 4 kinds of algorithms search engine.

`SimpleEngine`: brute force enumerating all of content.

`BOWEngine`: [Bag of Words Model](https://en.wikipedia.org/wiki/Bag-of-words_model) 

>In this model, a text (such as a sentence or a document) is represented as the bag (multiset) of its words, disregarding grammar and even word order but keeping multiplicity. 

`BOWInvertedIndexEngine`: [Inverted Index Model](https://en.wikipedia.org/wiki/Inverted_index)

>An inverted index is an index data structure storing a mapping from content, such as words or numbers, to its locations in a document or a set of documents. In simple words, it is a hashmap like data structure that directs you from a word to a document or a web page.
>
>[Inverted Index](https://www.geeksforgeeks.org/inverted-index/)

`BOWInvertedIndexEngineWithCache`: add cache

Inspired by [Python 核心技术与实践](http://gk.link/a/10ppl)

# TODO

- [ ] Improve `search()` function using a minimum heap to store index.
- [x] Axtract all the properties and functions of each classes and draw the inheritance relationships.