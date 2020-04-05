package main

import (
	"fmt"

	"github.com/udpsunil/learning/go/go-application/models"
)

func main() {
	u := models.User{
		ID:        0,
		FirstName: "Sunil",
		LastName:  "Udupi",
	}
	fmt.Println(u)
}
