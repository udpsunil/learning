package controllers

import "net/http"

//RegisterControllers allows user to register controllers
func RegisterControllers() {
	uc := newUserController()
	http.Handle("/users", *uc)
	http.Handle("/users/", *uc)
}
