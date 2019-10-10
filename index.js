/*
const concat = (...args) => [...args].reduce((r, g, b) => `${r}${g}${b}`);
module.exports = concat;

 console.log(concat(2,6,7)); */

 const f = x => x === 1 ? 1 : x * f(x - 1);
 console.log(f(3));
