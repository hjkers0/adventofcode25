const fs = require('node:fs')
const path = require('node:path')

const text = fs.readFileSync(path.resolve('input.txt'), 'utf8')


let currentPosition = 50;
let password = 0

const instructions = text.split('\n')

instructions.forEach(inst => {
	const dir = inst[0]
	const mov = parseInt(inst.slice(1))
	const proxPosition = dir == 'L' ? currentPosition - mov : currentPosition + mov
	
	currentPosition = proxPosition % 100

	if (currentPosition < 0) 
		currentPosition + 100
	
	if (currentPosition == 0)
		password += 1
})

console.log('password:', password)
