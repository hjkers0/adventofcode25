const fs = require('node:fs')
const path = require('node:path')
const banksFile = fs.readFileSync(path.resolve('input.txt'), 'utf8')

const banks = banksFile.split('\n')


const getHighestJoltaje = (bank) => {
  let currentBattery = bank[0]
  let max = 0
  let index = 1
  while (index < bank.length){
    let nums = bank.slice(index).split("")
    let nextMax = Math.max(...nums).toString()
    if (currentBattery + nextMax > max) {
      max = currentBattery + nextMax
    }
    currentBattery = bank[index]
    index++
  }
	return  parseInt(max);
}
let sum = 0

for (bank of banks) {
  sum += getHighestJoltaje(bank)
}

console.log('joltaje:', sum)
