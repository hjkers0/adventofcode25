const fs = require('node:fs')
const path = require('node:path')
const text = fs.readFileSync(path.resolve('input.txt'), 'utf8')

const rangeIds = text.split(',')

const rangeIdsClear = rangeIds.map(ids => ids.split('-'))

let sum = 0

const hasRepeated = (str) => {
  let left = str[0]
  let right = str.substr(1)
  let appnd = ''
  for (c of right) { 
    if (c == left && appnd.length + 1 == right.length)
      break
    appnd += c
    right = right.substr(1)
  }
  left += appnd
  return left == right
}

rangeIdsClear.forEach(ids => {
	const lowerId = parseInt(ids[0])
	const topId = parseInt(ids[1])
	for(let number = lowerId; number <= topId; number++) {
		if(hasRepeated(number.toString())) {
			sum += number
		}
	}
})
console.log('sum:', sum)
