

document.addEventListener('DOMContentLoaded',()=>{

  copyButtons=document.getElementsByClassName('copy-button')
  

  for(let i=0;i<copyButtons.length;i++){

    copyButtons[i].addEventListener('click',(e)=>{

     let link= e.target.getAttribute('data');
    
     baseUrl='prism-gallery.herokuapp.com'
    
     let fullLink=`${baseUrl}${link}`;
      navigator.clipboard.writeText(fullLink);
      alert('Copied')
    })
  }


})
