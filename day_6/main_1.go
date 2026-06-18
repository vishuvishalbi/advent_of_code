/*
--- Day 6: Trash Compactor ---
After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
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

func op(a int, b int, c string) int {

	if c == "+" {
		if a == 0 {
			return b
		}
		return a + b
	} else if c == "-" {
		if a == 0 {
			return b
		}
		return a - b
	} else if c == "*" {
		if a == 0 {
			return b
		}
		return a * b
	} else if c == "/" {
		if a == 0 {
			return b
		}
		return a / b
	}
	return 0
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

	re := regexp.MustCompile(`\s+`)
	arr := re.Split(formatted_data[4], -1)
	// fmt.Println(len(arr), "Length")

	total := 0
	sum := make([]int, len(arr))
	for i := 0; i < 4; i++ {
		nums := re.Split(formatted_data[i], -1)

		for j, num := range nums {
			num, _ := strconv.Atoi(num)
			sum[j] = op(sum[j], int(num), arr[j])
		}
	}

	for _, val := range sum {
		total += val
	}

	fmt.Println(len(sum), "Length")
	fmt.Println(sum, "Sum")
	fmt.Println(total, "Total")

}
