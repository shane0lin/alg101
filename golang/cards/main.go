package main
import (
	"fmt"
)
func main() {
	// var n int
	// fmt.Scan(&n)
	//var card string = "Ace of Spades"
	card := newCard()
	fmt.Println(card)
}

func newCard() string {
	return "Three of Diamonds"
}