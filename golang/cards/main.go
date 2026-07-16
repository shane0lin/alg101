package main

import (
	"fmt"
)

func main() {
	// var n int
	// fmt.Scan(&n)
	//var card string = "Ace of Spades"
	// card := newCard()
	// cards := deck{"Ace of Diamonds", newCard()}
	// cards = append(cards, "King of Heart")
	// fmt.Println(card)
	// cards := newDeck()
	// fmt.Println(cards)
	// fmt.Println()

	// for i, card := range cards {
	// 	fmt.Println(i, card)
	// }
	// cards[0:2].print()
	// hands, remainingCards := deal(cards, 5)
	// hands.print()
	// fmt.Println()
	// remainingCards.print()

	cards := newDeck()
	fmt.Println(cards.toString())

	cards.saveToFile("./test.tmp")

	d := newDeckFromFile("./test.tmp")
	d.print()

}
