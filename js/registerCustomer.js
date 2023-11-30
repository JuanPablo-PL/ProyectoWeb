$(document).ready(function() {
    // on ready
 });
 
 
 async function registrarUsuario() {
   let datos = {};
   datos.nombre = document.getElementById('txtNombre').value;
   datos.apellido = document.getElementById('txtApellido').value;
   datos.email = document.getElementById('txtEmail').value;
   datos.password = document.getElementById('txtPassword').value;
 
   // Si es que creas otro campo para repetir la contraseña
   let repetirPassword = document.getElementById('txtRepetirPassword').value;
 
   if (repetirPassword != datos.password) {
     alert('La contraseña que escribiste es diferente.');
     return;
   }
 
   const request = await fetch('api/registrar/customer', {
     method: 'POST',
     headers: {
       'Accept': 'application/json',
       'Content-Type': 'application/json'
     },
     body: JSON.stringify(datos)
   });
   alert("La cuenta fue creada con exito!");
   window.location.href = 'login.html'
 
}