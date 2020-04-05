package main

import "fmt"

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
}
