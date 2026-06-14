/*
--- Part Two ---
Now, the Elves just need help accessing as much of the paper as they can.

Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

Initial state:
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

Remove 13 rolls of paper:
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

Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?
*/
package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func hasLessThanFour(arr [][]string, i int, j int, mandatory string) bool {

	count := 0
	for k := -1; k <= 1; k++ {
		for l := -1; l <= 1; l++ {
			if k == 0 && l == 0 {
				continue
			}
			if i+k < 0 || i+k >= len(arr) || j+l < 0 || j+l >= len(arr[i]) {
				continue
			}
			if arr[i+k][j+l] == "@" || arr[i+k][j+l] == mandatory {
				count++
			}
		}
	}

	return count < 4
}

func replaceWithX(arr [][]string, c *int, mandatory string) [][]string {
	for i, val := range arr {
		for j, val2 := range val {
			if val2 == "@" {
				if hasLessThanFour(arr, i, j, mandatory) {
					arr[i][j] = mandatory
					*c = *c + 1
				}
			}
		}
	}
	return arr
}

func incrementString(s string) string {
	runes := []rune(s)
	carry := true

	// Step from right to left (least significant to most significant)
	for i := len(runes) - 1; i >= 0; i-- {
		if !carry {
			break
		}

		if runes[i] == 'Z' {
			runes[i] = 'A' // Reset current position and preserve the carry
		} else {
			runes[i]++    // Safely increment current letter
			carry = false // Carry has been resolved
		}
	}

	// If the carry remains unresolved, prepend a new starting character
	if carry {
		runes = append([]rune{'A'}, runes...)
	}

	return string(runes)
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
	canReplace := true
	total := 0
	mandatory := "a"
	for canReplace = true; canReplace; {
		count := 0
		arr = replaceWithX(arr, &count, mandatory)
		total += count
		canReplace = count > 0
		mandatory = incrementString(mandatory)
	}

	fmt.Println(total)
}
