package models

//User struct to hold user information
type User struct {
	ID        int
	FirstName string
	LastName  string
}

var (
	users  []*User
	nextID = 1
)

//GetUsers return users
func GetUsers() []*User {
	return users
}

//AddUser returns user added with ID and error value
func AddUser(u User) (User, error) {
	u.ID = nextID
	nextID++
	users = append(users, &u)
	return u, nil
}
