//Выполнил Петров Роман
// Ссылка на работу в kodaror.ru https://kodaktor.ru/task_func_b7fc6
function rgb(r = 255, g = 255, b = 255) {
     return `rgb(${r},${g},${b})`;
  }
   document.querySelector('button')
   .addEventListener(
     'click',
      e => {
        const result = rgb(100,200,200);
        e.target.textContent = result;
		document.body.style.backgroundColor = result;
      }
   );
