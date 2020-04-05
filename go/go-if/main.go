package main

// User structur
type User struct {
	ID        int
	FirstName string
	LastName  string
}

func main() {
	u1 := User{
		ID:        1,
		FirstName: "Sunil",
		LastName:  "Udupi",
	}
	u2 := User{
		ID:        2,
		FirstName: "Aparna",
		LastName:  "Udupi",
	}
	if u1.ID != u2.ID {
		println("Not same users!")
	} else if u1.FirstName == u2.FirstName {
		println("Similar users.")
	} else {
		println("Same users!")
	}
}
