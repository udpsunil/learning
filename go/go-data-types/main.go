package main

import "fmt"

//PI iota & constant expressions
const PI = 3.1415
const (
	first  = 0
	second = 1
	third  = iota
)

func main() {
	// declaration and definition
	var i int
	i = 42
	fmt.Println(i)

	// definition with declaration
	var f float32 = 3.14
	fmt.Println(f)

	firstName := "Sunil"
	fmt.Println(firstName)

	b := true
	fmt.Println(b)

	c := complex(3, 4)
	fmt.Println(c)

	r, im := real(c), imag(c)
	fmt.Println(r, im)

	// pointers, no pointer arithmetic
	var secondName *string = new(string)
	*secondName = "Udupi"
	fmt.Println(*secondName)

	ptr := &firstName
	fmt.Println(ptr, *ptr)

	firstName = "Aditi"
	fmt.Println(ptr, *ptr)

	// constants
	const pi = 3.1415 // same line - can not change. compile time constants not run time.
	fmt.Println(pi)

	const d = 3 // implicitly typed constant
	fmt.Println(d + 3)

	fmt.Println(d + 1.2)

	fmt.Println(PI)
	fmt.Println(first, second, third)

}
