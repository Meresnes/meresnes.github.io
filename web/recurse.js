/*
const concat = (...args) => [...args].reduce((r, g, b) => `${r}${g}${b}`);
module.exports = concat;

 console.log(concat(2,6,7)); */

 /*const f = x => x === 1 ? 1 : x * f(x - 1);
 console.log(f(160));
const sum = (x,y) => x + y;
console.log(sum(3,5));

function sumImperative(x,y){
  let s = x;
  for(let i = 0 ; i < y;i++){
    ++s;
  }
  return s;
}

console.assert(sumImperative(4,8) === 12);

let i = -1;
function sumImperative(x,y){
  let s = x;
  inc(i);
  if(i<=y){
    sumImperative(x+1;y);
  }
  return s;

}
console.log(sumImperative(4,8));

const inc = x => x+1;
const f = (x,y) => y === 0 ? x : inc(f(x,y-1));
console.log(f(4,9));
console.log(21);
*/

const sec = a => 1 + a;
const add = (a, b) => (b === 0) ? a : sec(add(a, b - 1));
const mpy = (a, b) => (b === 1) ? a : add(a, mpy(a, b - 1));
const pwr = (a, b) => (b === 1) ? a : mpy(a,pwr(a,b-1));

console.log(pwr(2, 10)); 
