const numberList = Array.from({ length: 1234567 }, (_, i) => i + 1);
const randomNumber = numberList[Math.floor(Math.random() * numberList.length)];

console.log(`Random number: ${randomNumber}/${numberList.length}`);

const simpleSearch = (numberList, target) => {
    return numberList.find(number => number === target);
}


const binarySearch = (numberList, target) => {
    let min = 0
    let max = numberList.length - 1    

    while (min <= max) {
        let average = Math.floor(((min + max) / 2))

        if (target === numberList[average]) return numberList[average]
        if (numberList[average] < target) min = average + 1
        if (numberList[average] > target) max = average - 1
    }
}

console.time('Normal')
console.log('Resultado: ', simpleSearch(numberList, randomNumber))
console.timeEnd('Normal')

console.time('Binary Search')
console.log('Resultado: ', binarySearch(numberList, randomNumber))
console.timeEnd('Binary Search')