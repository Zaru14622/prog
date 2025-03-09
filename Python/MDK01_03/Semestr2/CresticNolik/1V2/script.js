var a=1
function f(obj,y,x)
{if(obj.innerHTML!='X'&&obj.innerHTML!='O')
{if(a%2!=0){obj.innerHTML='X';a++;} else{obj.innerHTML='O';a++;}}
Chek(y,x)
}  

function Chek(y,x){
        table = document.getElementById("t").children[0]
        c = true
        for(el of table.children){
                for(cell of el.children){
                        if(cell.innerHTML!= "X" && cell.innerHTML!= "O"){
                                c = false
                        }
                }
        }
        if(c==true){
                alert("Ничья")
        }
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        if(x==3){
                x1 = 2
                x2 = 0
        }
        if(x==0){
                x1 = 2
                x2 = 1
        }
        else{
                x1 = x+1
                x2 = x-1
        }
        if(y==3){
                y1 = 2
                y2 = 0
        }
        if(y==0){
                y1 = 2
                y2=  1
        }
        else{
                y1 = y+1
                y2 = y-1
        }
        alert(String(x1)+" "+String(x2)+" "+String(y1)+" "+String(y2))


}