const infosMinhaConta = document.getElementById('infos');
const infosUpdate = document.getElementById('InfoUpdate');
const botaoEditar = document.getElementById('editar');

botaoEditar.addEventListener('click', () => {
    infosMinhaConta.classList.add('inativo');
    infosUpdate.classList.remove('inativo');
});

console.log(infosMinhaConta, botaoEditar)



var myModal = new bootstrap.Modal(document.getElementById('modalteste'), {
  backdrop: 'static',
  keyboard: false
});





console.log(myModal, myInput)