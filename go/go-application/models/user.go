package models

//User struct to hold user information
type User struct {
	ID int
	FirstName string
	LastName string
}

var (
	users []*User
	nextID = 1	
)