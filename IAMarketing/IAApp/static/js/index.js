/*Funció per mostrar el exercici 1*/
/*Versio 1*/
var myNav=0;
function modificarPagina(valor){
 /*   document.getElementsByClassName("row")[0].style.display='none';
    document.getElementsByClassName("row")[1].style.display='none';
    document.getElementsByClassName("row")[2].style.display='none';
    document.getElementsByClassName("row")[3].style.display='none';
    document.getElementsByClassName("row")[4].style.display='none';
    //Mostrem el que s'ha clicat
    document.getElementsByClassName("row")[valor].style.display='flex';*/


/*Versió 2
array=document.getElementsByClassName('row');
for (var i=0; i<array.length; i++){
    array[i].style.display='none';
}
document.getElementsByClassName("row")[valor].style.display='flex';
*/
//Versió 3
/*
var array=document.getElementsByClassName('fila');
var auxCon=0;

while(auxCon < array.length){
    array[auxCon].style.display='none';
    auxCon++;
}
document.getElementsByClassName("fila")[valor].style.display='flex';

    alert("Hello, Welcome to Javatpoint");
*/  
//Versio 4

    if(window.myNav != valor){ //Això s'encarrega de seleccionar totes les pestanyes en les que no estem. 

        document.getElementsByClassName('fila')[window.myNav].style.display="none";
        document.getElementsByClassName('navItem')[window.myNav].style.backgroundColor= "initial"; //Reestableix al color inicial
        document.getElementsByClassName('navItem')[window.myNav].style.color= "white"; //Li dona un color blanc
    
    
        document.getElementsByClassName('fila')[valor].style.display = "block";
        document.getElementsByClassName('navItem')[valor].style.backgroundColor= "#ddd"; //Posa el color de fons del contingut de la pestanya que hem seleccionat.
        document.getElementsByClassName('navItem')[valor].style.color= "black"; //Posa el color negre al text de la pestanya que hem seleccionat.
    
        window.myNav = valor;
    }

}

