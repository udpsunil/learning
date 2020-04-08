# Cource Overview

## Overview
Refer to https://golang.org/ref/spec#Packages

Package on the FileSystem

* All Go source files in a single directory
    * Subdirectory are excluded
* In a Go source file
    * Package declaration
    * Documentation
    * Imports
    * Var & Const blocks
    * Types and Interfaces
    * Functions
* Types of Packages
    * library package 
        - to be consumed by other packages
        - name must match the directory name
        - should provide a focused set of related features
    * main package
        - application entry point
        - contain a main function
        - can be in any directory
        - focus on application setup and initialization

## Working with package
* Naming packages
    * short and clear
    * lower case
    * no underscores
    * prefer nouns
    * abbreviate judiciously
    * don't steal good names from user

## Preparing packages to use
* Member visibility
    * Public Scope
        * Capitalize member
        * Available to all consumers
    * Package Scope
        * Lowercase member
        * Only available within package
        * No private scope only package Scope
    * Internal Package
        * Can use public and package level members
        * Scoped to parent package and its descendants
* Documenting a package
    * Package
        * Licensing
        * Package comment - start with Package <package name> and first sentence.
        * package declaration (package bufio)     
        * doc.go file to include detailed documentation   
    * Components
        * Use complete statements
        * Start first sentence with element name
        * Write first sentence as a short description of the element.
* Designing a Package
    * provide clear solution
        - single responsibility
        - cohesive api 
    * focus on the consumer
        - simple to use
        - minimize api
        - encapsulate changes
    * maximize reusability
        - reduce the number of dependencies
        - minimize the scope
* Interface strategies
    * concrete types
        - configuration
    * interfaces
        - behaviour
    * returns
        - return configuration and behaviour
        - avoid panics return errors
## Using other packages
* Alternative import methods
    * aliases - when package name is same
        - lmjson "pluralsight.com/libmanager/json"
    * import for side effect
        - _ "github.com/lib/pq" - calls init functions
    * internal packages
        - provides another scoping mechanism
        - accessible by parent and its children
        - enables better organization without leaking details
        - create a package name called 'internal'
    * relative imports
        - import package relative to current one
        - not valid in workspace or modules
        - probably will never need this