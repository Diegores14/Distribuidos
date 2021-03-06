package main

import (
	"bufio"
	"fmt"
	"math"
	"net"
	"strconv"
	"strings"
)

func eval(message string) string {

	values := strings.Split(message, " ") 	
	if len(values) != 3 {
		return "is not a valid operation"
	}
	a, err1 := strconv.Atoi(values[0])
	b, err2 := strconv.Atoi(values[1])
	if err1 != nil || err2 != nil {
		return "is not a valid operation"
	}	
	values[2] = values[2][:1]
	fmt.Print(values[2]+ "hello")
	switch {
	case values[2] == "+":
		return strconv.Itoa(a + b)
	case values[2] == "-":
		return strconv.Itoa(a - b)
	case values[2] == "*":
		return strconv.Itoa(a * b)
	case values[2] == "/":
		return strconv.Itoa(a / b)
	case values[2] == "^":
		return strconv.FormatFloat(math.Pow(float64(a), float64(b)), 'f', 6, 64)
	case values[2] == "sqrt":
		return strconv.FormatFloat(math.Pow(float64(a), 1.0/float64(b)), 'f', 6, 64)
	}
	fmt.Print("hello1\n")
	return "Not a valid operation"
}

func main() {
	fmt.Println("Launching server...")

	ln, _ := net.Listen("tcp", ":8083")
	conn, _ := ln.Accept()

	for {
		message, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			break
		}
		fmt.Print("Message Received: ", string(message))
		newmessage := strings.ToUpper("The operation result is: " + eval(message))
		conn.Write([]byte(newmessage + "\n"))
	}
	conn.Close()
}