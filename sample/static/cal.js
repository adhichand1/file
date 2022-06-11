function add(){
var x=Number(document.getElementById("a1").value);
var y=Number(document.getElementById("a2").value);
sum=x+y;
document.getElementById("a3").value=sum;
}
function sub(){
var x=Number(document.getElementById("a1").value);
var y=Number(document.getElementById("a2").value);
sub=x-y;
document.getElementById("a3").value=sub;
}
function mul(){
var x=Number(document.getElementById("a1").value);
var y=Number(document.getElementById("a2").value);
mul=x*y;
document.getElementById("a3").value=mul;
}
function div(){
var x=Number(document.getElementById("a1").value);
var y=Number(document.getElementById("a2").value);
div=x/y;
document.getElementById("a3").value=div;
}
function rem(){
var x=Number(document.getElementById("a1").value);
var y=Number(document.getElementById("a2").value);
rem=x%y;
document.getElementById("a3").value=rem;
}
