package main

import (
	"fmt"
	"time"
)

/*
  Restrictions may be placed on how the channel can be used by a function.
  c chan<- int implies that an int may be written to (but not read) from a channel
  c <-chan int implies that an int can only be read from a channel.
  channels are bi-directional by default.

  Channel read and write operations are blocking.

*/
func producer(c chan<- int, n int) {
	for i := 0; i < n; i++ {
		fmt.Println("producing", i+2)
		c <- i + 2
	}
}

func consumer(c <-chan int) {
	/*
		Select is like the switch statement for channels.
		cases in select are activated when there are messages available on different channels.
		This can also be used for a timeout by using time.After() function that creates a channel after a specified time.
	*/
	for {
		select {
		case x := <-c:
			fmt.Println("Consuming --", x)
		case <-time.After(time.Second * 2):
			fmt.Println("Shutting down consumer")
			return
		}
	}
}

func main() {

	/*
	 Channels are used as a communication medium.
	 Similar to ros topics.

	 3 is the buffer size of a channel. Buffered channels do not require the sender to wait.
	 To create an unbuffered channel
	 make (chan int) statenent it used.

	 If there are no go routines accessing a channel and the channel is full, then it leads to a deadlock.

	 a go-routine writing into a channel is not blocked until n+1 writes.
	 a go-routine reading from a channel is not blocked until the channel is empty.
	*/
	var ch chan int = make(chan int, 2)
	/*the go token is used to execute a function as a go-routine.
	  Go routine executes asynchronously.

	  In this program there are 3 go-routines
	  producer, consumer and main
	*/
	go producer(ch, 10)
	go consumer(ch)
	fmt.Println("Concurrency....")
	/*
	  without the Scanln call the program terminates without waiting for
	  the program to complete.
	*/
	var input string
	fmt.Scanln(&input)
	close(ch) // close channel.
}
