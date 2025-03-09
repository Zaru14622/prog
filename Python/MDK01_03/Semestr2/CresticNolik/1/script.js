var a=1
function f(obj,y,x)
{if(obj.innerHTML!='X'&&obj.innerHTML!='O')
{if(a%2!=0){obj.innerHTML='X';a++;} else{obj.innerHTML='O';a++;}}
Chek()
}  

function Chek(){
        table = document.getElementById("t").children[0]
        c = true
        for(el of table.children){
                for(cell of el.children){
                        if(cell.innerHTML!= "X" && cell.innerHTML!= "O"){
                                c = false
                        }
                }
        }
        if(c==true){alert("Ничья")}
        if(table.children[0].children[0].innerHTML == "X" && table.children[0].children[1].innerHTML == "X" && table.children[0].children[2].innerHTML == "X" || table.children[0].children[0].innerHTML == "O" && table.children[0].children[1].innerHTML == "O" && table.children[0].children[2].innerHTML == "O"){
                if(a%2 == 0){
                        alert("Крестик")
                }
                else{
                        alert("Нолик")
                }
        }
        if(table.children[1].children[0].innerHTML == "X" && table.children[1].children[1].innerHTML == "X" && table.children[1].children[2].innerHTML == "X" || table.children[1].children[0].innerHTML == "O" && table.children[1].children[1].innerHTML == "O" && table.children[1].children[2].innerHTML == "O"){
                if(a%2 == 0){
                        alert("Крестик")
                }
                else{
                        alert("Нолик")
                }
        }
        if(table.children[2].children[0].innerHTML == "X" && table.children[2].children[1].innerHTML == "X" && table.children[2].children[2].innerHTML == "X" || table.children[2].children[0].innerHTML == "O" && table.children[2].children[1].innerHTML == "O" && table.children[2].children[2].innerHTML == "O"){
                if(a%2 == 0){
                        alert("Крестик")
                }
                else{
                        alert("Нолик")
                }
        }
        if(table.children[0].children[0].innerHTML == "X" && table.children[1].children[0].innerHTML == "X" && table.children[2].children[0].innerHTML == "X" || table.children[0].children[0].innerHTML == "O" && table.children[1].children[0].innerHTML == "O" && table.children[2].children[0].innerHTML == "O"){
                if(a%2 == 0){
                        alert("Крестик")
                }
                else{
                        alert("Нолик")
                }
        }
        if(table.children[0].children[1].innerHTML == "X" && table.children[1].children[1].innerHTML == "X" && table.children[2].children[1].innerHTML == "X" || table.children[0].children[1].innerHTML == "O" && table.children[1].children[1].innerHTML == "O" && table.children[2].children[1].innerHTML == "O"){
                if(a%2 == 0){
                        alert("Крестик")
                }
                else{
                        alert("Нолик")
                }
        }
        if(table.children[0].children[2].innerHTML == "X" && table.children[1].children[2].innerHTML == "X" && table.children[2].children[2].innerHTML == "X" || table.children[0].children[2].innerHTML == "O" && table.children[1].children[2].innerHTML == "O" && table.children[2].children[2].innerHTML == "O"){
                if(a%2 == 0){
                        alert("Крестик")
                }
                else{
                        alert("Нолик")
                }
        }
        if(table.children[0].children[0].innerHTML == "X" && table.children[1].children[1].innerHTML == "X" && table.children[2].children[2].innerHTML == "X" || table.children[0].children[0].innerHTML == "O" && table.children[1].children[1].innerHTML == "O" && table.children[2].children[2].innerHTML == "O"){
                if(a%2 == 0){
                        alert("Крестик")
                }
                else{
                        alert("Нолик")
                }
        }
        if(table.children[0].children[2].innerHTML == "X" && table.children[1].children[1].innerHTML == "X" && table.children[2].children[0].innerHTML == "X" || table.children[0].children[2].innerHTML == "O" && table.children[1].children[1].innerHTML == "O" && table.children[2].children[0].innerHTML == "O"){
                if(a%2 == 0){
                        alert("Крестик")
                }
                else{
                        alert("Нолик")
                }
        }
}