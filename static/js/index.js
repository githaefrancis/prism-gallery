

document.addEventListener('DOMContentLoaded',()=>{

  copyButtons=document.getElementsByClassName('copy-button')
  

  for(let i=0;i<copyButtons.length;i++){

    copyButtons[i].addEventListener('click',(e)=>{

     let link= e.target.getAttribute('data');
    
     baseUrl=window.location.origin;
    
     let fullLink=`${baseUrl}${link}`;
      navigator.clipboard.writeText(fullLink);
      alert('Copied')
    })
  }


})
