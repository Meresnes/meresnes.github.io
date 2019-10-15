
const [a1, b1, c1, a2, b2, c2] = [1, 3, 2, 9, 2, 7];
let detA, detA1, detA2, x, y;
  		
detA = a1*b2 - a2*b1;
detA1 = c1*b2 - c2*b1;
detA2 = -c1*a2 + c2*a1;
x = detA1/detA;
y = detA2/detA;

console.log('Ответ: ' );
console.log("x = " + x);
console.log("y = " + y);
