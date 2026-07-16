package main

import "fmt"

type deck []string

func newDeck() deck {
	cards := deck{}

	cardSuits := []string{"Spade", "Diamonds", "Hearts", "C"}
	cardValues := []string{"Ace", "Two", "Three", "Four"}
	for _, suit := range cardSuits {
		for _, value := range cardValues {
			cards = append(cards, value+" of "+suit)
		}
	}
	return cards
}

func (d deck) print() {
	for i, card := range d {
		fmt.Println(i, card)
	}
}

func newCard() string {
	return "Three of Diamonds"
}

func deal(d deck, handSize int) (deck, deck) {
	return d[:handSize], d[handSize:]
}
