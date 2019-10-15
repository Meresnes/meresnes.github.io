const concat = (...args) => [...args].reduce((x, y, z) => `${x}${y}${z}`);
module.exports = concat;

console.log(concat(2,6,7)); 
