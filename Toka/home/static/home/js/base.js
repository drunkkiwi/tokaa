document.addEventListener('DOMContentLoaded', function(){

  let external_forms = document.getElementsByClassName('formjs');

  for(let i=0; i<external_forms.length; i++){

    external_forms[i].addEventListener('submit', function(e){
      let einp = external_forms[i].getElementsByClassName('inpjs')[0];
      if (einp.value == ""){
        e.preventDefault();
      }
    });
  }

});
