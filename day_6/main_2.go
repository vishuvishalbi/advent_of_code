/*
--- Part Two ---
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
*/

package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"runtime"
	"strconv"
	"strings"
)

func op(c string, num1 string, num2 string, num3 string, num4 string) int {

	length := len(num1)
	total := 0

	for startIndex := length - 1; startIndex >= 0; startIndex-- {

		num := fmt.Sprintf("%c%c%c%c", num1[startIndex], num2[startIndex], num3[startIndex], num4[startIndex])
		num = strings.TrimSpace(num)
		x, _ := strconv.Atoi(num)
		// fmt.Println(num, "num", x, "x")
		if c == "+" {
			total += x
		} else if c == "*" {
			if total == 0 {
				total = x
			} else {
				total *= x
			}
		}
		fmt.Println("c", c, "num", x)
	}
	fmt.Println(total, "total")
	return total
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
	// fmt.Println(len(formatted_data), "Length")

	re := regexp.MustCompile(`(\S)(\s*)`)
	matches := re.FindAllStringSubmatch(formatted_data[4], -1)
	startIndex := 0
	total := 0
	for _, val := range matches {
		char := val[1]
		spaceCount := len(val[2])
		// fmt.Println(char, spaceCount, "index", i)
		// fmt.Println(formatted_data[3][startIndex:startIndex+spaceCount], "count", spaceCount, "index", i, char)

		num1 := formatted_data[0][startIndex : startIndex+spaceCount+1]
		num2 := formatted_data[1][startIndex : startIndex+spaceCount+1]
		num3 := formatted_data[2][startIndex : startIndex+spaceCount+1]
		num4 := formatted_data[3][startIndex : startIndex+spaceCount+1]
		startIndex += spaceCount + 1
		total += op(char, num1, num2, num3, num4)
		// fmt.Println(num1, num2, num3, num4, "num1", "num2", "num3", "num4", char)
	}

	fmt.Println(total, "Total")

}
