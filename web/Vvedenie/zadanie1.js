//Выполнил Петров Роман

const [a1, b1, c1, a2, b2, c2] = [1, 3, 2, 9, 2, 7];
let A, A1, A2, x, y;
  		
A = a1*b2 - a2*b1;
A1 = c1*b2 - c2*b1;
A2 = -c1*a2 + c2*a1;
x = A1/A;
y = A2/A;

console.log('Ответ: ');
console.log("x = " + x);
console.log("y = " + y);
