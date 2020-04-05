package main

import (
	"net/http"

	"github.com/udpsunil/learning/go/go-application/controllers"
)

func main() {
	controllers.RegisterControllers()
	http.ListenAndServe(":3000", nil)
}
