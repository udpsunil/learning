package main

func main() {
	// for loop with condition
	var i int
	for i < 5 {
		i++
		if i == 3 {
			continue
		}
		//println(i)
	}

	// for loop with post clause
	for i := 0; i < 5; i++ {
		println(i)
	}

	// infinite loops
	i = 0
	for {
		if i == 5 {
			break
		}
		i++
		println(i)
	}

	// looping through collections
	slice := []int{1, 2, 3, 4, 5}
	for i, v := range slice {
		println(i, v)
	}

	wellKnownPorts := map[string]int{"http": 80, "https": 443}
	for k, v := range wellKnownPorts {
		println(k, v)
	}
}
