function Add() {
	e = document.getElementById("elements")
	values = GetValues()
	e.innerHTML += e.children[0].outerHTML
	SetValuesAfterAdd(values)
}
function GetValues(){
	values = []
	for (i = 0;i < document.getElementById("elements").children.length;i++){
		buf = []
		for (j = 0;j < document.getElementById("elements").children[i].children.length-1;j++){
			buf.push(document.getElementById("elements").children[i].children[j].value)
		}
		values.push(buf)
	}
	return values
}
function SetValuesAfterAdd(values){
	for (i = 0;i < document.getElementById("elements").children.length-1;i++){
		for (j = 0;j < document.getElementById("elements").children[i].children.length-1;j++){
			document.getElementById("elements").children[i].children[j].value = values[i][j]
		}
	}
}
function SetValuesAfterRemove(values){
	for (i = 0;i < document.getElementById("elements").children.length;i++){
		for (j = 0;j < document.getElementById("elements").children[i].children.length-1;j++){
			document.getElementById("elements").children[i].children[j].value = values[i][j]
		}
	}
}
function Remove(label)
{
	if(document.getElementById("elements").children.length==1){
		return 0
	}
	s = ''
	elements = document.getElementById("elements")
	values = []
	for (i = 0;i < elements.children.length;i++){
		buf = []
		if(label.parentElement != elements.children[i]){
			for(j = 0;j < elements.children[i].children.length;j++){
				buf.push(elements.children[i].children[j].value)
			}
			values.push(buf)
			s += elements.children[i].outerHTML
		}
	}
	elements.innerHTML = s
	SetValuesAfterRemove(values)	
}
function PrintMass(mass)
{
	s = ""
	for(i of mass){
		for (j of i){
			s+=j+" "
		}
		s+="\n"
	}
	alert(s)
}
function ToMass()
{
	elements = document.getElementById("elements")
	res = []
	for (el of elements.children)
	{
		buf = []
		for (e of el.children){
			if(e.value == ""){
				alert("есть пустая(пустые) клетка")
				return 0
			}
			buf.push(e.value)
		}
		res.push(buf)

	}
	PrintMass(res)
}