// Go version
package main

import "fmt"

func main() {
    fruits := []string{"apple", "banana", "pear"}
    for _, fruit := range fruits {
        fmt.Println("I like", fruit)
    }
}
