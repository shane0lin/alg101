package main

import "testing"
import "os"

func TestNewDeck(t *testing.T) {
	d := newDeck()

	if len(d) != 16 {
		t.Errorf("Expected deck length of 16, but got %v", len(d))
	}

	if d[0] != "Ace of Spades" {
		t.Errorf("Expected first card to be Ace of Spades, but got %v", d[0])
	}
	if d[len(d)-1] != "Four of Clubs" {
		t.Errorf("Expected last card to be Four of Clubs, but got %v", d[len(d)-1])
	}
}

func TestSaveToDeckAndNewDeckFromFile(t *testing.T) {
	// Create a temporary file for testing
	tmpFile := "_decktesting"
	// Clean up the temporary file after the test
	defer os.Remove(tmpFile)
	// Create a new deck and save it to the temporary file

	d := newDeck()
	d.saveToFile(tmpFile)
	// Read the deck back from the temporary file
	loadedDeck := newDeckFromFile(tmpFile)

	if len(loadedDeck) != 16 {
		t.Errorf("Expected deck length of 16, but got %v", len(loadedDeck))
	}
	if loadedDeck[0] != "Ace of Spades" {
		t.Errorf("Expected first card to be Ace of Spades, but got %v", loadedDeck[0])
	}
	if loadedDeck[len(loadedDeck)-1] != "Four of Clubs" {
		t.Errorf("Expected last card to be Four of Clubs, but got %v", loadedDeck[len(loadedDeck)-1])
	}
}
