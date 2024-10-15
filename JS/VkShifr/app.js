const btn = document.createElement('button')
var BtnStyle = btn.style
btn.setAttribute('type', 'button');
btn.classList.add('btn');
btn.textContent = 'Изменить';
BtnStyle.border = "15px"
BtnStyle.fontSize = "16px"
BtnStyle.padding = "14px 40px"
BtnStyle.position = "absolute"
BtnStyle.left = '90%'
BtnStyle.bottom = '70px'

document.body.append(btn)


btn.addEventListener('click', () => {
    alert('it job')
  })