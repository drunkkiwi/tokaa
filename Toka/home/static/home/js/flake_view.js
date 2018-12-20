document.addEventListener('DOMContentLoaded', function(){

  let explanfs = document.getElementsByClassName('sort-explan-fs');

  for (let i=0; i<explanfs.length; i++) {
    explanfs[i].addEventListener('click', function(){
      this.submit();
    });
  }

  let nr_query_lookup = document.getElementsByClassName('nr_query_lookup')[0];

  for(let j=0; j<explanfs.length; j++){
    let qlinp = explanfs[j].getElementsByTagName('input')[0];
    if (qlinp.value == nr_query_lookup.value){
      explanfs[j].classList.add('fs-filled');
    }
  }

});
