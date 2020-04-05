package main

import (
	"errors"
	"fmt"
)

func main() {
	fmt.Println("Hello, Go playground")
	port := 3000
	status, err := startWebServer(port, 2)
	fmt.Println("Server is started", status, err)
}

func startWebServer(port int, numOfRetries int) (int, error) {
	fmt.Println("Starting webserver...")
	//do important things
	fmt.Println("Server started on port", port)
	fmt.Println("Number of retries", numOfRetries)
	//return nil
	return 255, errors.New("Something went wrong")

}
