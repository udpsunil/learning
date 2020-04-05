// builtin collections
/*
Array - fixed size collection of similar datatypes
Slices,
Maps,
Structs,
*/

package main

import "fmt"

func main() {
	// Arrays - long form
	var arr [3]int
	arr[0] = 1
	arr[1] = 2
	arr[2] = 3

	fmt.Println(arr)
	// fmt.Println(arr[1])

	// Arrays short form
	arry := [3]int{1, 2, 3}
	fmt.Println(arry)

	// Slices using array
	arr1 := [3]int{1, 2, 3}
	slice := arr1[:1]
	fmt.Println(slice)

	slice1 := []int{1, 2, 3}
	fmt.Println(slice1)

	slice1 = append(slice1, 4)
	fmt.Println(slice1)

	//maps - key, value pair
	m := map[string]int{"sunil": 1}
	fmt.Println(m)
	fmt.Println(m["sunil"])

	delete(m, "sunil")
	fmt.Println(m)

	//structs - different data types
	type user struct {
		ID        int
		FirstName string
		LastName  string
	}
	var you user
	fmt.Println(you)
	you.ID = 0
	you.FirstName = "Sunil"
	you.LastName = "Udupi"
	fmt.Println(you)

	youtoo := user{1, "Aditi", "Udupi"}
	fmt.Println(youtoo)

	youthree := user{ID: 2, FirstName: "Aparna", LastName: "BM"}
	fmt.Println(youthree)

	// var u user = user{4,"",""}
	// fmt.Println(u)
}
