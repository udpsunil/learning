package main

import "fmt"

func main() {
	fmt.Println("Hello, Go playground")
	port := 3000
	startWebServer(port, 2)
}

func startWebServer(port int, numOfRetries int) {
	fmt.Println("Starting webserver...")
	//do important things
	fmt.Println("Server started on port", port)
	fmt.Println("Number of retries", numOfRetries)
}
