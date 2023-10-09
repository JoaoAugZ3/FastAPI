/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let call = []
    let add = call.length
    return function() {
        call.push(n + add)
        add++
        return call[add-1]
    };
};

const counter = createCounter(10)
counter()
counter()
counter()

