/*
--- Day 4: Printing Department ---
You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
*/
package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func hasLessThanFour(arr [][]string, i int, j int) bool {

	count := 0
	for k := -1; k <= 1; k++ {
		for l := -1; l <= 1; l++ {
			if k == 0 && l == 0 {
				continue
			}
			if i+k < 0 || i+k >= len(arr) || j+l < 0 || j+l >= len(arr[i]) {
				continue
			}
			if arr[i+k][j+l] == "@" || arr[i+k][j+l] == "x" {
				count++
			}
		}
	}

	return count < 4
}

func replaceWithX(arr [][]string, c *int) [][]string {
	for i, val := range arr {
		for j, val2 := range val {
			if val2 == "@" {
				if hasLessThanFour(arr, i, j) {
					arr[i][j] = "x"
					*c = *c + 1
				}
			}
		}
	}
	return arr
}

func main() {

	_, exePath, _, ok := runtime.Caller(0)
	if !ok {
		panic("No caller information")
	}

	exeDir := filepath.Dir(exePath)

	filepath := filepath.Join(exeDir, "input.txt")

	data, err := os.ReadFile(filepath)
	if err != nil {
		panic(err)
	}

	// fmt.Println(string(data))
	formatted_data := strings.Split(string(data), "\n")

	arr := make([][]string, len(formatted_data))

	for i, val := range formatted_data {
		arr[i] = strings.Split(val, "")
	}
	count := 0
	arr = replaceWithX(arr, &count)

	fmt.Println(count)
}
