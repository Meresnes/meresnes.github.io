//Выполнил Петров Роман
function geron(a,b,c) {
    p = 0.5 * (a + b + c);
    res = Math.sqrt(p * (p - a) * (p - b) * (p - c));
    return res;
}
const f = geron(3,4,5);
console.log(f);