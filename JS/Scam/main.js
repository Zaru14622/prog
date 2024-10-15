// let reader = new FileReader();
// reader.readAsText("540448.html");
// reader.onload = function(){
// 	alert(reader.result);
// fetch("540448.html")
//   .then(response => response.text())
//   .then(TEXT => alert(TEXT));
// 	
// var fso = WScript.CreatObject("Scripting.FileSystemObject");
// var f = fs0.GetFile("540448.html");
// var txt = f.opensTextStream(1,-2);
// var s = txtx.readAll();
// aler(s);
// function readFile(){
// 	$ajax('540448.html',function(txt){
// 		alert(txt);
// 	});
// }
// readFile();
// let fr = new FileReader();
// fr.readAsText("540448.html");
// fr.onload = function(){
// 	console.log(fr.result);
// };
// let b = new Blob(["540448.html"],{type:'text/html'});
// console.log(b);
// let fr = new FileReader();
// fr.readAsText(File("540448.html"));
// fr.onload = function(){
// 	console.log(fr.result);
// };

var fileData = chrome.extension.getURL("540448.html"{);
var xhr = new XMLHttpRequest();
xhr.open(‘GET’, fileData, false);
xhr.onreadystatechange = function() {
	if (xhr.readyState === 4 && xhr.status === 200) {
		var content = xhr.responseText;
		// обработка прочитанного файла
	}
};
xhr.send();