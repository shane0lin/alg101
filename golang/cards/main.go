package main

import (
	"fmt"
)

func main() {
	// var n int
	// fmt.Scan(&n)
	//var card string = "Ace of Spades"
	card := newCard()
	cards := []string{"Ace of Diamonds", newCard()}
	cards = append(cards, "King of Heart")
	fmt.Println(card)
	fmt.Println(cards)

	for i, card := range cards {
		fmt.Println(i, card)
	}
}

func newCard() string {
	return "Three of Diamonds"
}
