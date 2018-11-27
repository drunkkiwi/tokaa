document.addEventListener('DOMContentLoaded', function(){

  let path_name = window.location.pathname;

  let full_option_list = document.getElementsByClassName('full-option');

  for (let i=0; i<full_option_list.length; i++){
    let full_option = full_option_list[i];

    if (full_option.getAttribute('href')==path_name){
      full_option.getElementsByClassName('underbar')[0].classList.add('underbar-up');
    }
  }

});
